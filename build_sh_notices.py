#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""数据源三：上海工程建设规范「批准 / 发布通知」索引。

背景
----
`data/sh_local.tsv` 来自市住建委「现行标准」栏目，只收**当前仍现行**的规范，
且只有编号 / 名称 / 日期 / 全文 PDF —— 没有批准文号，也看不到批准通知原件。

而规范是怎么来的？每一本上海市工程建设规范都由市住建委发一纸
「关于批准《XXX》为上海市工程建设规范的通知」。这些通知散落在政府发文里，
**栏目更新比批准慢半拍**：2026 年新批准的一批（地下车站连通、桥梁改扩建、
模块化建筑导则等）在「现行标准」栏目里根本查不到，只能从批准通知看到。

把两批数据拼起来，才能回答两个不同问题：
- 这本规范现在有效吗、全文在哪 → sh_local.tsv
- 最近批了什么新规范、依据哪个文号 → sh_notices.tsv

数据源
------
输入：`gov_docs.csv`（Shanghai-Gov-Docs-Index 仓库的权威数据源，用 --src 指定）
      `data/sh_std_raw.json`（本库已有，住建委现行标准栏目原始抓取，用于补编号与全文 PDF）
输出：`data/sh_notices.tsv`（**不要手改**，改口径改本脚本后重跑）

用法
----
    python build_sh_notices.py --src <gov_docs.csv 路径>
    python build_sh_notices.py --src <路径> --raw data/sh_std_raw.json -o data/sh_notices.tsv

零第三方依赖。
"""

import argparse
import csv
import io
import json
import os
import re
import sys
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RAW = os.path.join(BASE, "data", "sh_std_raw.json")
DEFAULT_OUT = os.path.join(BASE, "data", "sh_notices.tsv")
SITE = "https://zjw.sh.gov.cn"   # 现行标准栏目的 url 字段常是站根相对路径，需补域名

COLS = ["分组", "标准名", "编号", "批准日期", "文号", "发布单位",
        "官方链接", "全文PDF", "红头PDF", "附件", "备注"]

# ---------- 抽取口径 ----------
BOOK = re.compile(r"[《<]([^》>]{3,60})[》>]")

APPROVE = re.compile(r"批准.{0,100}?(工程建设规范|标准设计|地方标准)")
ISSUE = re.compile(r"(发布|印发|出台).{0,80}?(导则|技术规定|技术标准|技术规程|"
                   r"审查要点|编制深度规定|技术导则|设计标准)")
WIDE = re.compile(r"(技术标准|技术规程|技术要求|技术规定)")

NOT_NOISE = re.compile(
    "复审|征集|编制计划|宣贯|培训|终止|工作要点|发展报告|认定工作|"
    "任务分解|继续教育")

# ---------- 专业分组 ----------
# 顺序即优先级：命中靠前者胜出。建筑工程视角，与 README 章节一致。
GROUPS = [
    ("消防与人防", "消防|防火|防排烟|灭火|人防|民防|防空|警报|灾害"),
    ("绿色建筑与节能", "绿色建筑|绿建|节能|超低能耗|近零能耗|零能耗|碳排放|"
                       "可再生能源|太阳能|光储直柔|用能|能源审计|绿色生态|绿色建材"),
    ("装配式与外围护", "装配式|预制|装配|模块化|外围护|幕墙|外墙|保温|"
                       "屋盖|门窗|遮阳"),
    ("改造与历史建筑", "既有建筑|既有住宅|改造|修缮|历史建筑|风貌|更新|"
                       "加固|鉴定|加装电梯|承重结构"),
    ("结构与抗震", "结构|抗震|地基|基础|基坑|桩|混凝土|钢结构|木结构|"
                   "索结构|预应力|砌体|砂浆|山工程"),
    ("设备与智能化", "设备|给排水|排水|电气|暖通|空调|通风|供暖|燃气|天然气|"
                     "管道|管线|智能化|信息化|BIM|建筑信息模型|通信|广电|"
                     "接入网|光纤|照明|电梯|热泵|变压器"),
    ("轨道交通与地下工程", "轨道|地铁|盾构|隧道|地下|管廊|地下空间|"
                           "连续墙|顶管"),
    ("市政与道路", "道路|公路|桥梁|桥面|市政|交通|公交|公共汽车|电车|"
                   "出租汽车|候车|停车场|停车|综合杆|养护|路面|护岸|疏浚"),
    ("水务与海绵", "水|海绵|雨水|河道|防汛|供水|污水|管网|圩区|水闸|泵闸"),
    ("绿化与市容", "绿化|绿地|公园|行道树|市容|环卫|公厕|垃圾|渣土|景观|"
                   "绿道|户外招牌|公益林"),
    ("勘察与测绘", "勘察|测绘|测量|物探|地质|岩土|沉降|监测"),
    ("规划与不动产", "规划|国土|土地|不动产|城市设计|建设用地|地理实体|地理信息"),
    ("建筑与住区", "住宅|住区|居住|建筑|养老|办公|学校|医院|商业|"
                   "保障性住房|租赁住房|装修|室内|村民住房|餐饮|"
                   "设计标准|设计导则"),
    ("施工与质量安全", "施工|质量|安全|验收|检测|评定|监理|造价|招标|评估"),
]
DEFAULT_GROUP = "其他"


def group_of(name):
    for g, kw in GROUPS:
        if re.search(kw, name):
            return g
    return DEFAULT_GROUP


# ---------- 名称对齐 ----------
PUNC = re.compile(r"[《》〈〉（）()\s、，,。:：;；\"'\-—_`·]")
TAIL = re.compile(r"(标准|规范|规程|导则|技术要求|技术规定|图集|设计标准)$")


def key(s):
    s = PUNC.sub("", s or "")
    s = re.sub(r"^上海市", "", s)
    s = TAIL.sub("", s)
    return s


def clean(v):
    """TSV 单元格：去掉会破坏分隔的字符。"""
    return re.sub(r"[\t\r\n]+", " ", (v or "")).strip()


def abs_url(u):
    """站根相对路径补域名（与 build_sh_local.py 口径一致）。"""
    u = (u or "").strip()
    if not u:
        return ""
    return SITE + u if u.startswith("/") else u


def first_attach(v):
    """附件字段是多值的：`文件名|URL ｜ 文件名|URL`。只取第一个 URL。

    不取全部的原因：markdown 的 `[文字](目标)` 只能是一个链接，
    把多个 URL 拼进去会生成一条必死的链。要全部附件请查原库。
    """
    v = (v or "").strip()
    if not v:
        return ""
    first = re.split(r"｜|\|", v)[0].strip()
    if first.startswith("http"):
        return first
    # 形如「文件名|URL」：取竖线右侧
    parts = v.split("｜")[0]
    if "|" in parts:
        url = parts.split("|", 1)[1].strip()
        if url.startswith("http"):
            return url
    return ""


def pick(title):
    if NOT_NOISE.search(title):
        return None
    if APPROVE.search(title):
        return "批准为工程建设规范"
    if ISSUE.search(title):
        return "发布/印发"
    if WIDE.search(title):
        return "技术类"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True,
                    help="gov_docs.csv 路径（Shanghai-Gov-Docs-Index 的 data/gov_docs.csv）")
    ap.add_argument("--raw", default=DEFAULT_RAW,
                    help="住建委现行标准原始 JSON，用于补编号与全文 PDF")
    ap.add_argument("-o", "--out", default=DEFAULT_OUT)
    a = ap.parse_args()

    if not os.path.exists(a.src):
        print("✗ 找不到 gov_docs.csv：%s" % a.src)
        return 1

    # 现行标准：名称 → 记录（补编号 / 实施日期 / 全文 PDF）
    by_key = {}
    if os.path.exists(a.raw):
        raw = json.load(open(a.raw, encoding="utf-8"))
        if isinstance(raw, dict):
            raw = raw.get("data") or raw.get("list") or raw.get("rows") or []
        for x in raw:
            mc = (x.get("mc") or "").strip()
            if mc:
                by_key.setdefault(key(mc), x)
    print("现行标准库 %d 条（用于补编号与全文 PDF）" % len(by_key))

    with io.open(a.src, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    print("gov_docs.csv %d 条" % len(rows))

    out, seen = [], set()
    n_hit = 0
    for r in rows:
        title = (r.get("标题") or "").strip()
        kind = pick(title)
        if not kind:
            continue
        names = [n.strip() for n in BOOK.findall(title)]
        if not names:
            continue
        for nm in names:
            short = re.sub(r"^上海市", "", nm)
            dup = (key(short), (r.get("发布日期") or "").strip())
            if dup in seen:
                continue
            seen.add(dup)
            std = by_key.get(key(short)) or by_key.get(key(nm))
            hit = std is not None
            n_hit += 1 if hit else 0
            out.append({
                "分组": group_of(short),
                "标准名": clean(nm),
                "编号": clean(std.get("bh", "")) if hit else "",
                "批准日期": clean(r.get("发布日期")),
                "文号": clean(r.get("文号")),
                "发布单位": clean(r.get("发布单位")),
                "官方链接": clean(r.get("官方链接")),
                "全文PDF": abs_url(std.get("url", "")) if hit else "",
                "红头PDF": clean(r.get("红头PDF")),
                "附件": first_attach(r.get("附件")),
                "备注": ("现行标准栏目已收录" if hit else "新批准，现行标准栏目未收录")
                        + ("/实施 %s" % clean(std.get("ss", "")) if hit and std.get("ss") else ""),
            })

    out.sort(key=lambda x: (x["分组"], x["批准日期"]), reverse=False)
    out.sort(key=lambda x: x["批准日期"] or "", reverse=True)

    with io.open(a.out, "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(COLS) + "\n")
        for r in out:
            f.write("\t".join(r[c] for c in COLS) + "\n")

    print()
    print("✓ %s —— %d 条（补上编号 %d 条，占 %.0f%%）"
          % (a.out, len(out), n_hit, 100.0 * n_hit / max(1, len(out))))
    print()
    for g, c in Counter(r["分组"] for r in out).most_common():
        print("   %-14s %d" % (g, c))
    return 0


if __name__ == "__main__":
    sys.exit(main())
