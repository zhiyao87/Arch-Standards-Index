#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
官方链接巡检工具。

逐个访问 data/standards.csv 里的「官方链接」，报告返回状态码，
并检查页面内容是否确实与该标准相关。

只用标准库，无第三方依赖。

用法
----
    python check_links.py                # 巡检全部
    python check_links.py --limit 10     # 只查前 10 条（快速自检）
    python check_links.py --strict       # 把「可疑」也视为失败（人工复核用）
    python check_links.py --json out.json  # 结果另存为 JSON

退出码
------
    0    无失效链接
    1    存在失效链接（bad）——便于接入 CI
    加 --strict 时，存在「可疑」（warn）也返回 1

    默认不因 warn 失败：本库有若干条目因原公告页已从住建部 CMS 移除，
    有意降级为栏目入口，这类 200 但内容不匹配属预期状态，不该让 CI 变红。
    需要严查时用 --strict 手工跑。

注意
----
政府站点常有反爬与限流。本工具：
  · 带正常浏览器 UA
  · 请求间隔默认 0.5 秒
  · 对方返回 403/429 时不计为「链接失效」，单列为「受限」

判定口径
--------
「页面标题或正文含该标准编号或名称」才算真正有效。
仅返回 200 但内容对不上（例如跳到栏目首页）会标为 warn —— 这类链接
对使用者没有价值，值得人工看一眼。
"""

import argparse
import csv
import gzip
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.request
import zlib

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "data", "standards.csv")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

LIMITED = {403, 429, 503}       # 视为「站点限制」而非「链接失效」


def fetch(url, timeout=25):
    """返回 (状态码, 页面文本)；网络层异常返回 (0, '')。"""
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            raw = r.read()
            enc = (r.headers.get("Content-Encoding") or "").lower()
            if "gzip" in enc:
                raw = gzip.decompress(raw)
            elif "deflate" in enc:
                raw = zlib.decompress(raw, -zlib.MAX_WBITS)
            return r.status, raw.decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception:
        return 0, ""


def flat(s):
    """压平字符串，便于宽松比对（去空白、书名号、常见标点）。"""
    return re.sub(r"[\s《》（）()、,，·—\-–/]", "", s or "")


def title_of(html):
    for pat in (r'<meta\s+name="ArticleTitle"\s+content="([^"]*)"',
                r"<title>(.*?)</title>"):
        m = re.search(pat, html, re.S | re.I)
        if m:
            return re.sub(r"<[^>]+>", "", m.group(1)).strip()
    return ""


def judge(row, code, html):
    """返回 (等级, 说明)。等级：ok / warn / bad / limited"""
    if code in LIMITED:
        return "limited", "HTTP %s（站点限制，非链接失效）" % code
    if code != 200:
        return "bad", "HTTP %s" % code
    ttl = title_of(html)
    if not html.strip():
        return "bad", "空响应"
    blob = flat(html[:30000])
    no, name = flat(row["编号"]), flat(row["名称"])
    if no and no in blob:
        return "ok", "命中编号｜%s" % ttl[:40]
    if name and (name in blob or name[:6] in blob):
        return "ok", "命中名称｜%s" % ttl[:40]
    return "warn", "200 但内容未命中（页面：%s）" % ttl[:40]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="只查前 N 条")
    ap.add_argument("--sleep", type=float, default=0.5, help="请求间隔秒数")
    ap.add_argument("--strict", action="store_true",
                    help="把 warn（200 但内容不匹配）也视为失败")
    ap.add_argument("--json", help="把结果写入 JSON 文件")
    args = ap.parse_args()

    with open(SRC, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if args.limit:
        rows = rows[:args.limit]

    results = []
    counts = {"ok": 0, "warn": 0, "bad": 0, "limited": 0}

    print("巡检 %d 条链接\n" % len(rows))
    for r in rows:
        url = (r.get("官方链接") or "").strip()
        code, html = fetch(url)
        level, msg = judge(r, code, html)
        counts[level] += 1
        mark = {"ok": "✔", "warn": "!", "bad": "✘", "limited": "·"}[level]
        print("%s %-22s %s" % (mark, r["编号"], msg))
        sys.stdout.flush()
        results.append({"编号": r["编号"], "名称": r["名称"],
                        "链接": url, "状态": code,
                        "等级": level, "说明": msg})
        time.sleep(args.sleep)

    print()
    print("=" * 66)
    print("正常 %d ｜ 可疑 %d ｜ 失效 %d ｜ 受限 %d"
          % (counts["ok"], counts["warn"], counts["bad"], counts["limited"]))

    if counts["warn"] or counts["bad"]:
        print()
        print("=== 需要人工确认 ===")
        for x in results:
            if x["等级"] in ("warn", "bad"):
                print("  [%s] %s\n      %s\n      %s" % (x["等级"], x["编号"], x["链接"], x["说明"]))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print()
        print("结果已写入 %s" % args.json)

    # 默认只让「真失效」触发失败；warn 多为有意降级的栏目入口，需 --strict 才计入
    failed = counts["bad"] or (args.strict and counts["warn"])
    if failed:
        print()
        print("✘ 巡检未通过（%s）" % (
            "含可疑项，--strict 模式" if counts["bad"] == 0 else "存在失效链接"))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
