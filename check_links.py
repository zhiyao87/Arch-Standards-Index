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
import urllib.parse
import urllib.request
import zlib

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "data", "standards.csv")
SH_LOCAL = os.path.join(BASE, "data", "sh_local.tsv")
SH_NOTICES = os.path.join(BASE, "data", "sh_notices.tsv")

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

CTX = ssl.create_default_context()
CTX.check_hostname = False
CTX.verify_mode = ssl.CERT_NONE

LIMITED = {403, 429, 503}       # 视为「站点限制」而非「链接失效」


def encode_url(u):
    """把 URL 路径里的非 ASCII 字符转成 percent-encoding。

    坑（2026-09-11 实测踩到）：urllib 不会像浏览器那样自动编码，
    直接请求含中文文件名的 URL 会抛
        UnicodeEncodeError: 'ascii' codec can't encode characters
    而 curl / 浏览器都自动处理 —— 于是出现「curl 测是 200、urllib 测全挂」
    的假象，极易误判为链接失效。上海住建委官网有大量中文文件名 PDF。
    """
    p = urllib.parse.urlparse(u)
    path = urllib.parse.quote(p.path, safe="/%")
    return urllib.parse.urlunparse((p.scheme, p.netloc, path, p.query, "", ""))


def fetch(url, timeout=25):
    """返回 (状态码, 页面文本, content-type)；网络层异常返回 (0, '', '')。

    PDF 只读前 8 KB —— 上海住建委的标准直链是 5–10 MB 的 PDF，
    全读一遍纯属浪费；只要拿到 200 和 content-type 就够了。
    """
    req = urllib.request.Request(encode_url(url), headers={
        "User-Agent": UA,
        "Accept-Encoding": "gzip, deflate",
        "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            ctype = (r.headers.get("Content-Type") or "").lower()
            raw = r.read(8192) if "pdf" in ctype else r.read()
            enc = (r.headers.get("Content-Encoding") or "").lower()
            if "gzip" in enc and raw:
                try:
                    raw = gzip.decompress(raw)
                except Exception:
                    pass
            elif "deflate" in enc and raw:
                try:
                    raw = zlib.decompress(raw, -zlib.MAX_WBITS)
                except Exception:
                    pass
            return r.status, raw.decode("utf-8", "replace"), ctype
    except urllib.error.HTTPError as e:
        return e.code, "", ""
    except Exception:
        return 0, "", ""


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


def is_spa(html):
    """判断是否为「前端渲染空壳页」。

    上海市统一政策发布平台的详情页（shanghai.gov.cn/zhengce/detail?businessId=…）
    是纯 JS 渲染：HTTP 200，但原始 HTML 只有 4 KB 空壳、20 个 <script>，
    正文一个字都没有。用 urllib 抓必然「内容未命中」—— 那是**误报**，不是死链。
    2026-09-11 实测：批准通知的发布页里 220/369 条（60%）都是这种页。
    同样的坑在住建部栏目页上也存在（见本文件顶部说明）。
    """
    if html.count("<script") < 5:
        return False
    body = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    text = re.sub(r"<[^>]+>", " ", body)
    return len(re.sub(r"\s+", " ", text).strip()) < 300


def judge(row, code, html, ctype=""):
    """返回 (等级, 说明)。等级：ok / warn / bad / limited"""
    if code in LIMITED:
        return "limited", "HTTP %s（站点限制，非链接失效）" % code
    if code != 200:
        return "bad", "HTTP %s" % code
    # 直接指向标准全文 PDF 的链接（上海住建委官网）：能下载即为有效。
    # 这类 PDF 部分是扫描件，没有文本层，硬要核对标准号会误报。
    if "pdf" in ctype:
        return "ok", "PDF 可下载"
    ttl = title_of(html)
    if not html.strip():
        return "bad", "空响应"
    # 前端渲染页：200 但 urllib 拿不到正文，无法自动核验，交人工（不算失效）
    if is_spa(html):
        return "limited", "HTTP 200（前端渲染页，正文需浏览器加载｜%s）" % ttl[:30]
    blob = flat(html[:30000])
    # 批准通知没有编号时（新批准、现行标准栏目未收录），只能靠标准名比对；
    # 两个都没有则无从判定，标 warn 交人工 —— 不要当成失效。
    no = flat(row.get("编号"))
    name = flat(row.get("名称") or row.get("标准名"))
    if no and no in blob:
        return "ok", "命中编号｜%s" % ttl[:40]
    if name and (name in blob or name[:6] in blob):
        return "ok", "命中名称｜%s" % ttl[:40]
    if not no and not name:
        return "warn", "200 但无编号/名称可比对（页面：%s）" % ttl[:40]
    return "warn", "200 但内容未命中（页面：%s）" % ttl[:40]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="只查前 N 条")
    ap.add_argument("--sleep", type=float, default=0.5, help="请求间隔秒数")
    ap.add_argument("--strict", action="store_true",
                    help="把 warn（200 但内容不匹配）也视为失败")
    ap.add_argument("--json", help="把结果写入 JSON 文件")
    ap.add_argument("--only", default="all",
                    choices=["all", "standards", "sh_local", "sh_notices"],
                    help="只巡检某个数据源（默认 all）")
    args = ap.parse_args()

    # 覆盖三个数据源：国标/行标（standards.csv）、上海现行规范（sh_local.tsv）、
    # 规范批准通知（sh_notices.tsv）。后两者链接指向 PDF 直链，含中文文件名，
    # 正好检验 percent-encoding 是否生效。
    # 批准通知每条贡献两条链接：发布页（官方链接）与标准全文 PDF（全文PDF）。
    rows = []
    if args.only in ("all", "standards"):
        with open(SRC, encoding="utf-8-sig", newline="") as f:
            rows += [r for r in csv.DictReader(f) if (r.get("官方链接") or "").strip()]
    if args.only in ("all", "sh_local") and os.path.exists(SH_LOCAL):
        with open(SH_LOCAL, encoding="utf-8-sig", newline="") as f:
            rows += [r for r in csv.DictReader(f, delimiter="\t")
                     if (r.get("官方链接") or "").strip()]
    if args.only in ("all", "sh_notices") and os.path.exists(SH_NOTICES):
        with open(SH_NOTICES, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                # 字段名对齐到 judge() 期望的「编号 / 名称」，缺失留空即可
                base = {"编号": (r.get("编号") or "").strip(),
                        "名称": (r.get("标准名") or "").strip()}
                for col in ("官方链接", "全文PDF"):
                    u = (r.get(col) or "").strip()
                    if u:
                        rows.append(dict(base, 官方链接=u))
    if args.limit:
        rows = rows[:args.limit]

    results = []
    counts = {"ok": 0, "warn": 0, "bad": 0, "limited": 0}

    print("巡检 %d 条链接\n" % len(rows))
    for r in rows:
        url = (r.get("官方链接") or "").strip()
        code, html, ctype = fetch(url)
        level, msg = judge(r, code, html, ctype)
        counts[level] += 1
        mark = {"ok": "✔", "warn": "!", "bad": "✘", "limited": "·"}[level]
        # 批准通知常没有编号，退化到标准名，免得整列空白对不上行
        label = (r.get("编号") or "").strip() or (r.get("名称") or "")[:20]
        name = (r.get("名称") or r.get("标准名") or "").strip()
        print("%s %-22s %s" % (mark, label, msg))
        sys.stdout.flush()
        results.append({"编号": label, "名称": name,
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
