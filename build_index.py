#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
建筑标准规范索引库 —— 索引生成器

单一数据源：data/standards.csv
输出：
  README.md                     仓库首页（含合规声明与完整索引表）
  obsidian/标准索引.md          Obsidian 主索引页
  obsidian/standards/*.md       每条标准一个笔记（YAML frontmatter）
  data/standards_excel.csv      UTF-8 BOM 版，Excel 可直接双击打开

用法：
  python build_index.py
"""

import csv
import os
import re
import urllib.parse
from collections import OrderedDict

BASE = os.path.dirname(os.path.abspath(__file__))
TITLE = "建筑设计规范索引"   # README 标题，与 GitHub 仓库名（Arch-Standards-Index）对应
REPO = "Arch-Standards-Index"  # GitHub 仓库名，用于 README 里的 clone 地址与目录结构
SRC = os.path.join(BASE, "data", "standards.csv")
README = os.path.join(BASE, "README.md")
OBS_DIR = os.path.join(BASE, "obsidian")
OBS_INDEX = os.path.join(OBS_DIR, "标准索引.md")
OBS_STD = os.path.join(OBS_DIR, "standards")
EXCEL_CSV = os.path.join(BASE, "data", "standards_excel.csv")
NOTICE_EXCEL_CSV = os.path.join(BASE, "data", "sh_notices_excel.csv")
NOTICE_COLS = ["分组", "标准名", "编号", "批准日期", "文号", "发布单位",
               "官方链接", "全文PDF", "红头PDF", "附件", "备注"]
SH_LOCAL = os.path.join(BASE, "data", "sh_local.tsv")   # 上海工程建设规范，由 build_sh_local.py 从市住建委官网生成
SH_NOTICES = os.path.join(BASE, "data", "sh_notices.tsv")  # 上海规范批准/发布通知索引，由 build_sh_notices.py 从 gov_docs.csv 生成

# 上海数据源只有「分组」概念，映射到本库统一的「分类」体系。
# 分组信息仍保留在 row["分组"] 里，供 README 分节展示。
SH_CATEGORY = {
    "设计基础": "建筑",
    "住宅与住区": "建筑",
    "消防与安全": "专项工程",
    "改造与历史建筑": "既有建筑",
    "装配式与外围护": "建筑",
    "结构与抗震": "结构",
    "绿色建筑与专项": "专项工程",
}
SH_GROUP_ORDER = ["设计基础", "住宅与住区", "消防与安全", "改造与历史建筑",
                  "装配式与外围护", "结构与抗震", "绿色建筑与专项"]

# 批准通知的专业分组（由 build_sh_notices.py 的 GROUPS 常量产出，顺序保持一致）
NOTICE_GROUP_ORDER = [
    "建筑与住区", "结构与抗震", "消防与人防", "绿色建筑与节能",
    "装配式与外围护", "改造与历史建筑", "设备与智能化",
    "轨道交通与地下工程", "市政与道路", "水务与海绵", "绿化与市容",
    "勘察与测绘", "施工与质量安全", "规划与不动产", "其他",
]

CATEGORY_ORDER = ["结构", "建筑", "设备与市政", "施工与安全", "既有建筑", "专项工程", "制图"]

TAG_BY_COPYRIGHT = {
    "A-不受著作权保护": "版权/不受保护",
    "B-受著作权保护": "版权/受保护-国标",
    "C-受著作权保护": "版权/受保护-行标",
}


def load_sh_local():
    """读上海工程建设规范数据源（data/sh_local.tsv）。

    该文件由 build_sh_local.py 从上海市住建委「现行标准」栏目生成，
    官方数据里没有「分类 / 属性 / 版权分层」这几个字段，在这里补齐：
    上海将 DGJ08 / DG/TJ08 一律标为推荐性标准（栏目内 0 条标注"强制性"），
    依《标准化法》第 2 条地方标准均为推荐性，故版权分层统一为 C。
    """
    if not os.path.exists(SH_LOCAL):
        return []
    out = []
    with open(SH_LOCAL, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            no = (r.get("编号") or "").strip()
            if not no:
                continue
            group = (r.get("分组") or "").strip()
            out.append({
                "编号": no,
                "名称": (r.get("名称") or "").strip(),
                "分类": SH_CATEGORY.get(group, "建筑"),
                "属性": "推荐性",
                "实施日期": (r.get("实施日期") or "").strip(),
                "状态": "现行",
                "官方链接": (r.get("官方链接") or "").strip(),
                "版权分层": "C-受著作权保护",
                "备注": "上海市工程建设规范（市住建委现行标准栏目收录）",
                "分组": group,
            })
    return out


def load_sh_notices():
    """读第三个数据源：上海工程建设规范「批准 / 发布通知」索引（data/sh_notices.tsv）。

    与 sh_local.tsv 的区别 —— 两者回答的是不同问题：
      sh_local.tsv   这本规范**现在有效吗**、全文 PDF 在哪（只收现行）
      sh_notices.tsv **最近批了什么新规范**、依据哪个文号、通知原件在哪

    后者由 build_sh_notices.py 从 Shanghai-Gov-Docs-Index 的 gov_docs.csv 生成，
    **不要手改**。返回结构只有「分组 / 标准名 / 编号 / 批准日期 / 文号 / 链接们」，
    没有「属性 / 版权分层 / 状态」—— 因为批准通知本身是行政文件，
    不是标准文本，不该混进标准表的版权分层统计里。
    """
    if not os.path.exists(SH_NOTICES):
        return []
    out = []
    with open(SH_NOTICES, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            name = (r.get("标准名") or "").strip()
            if not name:
                continue
            out.append({k: (v or "").strip() for k, v in r.items() if k})
    return out


def load_rows():
    # utf-8-sig：容忍数据源带 BOM（Excel 另存为 CSV 时常见）
    with open(SRC, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fields = [f.strip() for f in (reader.fieldnames or [])]
        rows = []
        for r in reader:
            clean = {}
            for k, v in r.items():
                if k is None:
                    continue
                clean[k.strip()] = (v or "").strip()
            if clean.get("编号"):
                rows.append(clean)
    # 上海数据作为独立源追加，不写进 standards.csv ——
    # 它可由脚本从官网重新抓取更新，无需手工维护。
    return fields, rows + load_sh_local()


def safe_filename(row):
    raw = "%s %s" % (row["编号"], row["名称"])
    return re.sub(r'[\\/:*?"<>|]', "-", raw).strip()


def cell(value, dash="-"):
    v = (value or "").strip()
    return v if v else dash


def is_mandatory(row):
    return (row.get("属性") or "").strip() == "强制性"


def is_gb550(row):
    """强制性工程建设规范：GB 55001—GB 55038 这一批全文强制规范。"""
    return re.match(r"^GB\s*55\d", (row.get("编号") or "").strip()) is not None


def is_sh_local(row):
    """上海工程建设规范：DGJ08 / DG/TJ08 系列（上海市住建委发布）。"""
    no = (row.get("编号") or "").strip().upper()
    return no.startswith("DGJ08") or no.startswith("DG/TJ08")


def link_md(url, label="官方发布页"):
    """生成 markdown 链接，URL 做 percent-encoding。

    为什么必须编码：markdown 的 `[文字](目标)` 在**空格处会截断目标**，
    括号也会让解析器提前收尾。上海住建委官网有 11 条 PDF 用了中文文件名，
    其中一条还带空格与括号：
        .../2201建筑信息模型应用标准 (1)20161114141911.pdf
    不编码的话，读者点进去就是断链 —— 这类问题在仓库页面里看不出来，
    只有真正点击才会暴露。

    safe 里保留 URL 结构字符，但**不含括号**：括号必须编码成 %28/%29，
    否则会破坏 markdown 语法。保留 % 是为了不二次编码已编码的部分。
    """
    u = (url or "").strip()
    if not u:
        return "-"
    safe = urllib.parse.quote(u, safe=":/?#[]@!$&'*+,;=%~.-_")
    return "[%s](%s)" % (label, safe)


# ---------------------------------------------------------------- README

def build_readme(rows, notices=None):
    notices = notices or []
    total = len(rows)
    # 分组按「编号体系」而非「属性」——属性和版权分层是逐条的法律判断，
    # 放在表格列里呈现；章节划分按标准体系走，读者才能对得上。
    mand = [r for r in rows if is_gb550(r)]                      # 强制性工程建设规范
    sh = [r for r in rows if is_sh_local(r)]                     # 上海工程建设规范
    rec = [r for r in rows if not is_gb550(r) and not is_sh_local(r)]   # 其余
    gb = [r for r in rec if r["编号"].startswith("GB")]           # 其他国家标准
    jg = [r for r in rec if r["编号"].startswith("JGJ")]          # 行业标准

    cats = OrderedDict()
    for r in mand:
        cats.setdefault(r["分类"], []).append(r)

    out = []
    w = out.append

    w("# " + TITLE)
    w("")
    w("> 本仓库**只收录标准的元数据与官方查阅链接，不包含任何标准正文内容**。")
    w("> 所有标准文本请通过下方官方渠道获取。")
    w("")
    w("> **配套仓库**：[Shanghai-Gov-Docs-Index](https://github.com/zhiyao87/Shanghai-Gov-Docs-Index)")
    w("> —— 上海建设工程**政府发文与规章**索引（政府规章、规范性文件、区级发文）。")
    w("> 本库管「技术标准」，那个库管「政府发文」，两者互补。")
    w("> 政府文件依《著作权法》第 5 条第（一）项不受著作权法保护，**那个库可以收录正文全文**。")
    w("")
    w("---")
    w("")
    w("## 合规声明")
    w("")
    w("本仓库的定位是**索引**，不是**文库**。这一区分是刻意的，也是本仓库能够公开存在的前提。")
    w("")
    w("### 为什么不能上传标准正文")
    w("")
    w("| 标准类型 | 编号形式 | 版权状态 | 法律依据 |")
    w("|---|---|---|---|")
    w("| 强制性国家标准 | **GB** + 数字 | 不受著作权法保护 | 《著作权法》第 5 条第（一）项：具立法、行政、司法性质的文件不适用本法 |")
    w("| 推荐性国家标准 | **GB/T** | **受著作权法保护** | 1999 年最高人民法院答复北京高院；国家版权局版权管理司意见 |")
    w("| 行业标准 | **JGJ**、CJJ 等 | **受著作权法保护** | 《标准化法》第 2 条明定「行业标准、地方标准是推荐性标准」 |")
    w("| 地方标准 | **DB**、DGJ 等 | **受著作权法保护** | 同上 |")
    w("| 标准图集 | 15G909、12J003 等 | **受著作权法保护** | 归中国建筑标准设计研究院等编制单位 |")
    w("")
    w("### 一个极易误判的点：强制性条文 ≠ 强制性标准")
    w("")
    w("住建部发布公告时，对含强制性条文的标准都会写「第 X.Y.Z 条为强制性条文，必须严格执行」。")
    w("**这句话只说明该标准含强制性条文，不说明该标准整体是强制性标准。**")
    w("")
    w("JGJ 行业标准普遍含强制性条文（如 JGJ 100-2015 的第 3.1.7、4.2.8 条），")
    w("但 2018 年施行的新《标准化法》**取消了强制性行业标准和强制性地方标准，")
    w("只保留强制性国家标准一级**，行业标准、地方标准一律为推荐性标准。")
    w("")
    w("> 所以本仓库「属性」列的判定依据是**标准编号**，不是公告措辞：")
    w("> `GB` → 强制性；`GB/T`、`JGJ`、`JGJ/T`、`DB`、`DGJ` → 推荐性。")
    w("")
    w("强制性标准虽不受著作权法保护，但出版单位依《标准出版管理办法》享有**专有出版权**，")
    w("实务上再分发他人出版的标准文本仍可能被主张权利 —— 这是本仓库坚持只做索引的现实理由。")
    w("")
    w("推荐性国家标准的著作权人为国家标准化管理委员会，**中国质量标准出版传媒有限公司**")
    w("（原中国标准出版社）享有专有出版权与信息网络传播权，是实际维权主体。")
    w("")
    w("**关键分界点**：公开仓库 = 向不特定公众提供作品，直接落入《著作权法》第 10 条第（十二）项")
    w("「信息网络传播权」的范畴。这与上传到任何公开分享平台性质相同。")
    w("")
    w("参考判例与执法数据：")
    w("")
    w("- (2021)京73民终437号，北京知识产权法院：质量标准传媒诉金盾出版社，判赔 5 万元并停止复制、发行。")
    w("- 2021 年，标准出版机构自律维权发展联盟对主流内容平台开展侵权监控，一次性通知删除侵权标准文档 14 万余项、封禁违规上传用户 50 余个。")
    w("- 河南省信阳市中级人民法院曾就销售侵权盗版标准作出刑事判决，被告人构成侵犯著作权罪。")
    w("")
    w("### 本仓库收录什么")
    w("")
    w("✅ 标准编号、名称、分类、属性、实施日期、现行/废止状态")
    w("")
    w("✅ 官方免费查阅渠道的链接")
    w("")
    w("✅ 个人使用笔记与项目经验记录（只写心得与结论，不摘录条文正文）")
    w("")
    w("### 本仓库不收录什么")
    w("")
    w("❌ 标准正文 PDF（任何格式、任何来源）")
    w("")
    w("❌ 标准图集扫描件")
    w("")
    w("❌ 付费出版物内容的再分发")
    w("")
    w("---")
    w("")
    w("## 数据概览")
    w("")
    w("| 项目 | 数量 |")
    w("|---|---|")
    w("| 收录标准总数 | %d |" % total)
    w("| 强制性工程建设规范（GB 55001—55038） | %d |" % len(mand))
    w("| 其他国家标准（GB 强制性 / GB/T 推荐性） | %d |" % len(gb))
    w("| 行业标准（JGJ，均为推荐性） | %d |" % len(jg))
    w("| 上海工程建设规范（DGJ08 / DG/TJ08，均为推荐性） | %d |" % len(sh))
    w("| **上海规范批准 / 发布通知**（另计，见第五节） | %d |" % len(notices))
    w("")
    w("按版权分层统计：")
    w("")
    w("| 分层 | 含义 | 数量 |")
    w("|---|---|---|")
    w("| A | 不受著作权法保护（强制性国家标准） | %d |" % len([r for r in rows if r["版权分层"].startswith("A")]))
    w("| B | 受著作权法保护（推荐性国家标准 GB/T） | %d |" % len([r for r in rows if r["版权分层"].startswith("B")]))
    w("| C | 受著作权法保护（行业标准 JGJ、上海工程建设规范） | %d |" % len([r for r in rows if r["版权分层"].startswith("C")]))
    w("")
    w("数据来源：住房和城乡建设部官网发布公告、上海市住房和城乡建设管理委员会「现行标准」栏目，")
    w("以及实际施工图设计说明中的现行规范引用表。详见文末「数据来源与核实方法」。")
    w("")
    w("> 本仓库不引用「国家标准全文公开系统」作为数据源 —— 该系统**不收录工程建设类标准**，")
    w("> 用它核对建筑国标会得到空结果。原因见第十节。")
    w("")
    w("---")
    w("")
    w("## 一、强制性工程建设规范")
    w("")
    w("自 2015 年《深化标准化工作改革方案》起，工程建设领域推行**全文强制性规范**体系，")
    w("逐步取代原先分散在各标准中的「强制性条文」。截至 2025 年 5 月，")
    w("已发布实施的强制性工程建设规范共 **%d 本**（GB 55001—GB 55038），**全部条文必须严格执行**。" % len(mand))
    w("")
    w("> 重要变化：GB 55038-2025《住宅项目规范》于 2025-05-01 实施，")
    w("> 同时废止《住宅建筑规范》GB 50368-2005 及 8 项标准的 55 条强制性条文。")
    w("> 引用住宅类标准时务必核对这一变更。")
    w("")

    for cat in CATEGORY_ORDER:
        items = cats.get(cat)
        if not items:
            continue
        items_sorted = sorted(items, key=lambda r: r["编号"])
        w("### %s（%d）" % (cat, len(items_sorted)))
        w("")
        w("| 编号 | 名称 | 实施日期 | 官方链接 | 备注 |")
        w("|---|---|---|---|---|")
        for r in items_sorted:
            w("| %s | %s | %s | %s | %s |" % (
                r["编号"], r["名称"], cell(r["实施日期"]), link_md(r["官方链接"]), cell(r["备注"])))
        w("")

    w("> 强制规范的官方电子版由住房城乡建设部官网随发布公告提供，可免费下载。")
    w("> 注意：国家标准全文公开系统**不收录**食品安全、环境保护、**工程建设**三类标准，")
    w("> 所以建筑类国标要走住建部官网，不要在该系统里找。")
    w("")
    w("---")
    w("")
    w("## 二、其他常用国家标准")
    w("")
    w("这一组里两类混排，看**属性**列区分：")
    w("")
    w("- **GB**（无 /T）＝ 强制性国家标准，含若干强制性条文，**该标准的著作权状态为「不受保护」**")
    w("- **GB/T** ＝ 推荐性国家标准，**受著作权法保护**")
    w("")
    w("| 编号 | 名称 | 分类 | 属性 | 实施日期 | 官方链接 | 备注 |")
    w("|---|---|---|---|---|---|---|")
    for r in sorted(gb, key=lambda x: x["编号"]):
        w("| %s | %s | %s | %s | %s | %s | %s |" % (
            r["编号"], r["名称"], r["分类"], cell(r["属性"]), cell(r["实施日期"]),
            link_md(r["官方链接"], "住建部公告"), cell(r["备注"])))
    w("")
    w("---")
    w("")
    w("## 三、常用行业标准")
    w("")
    w("均为 JGJ 行业标准。**注意：行业标准一律是推荐性标准，受著作权法保护** ——")
    w("即便标准正文里印着「强制性条文」，也不改变其推荐性标准的法律属性。详见上方合规声明。")
    w("")
    w("| 编号 | 名称 | 分类 | 实施日期 | 官方链接 |")
    w("|---|---|---|---|---|")
    for r in sorted(jg, key=lambda x: x["编号"]):
        w("| %s | %s | %s | %s | %s |" % (
            r["编号"], r["名称"], r["分类"], cell(r["实施日期"]),
            link_md(r["官方链接"], "住建部公告")))
    w("")
    w("---")
    w("")
    w("## 四、上海工程建设规范")
    w("")
    w("以 **DGJ08 / DG/TJ08** 编号，由**上海市住房和城乡建设管理委员会**发布。")
    w("共收录 **%d 条**，按用途分组。" % len(sh))
    w("")
    w("与国标的关系：上海工程建设规范补充本地要求，与国标**并行有效、不替代国标**；")
    w("两者的具体适用关系以各自总则条文为准。做上海项目时，国标与本市工程建设规范需一并核对。")
    w("")
    w("> ⚠️ **地方标准同样是推荐性标准、受著作权法保护**（《标准化法》第 2 条）。")
    w("> 上海市住建委在「现行标准」栏目里把它们一律标注为「推荐性标准」，")
    w("> 这与部分标准含「强制性条文」的事实并不矛盾 —— 与 JGJ 的情形相同。")
    w("")
    w("下表链接指向上海市住建委官网提供的**标准全文 PDF 直链**（官网自行公开）。")
    w("")
    for g in SH_GROUP_ORDER:
        items = [r for r in sh if r.get("分组") == g]
        if not items:
            continue
        w("### %s（%d）" % (g, len(items)))
        w("")
        w("| 编号 | 名称 | 实施日期 | 官方全文 |")
        w("|---|---|---|---|")
        for r in sorted(items, key=lambda x: x["编号"]):
            w("| %s | %s | %s | %s |" % (
                r["编号"], r["名称"], cell(r["实施日期"]), link_md(r["官方链接"], "PDF")))
        w("")
    w("---")
    w("")
    w("## 五、上海工程建设规范批准 / 发布通知")
    w("")
    w("每一本上海市工程建设规范，都不是凭空出现在「现行标准」栏目里的 —— ")
    w("它由市住建委发一纸「关于批准《XXX》为上海市工程建设规范的通知」才生效。")
    w("本节收录的就是这一纸通知，共 **%d 条**。" % len(notices))
    w("")
    w("**为什么单列一节**：官网「现行标准」栏目更新比批准动作慢半拍。")
    w("2026 年新批的那一批（《城市轨道交通地下车站与周边连通工程设计标准》、")
    w("《桥梁改扩建技术标准》、《钢结构 / 混凝土模块化建筑技术导则》等）在栏目里")
    w("至今查不到，只能从批准通知看到。想跟踪「最近批了什么」，看这一节；")
    w("想查「这本规范现在有效吗、全文在哪」，看第四节。")
    w("")
    n_hit = sum(1 for r in notices if r.get("编号"))
    w("| 项目 | 数量 |")
    w("|---|---|")
    w("| 通知总数 | %d |" % len(notices))
    w("| 已能对应上 DGJ08 / DG/TJ08 编号（附全文 PDF） | %d |" % n_hit)
    w("| 新批准、现行标准栏目尚未收录（暂无编号） | %d |" % (len(notices) - n_hit))
    w("")
    w("> 本表只登记**通知的出处**（发布页 / 红头 PDF / 附件原文），不收录标准正文。")
    w("> 规范全文是 DGJ08 / DG/TJ08 地方标准，依《标准化法》第 2 条属推荐性标准、")
    w("> **受著作权法保护** —— 有全文 PDF 直链的，链接指向市住建委官网自行公开的原件，")
    w("> 本仓库不镜像。批准通知本身属行政文件，不受著作权法保护。")
    w("")
    for g in NOTICE_GROUP_ORDER:
        items = [r for r in notices if r.get("分组") == g]
        if not items:
            continue
        w("### %s（%d）" % (g, len(items)))
        w("")
        w("| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |")
        w("|---|---|---|---|---|---|")
        for r in sorted(items, key=lambda x: (x.get("批准日期") or ""), reverse=True):
            full = r.get("全文PDF") or r.get("附件") or ""
            w("| %s | %s | %s | %s | %s | %s |" % (
                r["标准名"], cell(r.get("编号")), cell(r.get("批准日期")),
                cell(r.get("文号")),
                link_md(r.get("官方链接"), "发布页"),
                link_md(full, "PDF")))
        w("")
    w("---")
    w("")
    w("## 六、官方免费查阅渠道")
    w("")
    w("| 渠道 | 网址 | 覆盖范围 | 能否下载 |")
    w("|---|---|---|---|")
    w("| 国家标准全文公开系统 | https://openstd.samr.gov.cn/bzgk/gb/ | 国标（不含工程/食品/环保） | 2025-02 起开放 3 万余项在线阅读+下载 |")
    w("| 全国标准信息公共服务平台 | https://std.samr.gov.cn/ | 国标/行标/地标/团标题录 | 部分可在线读 |")
    w("| 住房和城乡建设部 | https://www.mohurd.gov.cn/ | **工程建设标准（含 38 本强规）** | ✅ 强规可免费下载 PDF |")
    w("| 国家工程建设标准化信息网 | https://www.ccsn.org.cn/ | 工程建设国标 + 行标 | 依标准而定 |")
    w("| 上海市住房和城乡建设管理委员会 | https://zjw.sh.gov.cn/xxbz/index.html | **上海工程建设规范（DGJ08 / DG/TJ08）** | ✅ 现行标准栏目提供全文 PDF 直链 |")
    w("| 上海市统一政策发布平台 | https://www.shanghai.gov.cn/zhengce/list | **市/区/街镇三级政府发文**（非标准） | ✅ 原文可下载 |")
    w("")
    w("> 提醒：官方提供免费下载 ≠ 你可以再分发。免费下载解决的是「获取」问题，")
    w("> 不解决「传播」问题。二者的法律边界在《著作权法》第 10 条。")
    w("")
    w("---")
    w("")
    w("## 七、目录结构")
    w("")
    w("仓库只跟踪**数据源 + 生成器 + 说明书**。由脚本产出的内容一律不入库，")
    w("克隆后跑一次 `build_index.py` 即可完整重建 —— 这样仓库里永远不会出现")
    w("「数据源改了、产物忘了重新生成」的不一致状态。")
    w("")
    w("```")
    w(REPO + "/")
    w("├── README.md                  本文件（脚本生成；入库，作仓库首页）")
    w("├── LICENSE                    双许可：脚本 MIT / 数据 CC BY 4.0")
    w("├── .gitattributes             换行符策略（仓库内统一 LF）")
    w("├── .gitignore                 生成产物排除规则")
    w("├── build_index.py             索引生成器（零第三方依赖）")
    w("├── build_sh_local.py          上海工程建设规范：提取 + 链接验证（零第三方依赖）")
    w("├── build_sh_notices.py        规范批准通知索引：从 gov_docs.csv 抽取 + 补编号（零第三方依赖）")
    w("├── check_links.py             官方链接巡检工具（零第三方依赖）")
    w("├── data/")
    w("│   ├── standards.csv          ★ 数据源一：国标 / 行标（手工维护）")
    w("│   ├── sh_std_raw.json        上海住建委官网原始抓取结果（489 条，只读缓存）")
    w("│   ├── sh_local.tsv           ★ 数据源二：上海工程建设规范（由脚本生成）")
    w("│   └── sh_notices.tsv         ★ 数据源三：规范批准 / 发布通知（由脚本生成）")
    w("└── 〔以下为生成产物，不入库，跑脚本即重建〕")
    w("    ├── data/standards_excel.csv   Excel 友好版（UTF-8 BOM）")
    w("    ├── data/sh_notices_excel.csv  批准通知 Excel 版（UTF-8 BOM，列结构不同于标准表）")
    w("    └── obsidian/")
    w("        ├── 标准索引.md             Obsidian 主索引页")
    w("        └── standards/              每条标准一个笔记（%d 个）" % total)
    w("```")
    w("")
    w("> README 本身也是脚本产物，但它被特意保留入库 —— GitHub 打开仓库即渲染它，")
    w("> 访客无需运行任何脚本就能看到完整索引表。")
    w("")
    w("---")
    w("")
    w("## 八、怎么用")
    w("")
    w("### 克隆本仓库")
    w("")
    w("```bash")
    w("git clone https://github.com/zhiyao87/" + REPO + ".git")
    w("cd " + REPO)
    w("```")
    w("")
    w("### 重建生成产物")
    w("")
    w("`obsidian/` 与 `data/standards_excel.csv` 不入库，克隆后跑一次生成器即可：")
    w("")
    w("```bash")
    w("python build_index.py     # 零依赖，标准库即可，约 1 秒跑完")
    w("```")
    w("")
    w("> 想建自己的副本？fork 本仓库，或本地 `git init` 后推到你自己的仓库。")
    w("> 记得把 `build_index.py` 顶部的 `TITLE` 与 `REPO` 两个常量改成你的仓库名，")
    w("> 否则下次生成 README 时标题和 clone 地址会被写回本仓库的值。")
    w("")
    w("### 日常维护")
    w("")
    w("三个数据源，各改各的，改完跑一次生成器即可：")
    w("")
    w("```bash")
    w("python build_sh_local.py --verify   # ① 上海现行规范：重新抓取 + 验证链接（可选）")
    w("python build_sh_notices.py --src <gov_docs.csv 路径>   # ② 批准通知：重新抽取（可选）")
    w("python build_index.py               # ③ 合并三个源，生成全部产物")
    w("```")
    w("")
    w("| 数据源 | 维护方式 |")
    w("|---|---|")
    w("| `data/standards.csv` | 国标 / 行标，手工编辑后跑 `build_index.py` |")
    w("| `data/sh_local.tsv` | 上海工程建设规范，由 `build_sh_local.py` 从官网生成，**不要手改** |")
    w("| `data/sh_notices.tsv` | 规范批准 / 发布通知，由 `build_sh_notices.py` 从 "
      "`gov_docs.csv`（配套仓库）生成，**不要手改** |")
    w("")
    w("三处产出（README 表格 / Obsidian 笔记 / Excel CSV）会自动保持同步。")
    w("")
    w("### 定期巡检链接")
    w("")
    w("政府网站改版频繁，链接会静默失效（返回 404 但没人发现）。")
    w("`check_links.py` 逐个访问并检查页面内容是否确实对应该标准：")
    w("")
    w("```bash")
    w("python check_links.py              # 巡检全部 143 条")
    w("python check_links.py --limit 10   # 快速自检")
    w("python check_links.py --strict     # 把「可疑」也视为失败，人工复核用")
    w("python check_links.py --json out.json")
    w("```")
    w("")
    w("退出码：**只有存在真正失效的链接才返回 1**，可直接接进 CI。")
    w("「可疑」（返回 200 但内容不匹配）默认不判失败 —— 本库有若干条目因原公告页已从住建部")
    w("CMS 移除而有意降级为栏目入口，属预期状态，不该让 CI 变红。要严查时加 `--strict`。")
    w("")
    w("```yaml")
    w("# .github/workflows/link-check.yml")
    w("on:")
    w("  schedule: [{cron: '0 1 * * 1'}]   # 每周一 09:00 (UTC+8)")
    w("  workflow_dispatch:")
    w("jobs:")
    w("  check:")
    w("    runs-on: ubuntu-latest")
    w("    steps:")
    w("      - uses: actions/checkout@v4")
    w("      - run: python check_links.py")
    w("```")
    w("")
    w("> 巡检判定口径：**仅返回 200 不算通过**，还要求页面标题或正文确实含该标准编号/名称。")
    w("> 那种「200 但跳到栏目首页」的链接对使用者没有价值，会被标为「可疑」单独列出。")
    w("")
    w("### 作为 Obsidian 笔记库")
    w("")
    w("先跑一次 `python build_index.py` 生成 `obsidian/`，再把该目录整体复制进 vault，即可获得：")
    w("")
    w("- 每条标准一个笔记，带 YAML frontmatter，可按标签 / 属性筛选")
    w("- `标准索引.md` 作为入口页")
    w("- 笔记里留有「个人笔记」区，可随手记录项目上的使用经验")
    w("")
    w("> 直接把 `obsidian/standards/` 拖进 vault 根目录也可以，笔记之间靠标签关联。")
    w("")
    w("---")
    w("")
    w("## 九、数据来源与核实方法")
    w("")
    w("| 字段 | 来源 | 核实方式 |")
    w("|---|---|---|")
    w("| 编号、名称（国标 / 行标） | 住建部发布公告 / 国标委公告 | 官方公告原文 |")
    w("| 编号、名称（上海） | 上海市住建委「现行标准」栏目 | 栏目内嵌数据，由 `build_sh_local.py` 解析 |")
    w("| 实施日期 | 发布公告 / 上海栏目 | 公告正文；同日批次发布的标准实施日期通常一致 |")
    w("| 现行/废止 | 最新公告的废止清单 | 新强规实施时会在公告中列明废止的标准与条文 |")
    w("| 官方链接 | 住建部官网发布页 / 上海市住建委官网 | 见下节；全部链接已逐条联网验证 |")
    w("| 批准 / 发布通知（上海） | 配套仓库 Shanghai-Gov-Docs-Index 的 `gov_docs.csv` | "
      "由 `build_sh_notices.py` 抽取；编号与全文 PDF 用 `sh_std_raw.json` 按名称回填 |")
    w("")
    w("**上海数据的抓取方式**：上海市住建委「现行标准」栏目（`zjw.sh.gov.cn/xxbz/`）")
    w("的列表由前端渲染，页面内嵌完整 JSON 数据（字段 `bh` 编号 / `mc` 名称 / `pz` 批准 /")
    w("`ss` 实施 / `url` 全文 PDF）。`build_sh_local.py` 直接解析该数据，")
    w("无需逐条翻页，也不会因页面改版而失效得太突然。原始抓取结果存于")
    w("`data/sh_std_raw.json`（489 条），从中挑选建筑设计常用条目生成 `data/sh_local.tsv`。")
    w("")
    w("> ⚠️ **该栏目名为「现行标准」，但实测混有新老版本**（例如《住宅设计标准》同时存在")
    w("> DGJ08-20-2019 的两条记录、《建筑抗震设计规程》DGJ08-9-2013 与其替代者")
    w("> DG/TJ08-9-2023 并存）。本库只收录**实施日期最新**的版本，")
    w("> 引用前请仍以官方公告为准。")
    w("")
    w("**批准通知的抽取方式**：`build_sh_notices.py` 从配套仓库的 `gov_docs.csv` 里")
    w("按标题模式挑出规范类发文（`批准《X》为上海市工程建设规范` / `发布《X导则》` /")
    w("`印发《X技术规定》`），再用 `sh_std_raw.json` 按名称回填编号与全文 PDF。")
    w("名称比对会先去掉标点与「上海市」前缀、再去掉尾部的「标准 / 规范 / 导则」，")
    w("因此《上海市住宅设计标准》与《住宅设计标准》能对上。")
    w("**约 42% 能对上编号** —— 对不上的多半是 2026 年新批准、栏目尚未更新的，")
    w("这正是第五节存在的意义。")
    w("")
    w("**已知待核实项**：GB 55033-2022《城市轨道交通工程项目规范》的实施日期在公开资料中未获确证，")
    w("表中留空。GB 55026/55027 的实施日期按住建部同期公告批次整理，正式的引用前请以官方公告为准。")
    w("")
    w("**一个重要提示**：工程建设标准体系处于持续重构期（全文强制性规范替代分散强条），")
    w("标准之间的废止/替代关系比标准本身更容易出错。用于正式设计文件前，")
    w("请在国家工程建设标准化信息网核对最新状态。")
    w("")
    w("---")
    w("")
    w("## 十、关于官方链接：一次真实的链接失效排查")
    w("")
    w("本仓库的官方链接全部指向住建部官网的**标准发布公告页**（公告页附标准全文 PDF）。")
    w("初次建库时曾指向「国家标准全文公开系统」，后经核查发现该系统**不收录工程建设类标准**：")
    w("")
    w("```")
    w("openstd 站内检索  GB 5749  →  count = 1   ✓ 收录（非工程建设类）")
    w("openstd 站内检索  GB 50352 →  count = 0   ✗ 不收录（工程建设类）")
    w("openstd 站内检索  GB 50016 →  count = 0   ✗ 不收录（工程建设类）")
    w("```")
    w("")
    w("> 住房和城乡建设部主管的工程建设标准，与市场监管总局主管的一般国家标准走的是两套体系。")
    w("> 全文公开系统的排除范围里明确包含工程建设类。")
    w("")
    w("### 住建部 CMS 改版后的 URL 规律")
    w("")
    w("住建部官网在 2024 年前后更换了内容管理系统，**文档 ID 不变、路径前缀全变**：")
    w("")
    w("```")
    w("旧（2024 年前，现全部 404）")
    w("  /gongkai/zhengce/zhengcefilelib/{YYYYMM}/{YYYYMMDD}_{文档ID}.html")
    w("")
    w("新（现行有效）")
    w("  /gongkai/zc/wjk/art/{YYYY}/art_17339_{文档ID}.html")
    w("```")
    w("")
    w("其中 `{YYYY}` 取旧路径前四位，栏目前缀固定为 `art_17339_`。")
    w("**知道文档 ID 就能拼出新链接** —— 文档 ID 在第三方转载页的「来源」一行里往往还留着旧格式 URL。")
    w("")
    w("### 两条容易搞错的事实")
    w("")
    w("**1. 部分标准在 2024 年局部修订时改了编号和名称**（强制性 GB → 推荐性 GB/T）：")
    w("")
    w("| 原编号 / 名称 | 现编号 / 名称 | 生效 | 依据 |")
    w("|---|---|---|---|")
    w("| GB 50011-2010《建筑抗震设计规范》 | **GB/T 50011-2010《建筑抗震设计标准》** | 2024-08-01 | 住建部公告 2024 年第 61 号 |")
    w("| GB 50010-2010《混凝土结构设计规范》 | **GB/T 50010-2010《混凝土结构设计标准》** | 2024-08-01 | 住建部公告 2024 年第 62 号 |")
    w("")
    w("**2. 本站不用「某某标准 2024 版」这类传言做数据源。**")
    w("排查过程中遇到网上流传的「GB 50974-2024《消防给水及消火栓系统技术规范》」，")
    w("经核对住建部官方公告**并无此标准**（GB 50974-2014 现行有效），未予采信。")
    w("")
    w("### 尚缺深链的条目")
    w("")
    w("有 8 条标准的原发布公告页在住建部现行 CMS 中检索不到（多为 2010 年前后发布、")
    w("公告未随改版迁移）。这些条目的链接降级为住建部文件库栏目入口，")
    w("并在「备注」列注明原因。**宁可给栏目入口，也不给一条点进去 404 的假链接。**")
    w("")
    w("---")
    w("")
    w("## 十一、配套仓库：上海建设工程政府发文索引")
    w("")
    w("技术标准之外，施工图设计还有一层依据是**政府发文**——规划管理技术规定、")
    w("施工图审查办法、抗震设防审查办法、消防设计审查验收办法、既有建筑装饰装修管理规定等。")
    w("这类文件不属于本仓库范围（本仓库只管标准），单独建了一个配套仓库：")
    w("")
    w("### [zhiyao87/Shanghai-Gov-Docs-Index](https://github.com/zhiyao87/Shanghai-Gov-Docs-Index)")
    w("")
    w("| 项目 | 情况 |")
    w("|---|---|")
    w("| 收录范围 | 上海市 **建筑、规划、工程建设** 领域的政府规章与行政规范性文件 |")
    w("| 数据源 | 市政府规章库 + 市住建委规范性文件 + 上海市统一政策发布平台（市/区/街镇三级）"
      "+ 国家法律法规数据库（上海市地方性法规） |")
    w("| 规模 | 2,600+ 条（含市/区/街镇三级 + 地方性法规），覆盖上海 16 个区 |")
    w("| 正文 | **收录全文**（有实质约束力的文件），另附官方链接；"
      "核心文件还附**红头文件 PDF / 附表附图**原件直链 |")
    w("| 时间跨度 | 1985 – 2026 |")
    w("| 主题速查 | 屋顶绿化 / 立体绿化、屋顶分布式光伏 / BIPV、建筑光伏 / 太阳能、"
      "绿色建筑 / 节能、海绵城市、既有建筑改造 —— 六大主题按正文全文检索归类 |")
    w("")
    w("### 两个仓库的版权处理为什么不一样")
    w("")
    w("| | 本仓库（标准） | 配套仓库（政府发文） |")
    w("|---|---|---|")
    w("| 文件性质 | 技术标准（推荐性为主） | 具有立法、行政性质的文件 |")
    w("| 著作权法适用 | **适用**，受保护 | **不适用**（第 5 条第（一）项） |")
    w("| 因此的处理 | 只存索引，不存正文 | **可全文收录** |")
    w("")
    w("同一套「只给链接 vs 给全文」的判断，差别不在保守程度，而在法律性质。")
    w("政府规章和行政规范性文件依《著作权法》第 5 条第（一）项被排除在保护范围之外，")
    w("收录正文不构成侵权；而 JGJ、DGJ08、GB/T 这类推荐性技术标准仍是受保护作品。")
    w("")
    w("> 与上海市住建委「规范性文件」栏目的区别：该栏目是**发布渠道**，")
    w("> 配套仓库是**按设计报建主题重组的索引**，并额外覆盖了区级、街镇级发文。")
    w("")
    w("### 两个仓库之间的数据流")
    w("")
    w("本节第五节那 %d 条批准 / 发布通知，正是从配套仓库的 `gov_docs.csv` 里" % len(notices))
    w("抽出来的 —— 由 `build_sh_notices.py` 按标题模式筛出规范类发文，")
    w("再用本仓库的 `sh_std_raw.json` 回填编号与全文 PDF。")
    w("两个仓库因此形成闭环：**配套仓库负责把文件抓全，本仓库负责把标准理顺**。")
    w("")
    w("所以想查某本规范的**批准文号或通知原件**，去配套仓库按标题搜；")
    w("想查它**是否有全文 PDF、编号是多少**，看本仓库第四节与第五节。")
    w("")
    w("---")
    w("")
    w("## 许可证")
    w("")
    w("- 本仓库的**元数据与索引内容**（标准编号、名称、链接等事实性信息）：CC BY 4.0")
    w("- **生成脚本** `build_index.py`：MIT")
    w("- **标准正文**：不在本仓库范围内，版权归各自权利人所有")
    w("")

    return "\n".join(out)


# ---------------------------------------------------------------- Obsidian

def build_obsidian_index(rows):
    out = []
    w = out.append
    w("---")
    w("标题: 建筑标准规范索引")
    w("类型: 索引页")
    w("更新: 由 build_index.py 自动生成")
    w("tags:")
    w("  - 标准/索引")
    w("---")
    w("")
    w("# 建筑标准规范索引")
    w("")
    w("> 本页由 `build_index.py` 自动生成，请勿手工编辑。修改请改 `data/standards.csv`。")
    w(">")
    w("> 本库**只存索引，不存标准正文**。正文请走官方渠道，原因见仓库 README 的合规声明。")
    w("")
    w("---")
    w("")
    w("## 强制性工程建设规范")
    w("")
    w("| 编号 | 名称 | 分类 | 实施日期 |")
    w("|---|---|---|---|")
    for r in sorted([x for x in rows if is_gb550(x)], key=lambda x: x["编号"]):
        w("| [[%s]] | %s | %s | %s |" % (safe_filename(r), r["名称"], r["分类"], cell(r["实施日期"])))
    w("")
    w("## 其他国家标准")
    w("")
    w("含强制性国家标准（GB）与推荐性国家标准（GB/T），看「属性」字段区分。")
    w("")
    w("| 编号 | 名称 | 分类 | 属性 | 实施日期 |")
    w("|---|---|---|---|---|")
    for r in sorted([x for x in rows if not is_gb550(x) and x["编号"].startswith("GB")],
                    key=lambda x: x["编号"]):
        w("| [[%s]] | %s | %s | %s | %s |" % (
            safe_filename(r), r["名称"], r["分类"], cell(r["属性"]), cell(r["实施日期"])))
    w("")
    w("## 行业标准")
    w("")
    w("均为推荐性标准，受著作权法保护。")
    w("")
    w("| 编号 | 名称 | 分类 | 实施日期 |")
    w("|---|---|---|---|")
    for r in sorted([x for x in rows if x["编号"].startswith("JGJ")], key=lambda x: x["编号"]):
        w("| [[%s]] | %s | %s | %s |" % (safe_filename(r), r["名称"], r["分类"], cell(r["实施日期"])))
    w("")
    w("## 上海工程建设规范")
    w("")
    w("上海市住建委发布的 DGJ08 / DG/TJ08 系列，同属推荐性标准、受著作权法保护。")
    w("官方全文 PDF 由市住建委「现行标准」栏目提供。")
    w("")
    for g in SH_GROUP_ORDER:
        items = [x for x in rows if is_sh_local(x) and x.get("分组") == g]
        if not items:
            continue
        w("### %s（%d）" % (g, len(items)))
        w("")
        w("| 编号 | 名称 | 分类 | 实施日期 |")
        w("|---|---|---|---|")
        for r in sorted(items, key=lambda x: x["编号"]):
            w("| [[%s]] | %s | %s | %s |" % (
                safe_filename(r), r["名称"], r["分类"], cell(r["实施日期"])))
        w("")
    w("---")
    w("")
    w("## 按属性筛选")
    w("")
    w("装了 Dataview 插件的话，下面这些查询会实时生效：")
    w("")
    w("````markdown")
    w("```dataview")
    w("TABLE 分类, 实施日期, 版权分层")
    w("FROM \"standards\"")
    w("WHERE 属性 = \"强制性\"")
    w("SORT 标准编号 ASC")
    w("```")
    w("")
    w("```dataview")
    w("TABLE 分类, 实施日期")
    w("FROM \"standards\"")
    w("WHERE 属性 = \"推荐性\"")
    w("SORT 实施日期 DESC")
    w("```")
    w("")
    w("```dataview")
    w("LIST")
    w("FROM \"standards\"")
    w("WHERE 分类 = \"建筑\"")
    w("```")
    w("````")
    w("")
    return "\n".join(out)


def build_std_note(row):
    tags = ["标准/" + row["分类"]]
    if is_mandatory(row):
        tags.append("标准/强制性")
    else:
        tags.append("标准/推荐性")
    ct = TAG_BY_COPYRIGHT.get(row.get("版权分层", ""))
    if ct:
        tags.append(ct)

    out = []
    w = out.append
    w("---")
    w("标准编号: %s" % row["编号"])
    w("名称: %s" % row["名称"])
    w("分类: %s" % row["分类"])
    w("属性: %s" % row["属性"])
    w("实施日期: %s" % cell(row["实施日期"], ""))
    w("状态: %s" % cell(row["状态"], "现行"))
    w("版权分层: %s" % cell(row["版权分层"]))
    w("tags:")
    for t in tags:
        w("  - %s" % t)
    w("---")
    w("")
    w("# %s %s" % (row["编号"], row["名称"]))
    w("")
    w("| 字段 | 值 |")
    w("|---|---|")
    w("| 标准编号 | %s |" % row["编号"])
    w("| 分类 | %s |" % row["分类"])
    w("| 属性 | %s |" % row["属性"])
    w("| 实施日期 | %s |" % cell(row["实施日期"]))
    w("| 状态 | %s |" % cell(row["状态"], "现行"))
    w("| 版权状态 | %s |" % cell(row["版权分层"]))
    w("")
    w("## 官方查阅")
    w("")
    if (row.get("官方链接") or "").strip():
        w("- [官方发布页](%s)" % row["官方链接"].strip())
    else:
        w("- （暂无链接）")
    w("")
    if (row.get("备注") or "").strip():
        w("## 关联与提示")
        w("")
        w("%s" % row["备注"].strip())
        w("")
    w("## 个人笔记")
    w("")
    w("> 在此记录本项目/图纸上的使用经验、易错点、审图意见。")
    w("")
    return "\n".join(out)


# ---------------------------------------------------------------- main

def main():
    fields, rows = load_rows()
    notices = load_sh_notices()

    if not rows:
        raise SystemExit("data/standards.csv 没有读到数据，请检查文件编码与表头")

    with open(README, "w", encoding="utf-8", newline="\n") as f:
        f.write(build_readme(rows, notices))

    os.makedirs(OBS_STD, exist_ok=True)
    with open(OBS_INDEX, "w", encoding="utf-8", newline="\n") as f:
        f.write(build_obsidian_index(rows))

    for r in rows:
        p = os.path.join(OBS_STD, safe_filename(r) + ".md")
        with open(p, "w", encoding="utf-8", newline="\n") as f:
            f.write(build_std_note(r))

    # lineterminator="\n"：显式输出 LF，与仓库换行符策略（.gitattributes）保持一致，
    # 避免 Windows 下 csv 模块默认写 CRLF 造成 Git 反复报换行符警告。
    # 编码仍用 utf-8-sig（带 BOM），Excel 双击打开不乱码。
    with open(EXCEL_CSV, "w", encoding="utf-8-sig", newline="") as f:
        # extrasaction="ignore"：上海数据源多带一个「分组」键（仅供 README 分节用），
        # 不写进 Excel 导出，以保持列结构与 standards.csv 一致。
        dw = csv.DictWriter(f, fieldnames=fields, lineterminator="\n",
                            extrasaction="ignore")
        dw.writeheader()
        dw.writerows(rows)

    # 批准通知单独导出一份 Excel —— 列结构与标准表不同（多文号、多链接），
    # 混进一张表会让两边都难用。
    with open(NOTICE_EXCEL_CSV, "w", encoding="utf-8-sig", newline="") as f:
        dw = csv.DictWriter(f, fieldnames=NOTICE_COLS, lineterminator="\n",
                            extrasaction="ignore")
        dw.writeheader()
        dw.writerows(notices)

    mand = sum(1 for r in rows if is_mandatory(r))
    sh = sum(1 for r in rows if is_sh_local(r))
    print("收录 %d 条（强制 %d / 推荐 %d；其中上海工程建设规范 %d）"
          % (len(rows), mand, len(rows) - mand, sh))
    print("另收录规范批准 / 发布通知 %d 条" % len(notices))
    print("生成：README.md")
    print("生成：obsidian/标准索引.md")
    print("生成：obsidian/standards/*.md  （%d 个）" % len(rows))
    print("生成：data/standards_excel.csv")


if __name__ == "__main__":
    main()
