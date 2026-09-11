#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从上海市住建委「现行标准」栏目数据中，提取建筑设计常用条目并验证官方 PDF 直链。

数据来源（脚本从已抓取的页面 JSON 解析，不重新联网取数据）：
    https://zjw.sh.gov.cn/xxbz/index.html      现行标准栏目
每个条目的官方链接形如：
    https://zjw.sh.gov.cn/cmsres/.../xxx.pdf    （CMS 生成，305 条）
    https://zjw.sh.gov.cn/shsd/userfiles/xxx.pdf（旧路径，182 条）

判定口径
--------
本表只收录**上海工程建设规范**（DGJ08 / DG/TJ08 系列）。
上海市住建委将其一律标为「推荐性标准」（栏目内 0 条标注"强制性"），
与其含强制性条文的事实不冲突 —— 参见《标准化法》第 2 条：
地方标准一律为推荐性标准。故版权分层统一为 C（受著作权法保护）。

用法
----
    python build_sh_local.py            # 只提取与统计，不联网
    python build_sh_local.py --verify   # 联网验证每条 PDF 直链
"""

import argparse
import collections
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(BASE, "data", "sh_std_raw.json")   # 原文抓取结果
OUT = os.path.join(BASE, "data", "sh_local.tsv")

SITE = "https://zjw.sh.gov.cn"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

# ── 入选清单 ────────────────────────────────────────────────────────
# 按建筑设计日常引用频次挑选。凡有新旧两版的，只取新版。
# 分组仅用于生成 README 表格时归类。
PICK = {
    "设计基础": [
        "DGJ08-20-2019",      # 住宅设计标准
        "DGJ08-11-2018",      # 地基基础设计标准
        "DG/TJ08-9-2023",     # 建筑抗震设计标准
        "DGJ08-205-2015",     # 居住建筑节能设计标准
        "DGJ08107-2015",      # 公共建筑节能设计标准
        "DGJ08-2143-2021",    # 公共建筑绿色设计标准
        "DGJ08-2139-2021",    # 住宅建筑绿色设计标准
        "DG/TJ08-7-2021",     # 建筑工程交通设计及停车库（场）设置标准
        "DG/TJ08-88-2021",    # 建筑防排烟系统设计标准
        "DG/TJ08-56-2019",    # 建筑幕墙工程技术标准
        "DG/TJ08-2242-2017",  # 民用建筑外窗应用技术规程
        "DG/TJ08-2328-2020",  # 建筑风环境气象参数标准
        "DG/TJ08-2314-2020",  # 建筑同层排水系统应用技术标准
        "DG/TJ08-2201-2016",  # 建筑信息模型应用标准
    ],
    "住宅与住区": [
        "DG/TJ08-2291-2019",   # 保障性住房设计标准
        "DG/TJ08-2291B-2022",  # 保障性住房设计标准（保障性租赁住房新建分册）
        "DG/TJ08-2291C-2022",  # 保障性住房设计标准（保障性租赁住房改建分册）
        "DG/TJ08-2178-2021",   # 全装修住宅室内装修设计标准
        "DG/TJ08-2381-2021",   # 既有多层住宅加装电梯技术标准
        "DG/TJ08-2374-2022",   # 既有住宅小区宜居改造技术标准
        "DG/TJ08-2029-2021",   # 多高层钢结构住宅技术标准
        "DG/TJ08-82-2020",     # 养老设施建筑设计标准
        "DG/TJ08-2247-2017",   # 绿色养老建筑评价标准
        "DG/TJ08-2243-2017",   # 市属高校建筑规划面积标准
        "DG/TJ08-12-2004",     # 普通中小学校建设标准
        "DG/TJ08-45-2005",     # 普通幼儿园建设标准
    ],
    "消防与安全": [
        "DG/TJ08-2408-2022",   # 城市综合体消防技术标准
        "DG/TJ08-2343-2020",   # 大型物流建筑消防设计标准
        "DG/TJ08-2410-2022",   # 文物和优秀历史建筑消防技术标准
        "DG/TJ08-2409-2022",   # 老旧住宅小区消防改造技术标准
        "DGJ08-2173-2016",     # 展览建筑及布展设计防火规程
        "DGJ08-2048-2016",     # 民用建筑电气防火设计规程
        "DGJ08-94-2007",       # 民用建筑水灭火系统设计规程
        "DGJ08-2164-2015",     # 民用建筑外保温材料防火技术规程
        "DG/TJ08-2177-2015",   # 建筑工程消防施工质量验收规范
        "DG/TJ08-2188-2015",   # 应急避难场所设计规范
    ],
    "改造与历史建筑": [
        "DG/TJ08-108-2014",    # 优秀历史建筑保护修缮技术规程
        "DG/TJ08-2403-2022",   # 优秀历史建筑抗震鉴定与加固标准
        "DG/TJ08-2338-2020",   # 既有建筑绿色改造技术标准
        "DG/TJ08-2235-2017",   # 既有地下建筑改扩建技术规范
        "DG/TJ08-2136-2022",   # 既有居住建筑节能改造技术标准
        "DG/TJ08-2137-2022",   # 既有公共建筑节能改造技术标准
    ],
    "装配式与外围护": [
        "DG/TJ08-2198-2019",   # 装配式建筑评价标准
        "DG/TJ08-2071-2016",   # 装配整体式混凝土居住建筑设计规程
        "DG/TJ08-2154-2014",   # 装配整体式混凝土公共建筑设计规程
        "DG/TJ08-2158-2023",   # 预制混凝土夹心保温外墙应用技术标准
        "DG/TJ08-2433A-2023",  # 外墙保温一体化系统应用技术标准（预制混凝土反打保温外墙）
        "DG/TJ08-2433B-2023",  # 外墙保温一体化系统应用技术标准（现浇混凝土反打保温外墙）
        "DG/TJ08-2365-2021",   # 建筑浮筑楼板保温隔声系统应用技术标准
    ],
    "结构与抗震": [
        "DGJ08-81-2021",       # 现有建筑抗震鉴定与加固标准
        "DG/TJ08-2326-2020",   # 建筑消能减震及隔震技术标准
        "DGJ08-69-2015",       # 预应力混凝土结构设计规程
        "DG/TJ08-019-2018",    # 建筑索结构技术标准
        "DG/TJ08-52-2020",     # 空间格构结构技术标准
        "DG/TJ08-2192-2016",   # 工程木结构设计规范
        "DG/TJ08-2350-2021",   # 大跨度建筑空间结构抗连续倒塌设计标准
    ],
    "绿色建筑与专项": [
        "DG/TJ08-2090-2020",   # 绿色建筑评价标准
        "DG/TJ08-2040-2021",   # 公共建筑绿色及节能工程智能化技术标准
        "DG/TJ08-2263-2018",   # 城市轨道交通上盖建筑设计标准
        "DG/TJ08-60-2017",     # 机械式停车库（场）设计规程
    ],
}

ALL_PICKS = [b for v in PICK.values() for b in v]


def norm_no(no):
    """规范化官网数据里的标准编号。

    官网 JSON 的 `bh` 字段格式不统一，实测存在这些脏数据：
        DG/J08-20-2019      多余斜杠
        DGTJ08-2154-2014    缺 /T
        DGJ08107-2015       缺横杠分隔（实为 DGJ08-107-2015）
        DG/TJ 08-2075-2022  含空格
        DG/TJ08 2397-2022   空格代替横杠
        DG\\TJ08-2336-2020  反斜杠
        DJ/TJ08-10-2022     拼写错误
    """
    s = re.sub(r"[\s　]+", "", (no or "")).upper()
    s = s.replace("\\", "/").replace("DJ/TJ", "DG/TJ")
    s = s.replace("DG/J", "DGJ").replace("DGTJ", "DG/TJ")

    m = re.match(r"^(.*?)-?(\d{4})$", s)
    if not m:
        return s
    head, year = m.group(1).rstrip("-"), m.group(2)
    m2 = re.match(r"^(DG/TJ|DGJ)0?8-?0*(\d{1,4})([A-Z]?)$", head)
    if m2:
        prefix, num, suf = m2.groups()
        return "%s08-%s%s-%s" % (prefix, num, suf, year)
    return s


def load_raw():
    """读原始抓取结果，按规范化编号建索引。

    同一标准化编号若有多条记录（官网列表新旧版并存，如 住宅设计标准
    DGJ08-20-2019 与 DG/J08-20-2019），取**实施日期最晚**的那条。
    """
    if not os.path.exists(CACHE):
        sys.exit("缺少 %s —— 请先运行抓取步骤" % CACHE)
    with open(CACHE, encoding="utf-8") as f:
        recs = json.load(f)
    out = {}
    for r in recs:
        k = norm_no(r["bh"])
        old = out.get(k)
        if old is None or (r.get("ss") or "") > (old.get("ss") or ""):
            out[k] = r
    return out


def encode_url(u):
    """把 URL 路径里的非 ASCII 字符（中文文件名）转成 percent-encoding。

    坑：urllib 不像浏览器那样自动编码，直接传含中文的 URL 会抛
        UnicodeEncodeError: 'ascii' codec can't encode characters
    而 curl 和浏览器都会自动处理，所以用 curl 测是通的、
    用 urllib 测就全部"失败"——极易误判为链接失效。

    住建委官网有相当一部分 PDF 用了中文文件名，例如
        /shsd/userfiles/107公共建筑节能设计标准20160504104711.pdf
    这类 URL 必须编码后才能用 urllib 请求。
    """
    p = urllib.parse.urlparse(u)
    path = urllib.parse.quote(p.path, safe="/%")   # 保留 / 和已有的 %
    return urllib.parse.urlunparse((p.scheme, p.netloc, path, p.query, "", ""))


def fetch(url, timeout=30):
    req = urllib.request.Request(encode_url(url), headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            head = r.read(2048)
            return r.status, r.headers.get("Content-Type", ""), len(head)
    except urllib.error.HTTPError as e:
        return e.code, "", 0
    except Exception:
        return 0, "", 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verify", action="store_true", help="联网验证 PDF 直链")
    ap.add_argument("--sleep", type=float, default=0.4)
    args = ap.parse_args()

    recs = load_raw()
    print("原始记录 %d 条\n" % len(recs))

    rows = []
    missing = []
    for group, codes in PICK.items():
        for c in codes:
            r = recs.get(norm_no(c))
            if not r:
                missing.append(c)
                continue
            rows.append({
                "分组": group,
                "编号": norm_no(r["bh"]),
                "名称": r["mc"].strip(),
                "批准日期": (r["pz"] or "").strip()[:10],
                "实施日期": (r["ss"] or "").strip()[:10],
                "官方链接": SITE + r["url"] if r["url"].startswith("/") else r["url"],
                "原始编号": r["bh"],
            })

    print("命中 %d 条，未命中 %d 条" % (len(rows), len(missing)))
    if missing:
        print("未命中：")
        for m in missing:
            print("  ", m)
    print()

    if args.verify:
        print("=== 验证 PDF 直链 ===")
        bad = []
        for i, r in enumerate(rows, 1):
            code, ctype, _ = fetch(r["官方链接"])
            ok = code == 200 and ("pdf" in ctype.lower() or ctype == "")
            mark = "OK " if ok else "FAIL"
            if not ok:
                bad.append((r["编号"], code, ctype))
            print("  [%s] %-20s %s  %s" % (mark, r["编号"], code, ctype[:30]))
            sys.stdout.flush()
            time.sleep(args.sleep)
        print()
        print("通过 %d / 失败 %d" % (len(rows) - len(bad), len(bad)))
        for b in bad:
            print("  失败：", b)
        rows = [r for r in rows if r["编号"] not in {b[0] for b in bad}]

    # 输出 TSV
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("分组\t编号\t名称\t批准日期\t实施日期\t官方链接\n")
        for r in rows:
            f.write("\t".join([r["分组"], r["编号"], r["名称"],
                               r["批准日期"], r["实施日期"], r["官方链接"]]) + "\n")
    print()
    print("已写入 %s（%d 条）" % (OUT, len(rows)))

    # 分组统计
    print()
    for k, v in collections.Counter(r["分组"] for r in rows).items():
        print("  %-14s %d" % (k, v))


if __name__ == "__main__":
    main()
