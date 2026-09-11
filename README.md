# 建筑设计规范索引

> 本仓库**只收录标准的元数据与官方查阅链接，不包含任何标准正文内容**。
> 所有标准文本请通过下方官方渠道获取。

> **配套仓库**：[Shanghai-Gov-Docs-Index](https://github.com/zhiyao87/Shanghai-Gov-Docs-Index)
> —— 上海建设工程**政府发文与规章**索引（政府规章、规范性文件、区级发文）。
> 本库管「技术标准」，那个库管「政府发文」，两者互补。
> 政府文件依《著作权法》第 5 条第（一）项不受著作权法保护，**那个库可以收录正文全文**。

---

## 合规声明

本仓库的定位是**索引**，不是**文库**。这一区分是刻意的，也是本仓库能够公开存在的前提。

### 为什么不能上传标准正文

| 标准类型 | 编号形式 | 版权状态 | 法律依据 |
|---|---|---|---|
| 强制性国家标准 | **GB** + 数字 | 不受著作权法保护 | 《著作权法》第 5 条第（一）项：具立法、行政、司法性质的文件不适用本法 |
| 推荐性国家标准 | **GB/T** | **受著作权法保护** | 1999 年最高人民法院答复北京高院；国家版权局版权管理司意见 |
| 行业标准 | **JGJ**、CJJ 等 | **受著作权法保护** | 《标准化法》第 2 条明定「行业标准、地方标准是推荐性标准」 |
| 地方标准 | **DB**、DGJ 等 | **受著作权法保护** | 同上 |
| 标准图集 | 15G909、12J003 等 | **受著作权法保护** | 归中国建筑标准设计研究院等编制单位 |

### 一个极易误判的点：强制性条文 ≠ 强制性标准

住建部发布公告时，对含强制性条文的标准都会写「第 X.Y.Z 条为强制性条文，必须严格执行」。
**这句话只说明该标准含强制性条文，不说明该标准整体是强制性标准。**

JGJ 行业标准普遍含强制性条文（如 JGJ 100-2015 的第 3.1.7、4.2.8 条），
但 2018 年施行的新《标准化法》**取消了强制性行业标准和强制性地方标准，
只保留强制性国家标准一级**，行业标准、地方标准一律为推荐性标准。

> 所以本仓库「属性」列的判定依据是**标准编号**，不是公告措辞：
> `GB` → 强制性；`GB/T`、`JGJ`、`JGJ/T`、`DB`、`DGJ` → 推荐性。

强制性标准虽不受著作权法保护，但出版单位依《标准出版管理办法》享有**专有出版权**，
实务上再分发他人出版的标准文本仍可能被主张权利 —— 这是本仓库坚持只做索引的现实理由。

推荐性国家标准的著作权人为国家标准化管理委员会，**中国质量标准出版传媒有限公司**
（原中国标准出版社）享有专有出版权与信息网络传播权，是实际维权主体。

**关键分界点**：公开仓库 = 向不特定公众提供作品，直接落入《著作权法》第 10 条第（十二）项
「信息网络传播权」的范畴。这与上传到任何公开分享平台性质相同。

参考判例与执法数据：

- (2021)京73民终437号，北京知识产权法院：质量标准传媒诉金盾出版社，判赔 5 万元并停止复制、发行。
- 2021 年，标准出版机构自律维权发展联盟对主流内容平台开展侵权监控，一次性通知删除侵权标准文档 14 万余项、封禁违规上传用户 50 余个。
- 河南省信阳市中级人民法院曾就销售侵权盗版标准作出刑事判决，被告人构成侵犯著作权罪。

### 本仓库收录什么

✅ 标准编号、名称、分类、属性、实施日期、现行/废止状态

✅ 官方免费查阅渠道的链接

✅ 个人使用笔记与项目经验记录（只写心得与结论，不摘录条文正文）

### 本仓库不收录什么

❌ 标准正文 PDF（任何格式、任何来源）

❌ 标准图集扫描件

❌ 付费出版物内容的再分发

---

## 数据概览

| 项目 | 数量 |
|---|---|
| 收录标准总数 | 143 |
| 强制性工程建设规范（GB 55001—55038） | 38 |
| 其他国家标准（GB 强制性 / GB/T 推荐性） | 34 |
| 行业标准（JGJ，均为推荐性） | 11 |
| 上海工程建设规范（DGJ08 / DG/TJ08，均为推荐性） | 60 |
| **上海规范批准 / 发布通知**（另计，见第五节） | 369 |

按版权分层统计：

| 分层 | 含义 | 数量 |
|---|---|---|
| A | 不受著作权法保护（强制性国家标准） | 64 |
| B | 受著作权法保护（推荐性国家标准 GB/T） | 8 |
| C | 受著作权法保护（行业标准 JGJ、上海工程建设规范） | 71 |

数据来源：住房和城乡建设部官网发布公告、上海市住房和城乡建设管理委员会「现行标准」栏目，
以及实际施工图设计说明中的现行规范引用表。详见文末「数据来源与核实方法」。

> 本仓库不引用「国家标准全文公开系统」作为数据源 —— 该系统**不收录工程建设类标准**，
> 用它核对建筑国标会得到空结果。原因见第十节。

---

## 一、强制性工程建设规范

自 2015 年《深化标准化工作改革方案》起，工程建设领域推行**全文强制性规范**体系，
逐步取代原先分散在各标准中的「强制性条文」。截至 2025 年 5 月，
已发布实施的强制性工程建设规范共 **38 本**（GB 55001—GB 55038），**全部条文必须严格执行**。

> 重要变化：GB 55038-2025《住宅项目规范》于 2025-05-01 实施，
> 同时废止《住宅建筑规范》GB 50368-2005 及 8 项标准的 55 条强制性条文。
> 引用住宅类标准时务必核对这一变更。

### 结构（10）

| 编号 | 名称 | 实施日期 | 官方链接 | 备注 |
|---|---|---|---|---|
| GB 55001-2021 | 工程结构通用规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761192.html) | 废止 GB 50153-2008 等 8 项标准相关强条 |
| GB 55002-2021 | 建筑与市政工程抗震通用规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761174.html) | - |
| GB 55003-2021 | 建筑与市政地基基础通用规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761185.html) | - |
| GB 55004-2021 | 组合结构通用规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761186.html) | - |
| GB 55005-2021 | 木结构通用规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761187.html) | - |
| GB 55006-2021 | 钢结构通用规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761191.html) | - |
| GB 55007-2021 | 砌体结构通用规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761188.html) | - |
| GB 55008-2021 | 混凝土结构通用规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762454.html) | 废止 GB 50010-2010 等 36 项标准相关强条 |
| GB 55017-2021 | 工程勘察通用规范 | 2022-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762455.html) | - |
| GB 55018-2021 | 工程测量通用规范 | 2022-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762456.html) | - |

### 建筑（8）

| 编号 | 名称 | 实施日期 | 官方链接 | 备注 |
|---|---|---|---|---|
| GB 55015-2021 | 建筑节能与可再生能源利用通用规范 | 2022-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762460.html) | 设计说明中最常引用的节能强规 |
| GB 55016-2021 | 建筑环境通用规范 | 2022-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762459.html) | - |
| GB 55019-2021 | 建筑与市政工程无障碍通用规范 | 2022-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762461.html) | 与 GB 50763-2012 并行使用 |
| GB 55025-2022 | 宿舍、旅馆建筑项目规范 | 2022-10-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_765629.html) | - |
| GB 55030-2022 | 建筑与市政工程防水通用规范 | 2023-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_768499.html) | - |
| GB 55031-2022 | 民用建筑通用规范 | 2023-03-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_767703.html) | 建筑专业最核心的强规 |
| GB 55037-2022 | 建筑防火通用规范 | 2023-06-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_770016.html) | 与 GB 50016-2014(2018年版) 并行 |
| GB 55038-2025 | 住宅项目规范 | 2025-05-01 | [官方发布页](https://www.gov.cn/zhengce/zhengceku/202504/content_7016620.htm) | 住建部公告2025年第39号；废止 GB 50368-2005 及 8 项标准 55 条强条 |

### 设备与市政（12）

| 编号 | 名称 | 实施日期 | 官方链接 | 备注 |
|---|---|---|---|---|
| GB 55009-2021 | 燃气工程项目规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761173.html) | - |
| GB 55010-2021 | 供热工程项目规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761189.html) | - |
| GB 55011-2021 | 城市道路交通工程项目规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761190.html) | - |
| GB 55012-2021 | 生活垃圾处理处置工程项目规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761194.html) | - |
| GB 55013-2021 | 市容环卫工程项目规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761195.html) | - |
| GB 55014-2021 | 园林绿化工程项目规范 | 2022-01-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_761193.html) | - |
| GB 55020-2021 | 建筑给水排水与节水通用规范 | 2022-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762458.html) | - |
| GB 55024-2022 | 建筑电气与智能化通用规范 | 2022-10-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_765632.html) | - |
| GB 55026-2022 | 城市给水工程项目规范 | 2022-10-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_765626.html) | - |
| GB 55027-2022 | 城乡排水工程项目规范 | 2022-10-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_765619.html) | - |
| GB 55029-2022 | 安全防范工程通用规范 | 2022-10-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_765630.html) | - |
| GB 55036-2022 | 消防设施通用规范 | 2023-03-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_767704.html) | - |

### 施工与安全（3）

| 编号 | 名称 | 实施日期 | 官方链接 | 备注 |
|---|---|---|---|---|
| GB 55023-2022 | 施工脚手架通用规范 | 2022-10-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_765631.html) | - |
| GB 55032-2022 | 建筑与市政工程施工质量控制通用规范 | 2023-03-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_767714.html) | - |
| GB 55034-2022 | 建筑与市政施工现场安全卫生与职业健康通用规范 | 2023-06-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_768953.html) | - |

### 既有建筑（2）

| 编号 | 名称 | 实施日期 | 官方链接 | 备注 |
|---|---|---|---|---|
| GB 55021-2021 | 既有建筑鉴定与加固通用规范 | 2022-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762453.html) | - |
| GB 55022-2021 | 既有建筑维护与改造通用规范 | 2022-04-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2021/art_17339_762457.html) | - |

### 专项工程（3）

| 编号 | 名称 | 实施日期 | 官方链接 | 备注 |
|---|---|---|---|---|
| GB 55028-2022 | 特殊设施工程项目规范 | 2022-10-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_765617.html) | - |
| GB 55033-2022 | 城市轨道交通工程项目规范 | - | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2022/art_17339_767715.html) | 实施日期待核实 |
| GB 55035-2023 | 城乡历史文化保护利用项目规范 | 2023-12-01 | [官方发布页](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2023/art_17339_772515.html) | - |

> 强制规范的官方电子版由住房城乡建设部官网随发布公告提供，可免费下载。
> 注意：国家标准全文公开系统**不收录**食品安全、环境保护、**工程建设**三类标准，
> 所以建筑类国标要走住建部官网，不要在该系统里找。

---

## 二、其他常用国家标准

这一组里两类混排，看**属性**列区分：

- **GB**（无 /T）＝ 强制性国家标准，含若干强制性条文，**该标准的著作权状态为「不受保护」**
- **GB/T** ＝ 推荐性国家标准，**受著作权法保护**

| 编号 | 名称 | 分类 | 属性 | 实施日期 | 官方链接 | 备注 |
|---|---|---|---|---|---|---|
| GB 50009-2012 | 建筑结构荷载规范 | 结构 | 强制性 | 2012-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2012/art_17339_210754.html) | 相关强条已由 GB 55001-2021 废止 |
| GB 50015-2019 | 建筑给水排水设计标准 | 设备与市政 | 强制性 | 2020-03-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2019/art_17339_242990.html) | - |
| GB 50016-2014(2018年版) | 建筑设计防火规范 | 建筑 | 强制性 | 2015-05-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224333.html) | 部分条文因 GB 55037-2022 废止 |
| GB 50033-2013 | 建筑采光设计标准 | 建筑 | 强制性 | 2013-05-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224720.html) | 4.0.1 已被 GB 55038-2025 废止 |
| GB 50037-2013 | 建筑地面设计规范 | 建筑 | 强制性 | 2014-05-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224845.html) | - |
| GB 50038-2005 | 人民防空地下室设计规范 | 专项工程 | 强制性 | 2006-03-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/index.html) | 住建部现行 CMS 未检索到原发布公告页（2023 年有局部修订，官网未发布公告） |
| GB 50057-2010 | 建筑物防雷设计规范 | 设备与市政 | 强制性 | 2011-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2011/art_17339_202151.html) | - |
| GB 50067-2014 | 汽车库、修车库、停车场设计防火规范 | 建筑 | 强制性 | 2015-08-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224265.html) | - |
| GB 50084-2017 | 自动喷水灭火系统设计规范 | 设备与市政 | 强制性 | 2018-01-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2017/art_17339_233407.html) | - |
| GB 50096-2011 | 住宅设计规范 | 建筑 | 强制性 | 2012-08-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2011/art_17339_206878.html) | 55 条强条已被 GB 55038-2025 废止 |
| GB 50098-2009 | 人民防空工程设计防火规范 | 专项工程 | 强制性 | 2010-07-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/index.html) | 住建部现行 CMS 未检索到原发布公告页 |
| GB 50116-2013 | 火灾自动报警系统设计规范 | 设备与市政 | 强制性 | 2014-05-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224820.html) | - |
| GB 50118-2010 | 民用建筑隔声设计规范 | 建筑 | 强制性 | 2011-06-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/index.html) | 4.2.1/4.2.2/4.2.5 强制性条文已由 GB 55038-2025《住宅项目规范》废止；原发布公告页未检索到 |
| GB 50176-2016 | 民用建筑热工设计规范 | 建筑 | 强制性 | 2017-04-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2017/art_17339_230579.html) | - |
| GB 50189-2015 | 公共建筑节能设计标准 | 建筑 | 强制性 | 2015-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224011.html) | - |
| GB 50222-2017 | 建筑内部装修设计防火规范 | 建筑 | 强制性 | 2018-04-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2018/art_17339_236695.html) | - |
| GB 50325-2020 | 民用建筑工程室内环境污染控制标准 | 建筑 | 强制性 | 2020-08-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2020/art_17339_245708.html) | - |
| GB 50345-2012 | 屋面工程技术规范 | 建筑 | 强制性 | 2012-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2012/art_17339_210744.html) | - |
| GB 50352-2019 | 民用建筑设计统一标准 | 建筑 | 强制性 | 2019-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2019/art_17339_240715.html) | - |
| GB 50693-2011 | 坡屋面工程技术规范 | 建筑 | 强制性 | 2012-05-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2011/art_17339_207965.html) | - |
| GB 50736-2012 | 民用建筑供暖通风与空气调节设计规范 | 设备与市政 | 强制性 | 2012-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2012/art_17339_209265.html) | - |
| GB 50763-2012 | 无障碍设计规范 | 建筑 | 强制性 | 2012-09-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2012/art_17339_209758.html) | 与 GB 55019-2021 并行 |
| GB 50974-2014 | 消防给水及消火栓系统技术规范 | 设备与市政 | 强制性 | 2014-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/index.html) | 原发布公告页未检索到；全部强制性条文已由 GB 55036-2022《消防设施通用规范》废止 |
| GB 51251-2017 | 建筑防烟排烟系统技术标准 | 设备与市政 | 强制性 | 2018-08-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2019/art_17339_240707.html) | - |
| GB 51309-2018 | 消防应急照明和疏散指示系统技术标准 | 设备与市政 | 强制性 | 2019-03-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2019/art_17339_239607.html) | - |
| GB 51348-2019 | 民用建筑电气设计标准 | 设备与市政 | 强制性 | 2020-08-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2020/art_17339_247248.html) | - |
| GB/T 50001-2017 | 房屋建筑制图统一标准 | 制图 | 推荐性 | 2018-05-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2018/art_17339_234638.html) | - |
| GB/T 50010-2010 | 混凝土结构设计标准 | 结构 | 推荐性 | 2011-07-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2024/art_17339_778180.html) | 2024-08-01 局部修订：更名《混凝土结构设计标准》、改编号为 GB/T 50010-2010（住建部公告 2024 年第 62 号），原编号 GB 50010-2010；相关强条已由 GB 55008-2021 废止 |
| GB/T 50011-2010 | 建筑抗震设计标准 | 结构 | 推荐性 | 2010-12-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2024/art_17339_778179.html) | 2024-08-01 局部修订：更名《建筑抗震设计标准》、改编号为 GB/T 50011-2010（住建部公告 2024 年第 61 号），原编号 GB 50011-2010；相关强条已由 GB 55002-2021 废止 |
| GB/T 50034-2024 | 建筑照明设计标准 | 设备与市政 | 推荐性 | 2024-11-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2024/art_17339_777466.html) | 官方公告编号为 GB/T 50034-2024，原文写作 GB |
| GB/T 50103-2010 | 总图制图标准 | 制图 | 推荐性 | 2011-03-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/index.html) | 住建部现行 CMS 未检索到原发布公告页 |
| GB/T 50104-2010 | 建筑制图标准 | 制图 | 推荐性 | 2011-03-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/index.html) | 住建部现行 CMS 未检索到原发布公告页 |
| GB/T 50353-2013 | 建筑工程建筑面积计算规范 | 建筑 | 推荐性 | 2014-07-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224960.html) | 报建面积计算依据 |
| GB/T 50378-2019 | 绿色建筑评价标准 | 建筑 | 推荐性 | 2019-08-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2024/art_17339_240717.html) | - |

---

## 三、常用行业标准

均为 JGJ 行业标准。**注意：行业标准一律是推荐性标准，受著作权法保护** ——
即便标准正文里印着「强制性条文」，也不改变其推荐性标准的法律属性。详见上方合规声明。

| 编号 | 名称 | 分类 | 实施日期 | 官方链接 |
|---|---|---|---|---|
| JGJ 1-2014 | 装配式混凝土结构技术规程 | 结构 | 2014-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2020/art_17339_244041.html) |
| JGJ 100-2015 | 车库建筑设计规范 | 建筑 | 2015-12-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224048.html) |
| JGJ 102-2003 | 玻璃幕墙工程技术规范 | 建筑 | 2004-01-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2006/art_17339_155736.html) |
| JGJ 113-2015 | 建筑玻璃应用技术规程 | 建筑 | 2016-04-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_225292.html) |
| JGJ 214-2010 | 铝合金门窗工程技术规范 | 建筑 | 2011-03-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/index.html) |
| JGJ 230-2010 | 倒置式屋面工程技术规程 | 建筑 | 2011-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2011/art_17339_201983.html) |
| JGJ 3-2010 | 高层建筑混凝土结构技术规程 | 结构 | 2011-10-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/index.html) |
| JGJ 36-2016 | 宿舍建筑设计规范 | 建筑 | 2017-06-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2017/art_17339_231189.html) |
| JGJ 39-2016(2019年版) | 托儿所、幼儿园建筑设计规范 | 建筑 | 2016-11-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2016/art_17339_227480.html) |
| JGJ 48-2014 | 商店建筑设计规范 | 建筑 | 2015-03-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2015/art_17339_224190.html) |
| JGJ/T 67-2019 | 办公建筑设计标准 | 建筑 | 2020-06-01 | [住建部公告](https://www.mohurd.gov.cn/gongkai/zc/wjk/art/2024/art_17339_244786.html) |

---

## 四、上海工程建设规范

以 **DGJ08 / DG/TJ08** 编号，由**上海市住房和城乡建设管理委员会**发布。
共收录 **60 条**，按用途分组。

与国标的关系：上海工程建设规范补充本地要求，与国标**并行有效、不替代国标**；
两者的具体适用关系以各自总则条文为准。做上海项目时，国标与本市工程建设规范需一并核对。

> ⚠️ **地方标准同样是推荐性标准、受著作权法保护**（《标准化法》第 2 条）。
> 上海市住建委在「现行标准」栏目里把它们一律标注为「推荐性标准」，
> 这与部分标准含「强制性条文」的事实并不矛盾 —— 与 JGJ 的情形相同。

下表链接指向上海市住建委官网提供的**标准全文 PDF 直链**（官网自行公开）。

### 设计基础（14）

| 编号 | 名称 | 实施日期 | 官方全文 |
|---|---|---|---|
| DG/TJ08-2201-2016 | 建筑信息模型应用标准 | 2016-09-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2201%E5%BB%BA%E7%AD%91%E4%BF%A1%E6%81%AF%E6%A8%A1%E5%9E%8B%E5%BA%94%E7%94%A8%E6%A0%87%E5%87%86%20%281%2920161114141911.pdf) |
| DG/TJ08-2242-2017 | 民用建筑外窗应用技术规程 | 2017-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/6d/6d198277bb364e98957a475220a6a503/adc14207c18fc2f09e9e4e9d035fc6db.pdf) |
| DG/TJ08-2314-2020 | 建筑同层排水系统应用技术标准 | 2020-09-01 | [PDF](https://zjw.sh.gov.cn/cmsres/e7/e757656ee0764aeab2403dbb9e190ac4/8af604bfc3af1bd19f92f56452022fef.pdf) |
| DG/TJ08-2328-2020 | 建筑风环境气象参数标准 | 2021-01-01 | [PDF](https://zjw.sh.gov.cn/cmsres/e9/e9e4ff8001aa472488d5e686a15f666d/e175a4e064dd34daa97f7de67ef2081e.pdf) |
| DG/TJ08-56-2019 | 建筑幕墙工程技术标准 | 2020-04-01 | [PDF](https://zjw.sh.gov.cn/cmsres/b3/b3d6916257f842788fa66c58051ac236/4b19832227aeacf7362e0df617db3429.pdf) |
| DG/TJ08-7-2021 | 建筑工程交通设计及停车库（场）设置标准 | 2022-01-01 | [PDF](https://zjw.sh.gov.cn/cmsres/07/079dc87c4eaa4571b5dd3f71aa729d75/e13124893c83a8b098989d0602b7ec42.pdf) |
| DG/TJ08-88-2021 | 建筑防排烟系统设计标准 | 2021-09-01 | [PDF](https://zjw.sh.gov.cn/cmsres/c5/c560c9556c8f4fa499b5e4d3a60fafbc/011ab52ef7c9d5a9c63fc8eb6a160954.pdf) |
| DG/TJ08-9-2023 | 建筑抗震设计标准 | 2023-06-01 | [PDF](https://zjw.sh.gov.cn/cmsres/00/007f14f3eb2341ffb407844dde0ce4b2/bda7bdd4527111d51b62a369226f9ef6.pdf) |
| DGJ08-107-2015 | 公共建筑节能设计标准 | 2016-05-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/107%E5%85%AC%E5%85%B1%E5%BB%BA%E7%AD%91%E8%8A%82%E8%83%BD%E8%AE%BE%E8%AE%A1%E6%A0%87%E5%87%8620160504104711.pdf) |
| DGJ08-11-2018 | 地基基础设计标准 | 2019-08-01 | [PDF](https://zjw.sh.gov.cn/cmsres/61/61ce445b195840b6aecf936275a1dd4d/725ffd47336d7a09823f78f641ada513.pdf) |
| DGJ08-20-2019 | 住宅设计标准 | 2022-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/0a/0a2db6d53a7f419ead2ad76584ada1fc/3884665e2cbca772db93c30985f3773f.pdf) |
| DGJ08-205-2015 | 居住建筑节能设计标准 | 2016-05-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/205%E5%B1%85%E4%BD%8F%E5%BB%BA%E7%AD%91%E8%8A%82%E8%83%BD%E8%AE%BE%E8%AE%A1%E6%A0%87%E5%87%8620160504104950.pdf) |
| DGJ08-2139-2021 | 住宅建筑绿色设计标准 | 2021-06-01 | [PDF](https://zjw.sh.gov.cn/cmsres/f3/f393b7748b084324aa98ec37a68c423d/12894cd15fc07589507a6b6450115fb8.pdf) |
| DGJ08-2143-2021 | 公共建筑绿色设计标准 | 2021-06-01 | [PDF](https://zjw.sh.gov.cn/cmsres/fd/fd2c40e843e1417f8cad4134754dcd7e/e5abd7ff3043946324c0ce84654a6dc1.pdf) |

### 住宅与住区（12）

| 编号 | 名称 | 实施日期 | 官方全文 |
|---|---|---|---|
| DG/TJ08-12-2004 | 普通中小学校建设标准 | 2004-08-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/90%E6%99%AE%E9%80%9A%E4%B8%AD%E5%B0%8F%E5%AD%A6%E6%A0%A1%E5%BB%BA%E8%AE%BE%E6%A0%87%E5%87%86.pdf) |
| DG/TJ08-2029-2021 | 多高层钢结构住宅技术标准 | 2021-11-01 | [PDF](https://zjw.sh.gov.cn/cmsres/f6/f640dd264cae40b3a0ef2dcf0b09d2da/aef768257b850cd075073ca76fa53729.pdf) |
| DG/TJ08-2178-2021 | 全装修住宅室内装修设计标准 | 2021-09-01 | [PDF](https://zjw.sh.gov.cn/cmsres/dc/dcc9ba7ed16b4982837fb054b4e1c731/554b47c0aad67ad1687d9fdd9bab7114.pdf) |
| DG/TJ08-2243-2017 | 市属高校建筑规划面积标准 | 2017-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/9d/9d9ff1add895470aaa35cb32e6572544/905b9ecf0d7f31426dedc87d3908a19d.pdf) |
| DG/TJ08-2247-2017 | 绿色养老建筑评价标准 | 2018-04-01 | [PDF](https://zjw.sh.gov.cn/cmsres/46/46d23c2ec812473ba9bcaa9b5083adc6/99c0f3ab316e17a1e0eea39cf76741cb.pdf) |
| DG/TJ08-2291-2019 | 保障性住房设计标准 | 2022-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/a1/a111fc7db226432ab42b496e9c1d4cca/3ef876c06ca695b7a4e389de3b5dc37d.pdf) |
| DG/TJ08-2291B-2022 | 保障性住房设计标准（保障性租赁住房新建分册） | 2022-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/66/6607c6540a4341c8abac739c61614d45/5fdbcdcfad61d017184148ec4788f83d.pdf) |
| DG/TJ08-2291C-2022 | 保障性住房设计标准（保障性租赁住房改建分册） | 2022-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/ed/edc21b3ab20445b3b90cb1920f6e8e02/f92a6c8516ba3cf5ac4bb499b00fe3e1.pdf) |
| DG/TJ08-2374-2022 | 既有住宅小区宜居改造技术标准 | 2022-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/1e/1e0e8af6338a480c9ee6c2d2a47a6fb9/739b080dab1795ee362482b3744655e5.pdf) |
| DG/TJ08-2381-2021 | 既有多层住宅加装电梯技术标准 | 2021-11-01 | [PDF](https://zjw.sh.gov.cn/cmsres/dc/dce996d5e6a34c80b7a6cf8794e32c59/823588f97918eb943e5e7bd4006e25ef.pdf) |
| DG/TJ08-45-2005 | 普通幼儿园建设标准 | 2005-08-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/112%E6%99%AE%E9%80%9A%E5%B9%BC%E5%84%BF%E5%9B%AD%E5%BB%BA%E8%AE%BE%E6%A0%87%E5%87%86.pdf) |
| DG/TJ08-82-2020 | 养老设施建筑设计标准 | 2020-09-01 | [PDF](https://zjw.sh.gov.cn/cmsres/2d/2df36620720842649f6fc2ea6c8363a4/a3426086ca29845f2aec787038ddbf7c.pdf) |

### 消防与安全（10）

| 编号 | 名称 | 实施日期 | 官方全文 |
|---|---|---|---|
| DG/TJ08-2177-2015 | 建筑工程消防施工质量验收规范 | 2015-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/d8/d885dcb869ac44a096e5949560837bf8/cfe684998aa924467eb4a38ebef934f9.pdf) |
| DG/TJ08-2188-2015 | 应急避难场所设计规范 | 2016-05-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2188%E5%BA%94%E6%80%A5%E9%81%BF%E9%9A%BE%E5%9C%BA%E6%89%80%E8%AE%BE%E8%AE%A1%E8%A7%84%E8%8C%8320160620145016.pdf) |
| DG/TJ08-2343-2020 | 大型物流建筑消防设计标准 | 2021-07-01 | [PDF](https://zjw.sh.gov.cn/cmsres/c0/c027665a23a24cf3a2ca4700b97c4062/95a6e6af71d970d4a218d96e2cb0771b.pdf) |
| DG/TJ08-2408-2022 | 城市综合体消防技术标准 | 2023-02-01 | [PDF](https://zjw.sh.gov.cn/cmsres/a5/a5875f7a69e04e81b67105359f7326e6/23cbc0d0ccef9c194b4ecbe219f94b98.pdf) |
| DG/TJ08-2409-2022 | 老旧住宅小区消防改造技术标准 | 2023-01-01 | [PDF](https://zjw.sh.gov.cn/cmsres/a3/a33d0fd6ca9f48ea836ba10acd2f36f0/44a5c7afbe6fda4be3f3485d6d07e62d.pdf) |
| DG/TJ08-2410-2022 | 文物和优秀历史建筑消防技术标准 | 2023-02-01 | [PDF](https://zjw.sh.gov.cn/cmsres/77/7793080f3bbd4857ac900944a7089a25/62a7bbdff0dbff79e1215a742768782c.pdf) |
| DGJ08-2048-2016 | 民用建筑电气防火设计规程 | 2017-05-01 | [PDF](https://zjw.sh.gov.cn/cmsres/91/91f35df45e584410bff66e7bffae4126/ddafbe17da733aa3257436101c3a895d.pdf) |
| DGJ08-2164-2015 | 民用建筑外保温材料防火技术规程 | 2015-10-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/15%E6%B0%91%E7%94%A8%E5%BB%BA%E7%AD%91%E5%A4%96%E5%A4%96%E4%BF%9D%E6%B8%A9%E6%9D%90%E6%96%99%E9%98%B2%E7%81%AB%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B20151028141231.pdf) |
| DGJ08-2173-2016 | 展览建筑及布展设计防火规程 | 2016-06-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2173%E5%B1%95%E8%A7%88%E5%BB%BA%E7%AD%91%E5%8F%8A%E5%B8%83%E5%B1%95%E8%AE%BE%E8%AE%A1%E9%98%B2%E7%81%AB%E8%A7%84%E7%A8%8B20160620144800.pdf) |
| DGJ08-94-2007 | 民用建筑水灭火系统设计规程 | 2008-03-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/185%E6%B0%91%E7%94%A8%E5%BB%BA%E7%AD%91%E6%B0%B4%E7%81%AD%E7%81%AB%E7%B3%BB%E7%BB%9F%E8%AE%BE%E8%AE%A1%E8%A7%84%E7%A8%8B.pdf) |

### 改造与历史建筑（6）

| 编号 | 名称 | 实施日期 | 官方全文 |
|---|---|---|---|
| DG/TJ08-108-2014 | 优秀历史建筑保护修缮技术规程 | 2015-01-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/369%E4%BC%98%E7%A7%80%E5%8E%86%E5%8F%B2%E5%BB%BA%E7%AD%91%E4%BF%9D%E6%8A%A4%E4%BF%AE%E7%BC%AE%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B.pdf) |
| DG/TJ08-2136-2022 | 既有居住建筑节能改造技术标准 | 2022-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/9d/9d0121dd2c8f49c185007841cf728028/5c9c7bbb38857eca1825aefc3fc2d6ed.pdf) |
| DG/TJ08-2137-2022 | 既有公共建筑节能改造技术标准 | 2022-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/f9/f91e64892592436fa6967bf71697596a/f7d3dd2cc6748416e26f3db295774d13.pdf) |
| DG/TJ08-2235-2017 | 既有地下建筑改扩建技术规范 | 2017-10-01 | [PDF](https://zjw.sh.gov.cn/cmsres/33/33839bbdabcd464c98214ce74f93ec09/2881aa35f892192e2851967ba9bb25b9.pdf) |
| DG/TJ08-2338-2020 | 既有建筑绿色改造技术标准 | 2021-04-01 | [PDF](https://zjw.sh.gov.cn/cmsres/a9/a946d2b3a85d48e5a2d17bd7b2234a02/70ccda2ba34ccf56c7d32a5af0b9496f.pdf) |
| DG/TJ08-2403-2022 | 优秀历史建筑抗震鉴定与加固标准 | 2023-03-01 | [PDF](https://zjw.sh.gov.cn/cmsres/4f/4fb3ec5fc9024f47ae041e43f3fad1a8/238bd5734252270c052189327c18ec71.pdf) |

### 装配式与外围护（7）

| 编号 | 名称 | 实施日期 | 官方全文 |
|---|---|---|---|
| DG/TJ08-2071-2016 | 装配整体式混凝土居住建筑设计规程 | 2016-12-01 | [PDF](https://zjw.sh.gov.cn/cmsres/c7/c748dde00f604e60b924e9ca1015f1cc/8d59ee1f07557bfd53653a9d57b32fca.pdf) |
| DG/TJ08-2154-2014 | 装配整体式混凝土公共建筑设计规程 | 2015-03-01 | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/375%E8%A3%85%E9%85%8D%E6%95%B4%E4%BD%93%E5%BC%8F%E6%B7%B7%E5%87%9D%E5%9C%9F%E5%85%AC%E5%85%B1%E5%BB%BA%E7%AD%91%E8%AE%BE%E8%AE%A1%E8%A7%84%E7%A8%8B.pdf) |
| DG/TJ08-2158-2023 | 预制混凝土夹心保温外墙应用技术标准 | 2023-06-01 | [PDF](https://zjw.sh.gov.cn/cmsres/29/29e38d3f7bbf446e88d5275c8f2141da/289ddd9349c90bf3bfc07807fef1a96b.pdf) |
| DG/TJ08-2198-2019 | 装配式建筑评价标准 | 2020-04-01 | [PDF](https://zjw.sh.gov.cn/cmsres/0c/0c9a1892e8574f2ab134289b77a97b74/9bea1200559d4a1084a892d5de134576.pdf) |
| DG/TJ08-2365-2021 | 建筑浮筑楼板保温隔声系统应用技术标准 | 2021-11-01 | [PDF](https://zjw.sh.gov.cn/cmsres/0c/0cb1488e48df44d382e7788141c428a8/5e8c8e12f84c3f1ec354d02273ffac77.pdf) |
| DG/TJ08-2433A-2023 | 外墙保温一体化系统应用技术标准（预制混凝土反打保温外墙） | 2023-10-01 | [PDF](https://zjw.sh.gov.cn/cmsres/3f/3f4174510125472b80b2b9a38d78c7dc/14d171af33d6c13792e1931753d2f180.pdf) |
| DG/TJ08-2433B-2023 | 外墙保温一体化系统应用技术标准（现浇混凝土反打保温外墙） | 2023-10-01 | [PDF](https://zjw.sh.gov.cn/cmsres/29/2979c3dd6dea4e518260f7208af7782c/253268745570edcb956be53d40e71d7b.pdf) |

### 结构与抗震（7）

| 编号 | 名称 | 实施日期 | 官方全文 |
|---|---|---|---|
| DG/TJ08-19-2018 | 建筑索结构技术标准 | 2019-5-1 | [PDF](https://zjw.sh.gov.cn/cmsres/ca/ca2703fe7c1841f1913a1860b8fd9106/c0e3c4c0a1e862ca46a1aac1c6d78214.pdf) |
| DG/TJ08-2192-2016 | 工程木结构设计规范 | 2016-05-01 | [PDF](https://zjw.sh.gov.cn/cmsres/fd/fd3d5b5394eb4c53b981f8b14efb69bd/d0f15238da028a5edbfdd78099c30a11.pdf) |
| DG/TJ08-2326-2020 | 建筑消能减震及隔震技术标准 | 2021-01-01 | [PDF](https://zjw.sh.gov.cn/cmsres/a5/a5fbac6a6968459c999bb10a0c41ec8c/72879c07b5b1f3b4a423ff2d04dc65fd.pdf) |
| DG/TJ08-2350-2021 | 大跨度建筑空间结构抗连续倒塌设计标准 | 2021-07-01 | [PDF](https://zjw.sh.gov.cn/cmsres/37/37ae0e21afef46b68a1ea1212a93f5e2/24d3a2a3507a7e499531e79cfab7b0c6.pdf) |
| DG/TJ08-52-2020 | 空间格构结构技术标准 | 2021-03-01 | [PDF](https://zjw.sh.gov.cn/cmsres/f0/f0ec9042c30e49ffbb7960f9b9390434/ad6c8918c81aad0f59bafb90f5e526bd.pdf) |
| DGJ08-69-2015 | 预应力混凝土结构设计规程 | 2016-06-01 | [PDF](https://zjw.sh.gov.cn/cmsres/89/8925525b534e4e63a43c9ab106d0ad8b/b4ae1e5348525166d0d3bf33e4c61d4b.pdf) |
| DGJ08-81-2021 | 现有建筑抗震鉴定与加固标准 | 2021-08-01 | [PDF](https://zjw.sh.gov.cn/cmsres/70/70c1a5c3608141f7b12e22dda36f702a/0eb4335ec853a054ba763ada4704072e.pdf) |

### 绿色建筑与专项（4）

| 编号 | 名称 | 实施日期 | 官方全文 |
|---|---|---|---|
| DG/TJ08-2040-2021 | 公共建筑绿色及节能工程智能化技术标准 | 2021-08-01 | [PDF](https://zjw.sh.gov.cn/cmsres/70/70ca03ac464c4de3bb12d5f4c1dddfac/5e3c2f581dbf5fd21c1461aa3ed87945.pdf) |
| DG/TJ08-2090-2020 | 绿色建筑评价标准 | 2020-07-01 | [PDF](https://zjw.sh.gov.cn/cmsres/9c/9c07f1b2aedd46d9a2b865cfe33c265d/8d7281ca46c8641107273e40fd4f2d1b.pdf) |
| DG/TJ08-2263-2018 | 城市轨道交通上盖建筑设计标准 | 2018-09-01 | [PDF](https://zjw.sh.gov.cn/cmsres/42/42232d71f65f4811adbea918cfcbffca/b2dfc8e9e9a21ec3bc13814b894a044e.pdf) |
| DG/TJ08-60-2017 | 机械式停车库（场）设计规程 | 2017-06-01 | [PDF](https://zjw.sh.gov.cn/cmsres/06/064a780a63994502902246e26b503c3d/8f0e7bbe4deec86f4be2170c443a8c68.pdf) |

---

## 五、上海工程建设规范批准 / 发布通知

每一本上海市工程建设规范，都不是凭空出现在「现行标准」栏目里的 —— 
它由市住建委发一纸「关于批准《XXX》为上海市工程建设规范的通知」才生效。
本节收录的就是这一纸通知，共 **369 条**。

**为什么单列一节**：官网「现行标准」栏目更新比批准动作慢半拍。
2026 年新批的那一批（《城市轨道交通地下车站与周边连通工程设计标准》、
《桥梁改扩建技术标准》、《钢结构 / 混凝土模块化建筑技术导则》等）在栏目里
至今查不到，只能从批准通知看到。想跟踪「最近批了什么」，看这一节；
想查「这本规范现在有效吗、全文在哪」，看第四节。

| 项目 | 数量 |
|---|---|
| 通知总数 | 369 |
| 已能对应上 DGJ08 / DG/TJ08 编号（附全文 PDF） | 155 |
| 新批准、现行标准栏目尚未收录（暂无编号） | 214 |

> 本表只登记**通知的出处**（发布页 / 红头 PDF / 附件原文），不收录标准正文。
> 规范全文是 DGJ08 / DG/TJ08 地方标准，依《标准化法》第 2 条属推荐性标准、
> **受著作权法保护** —— 有全文 PDF 直链的，链接指向市住建委官网自行公开的原件，
> 本仓库不镜像。批准通知本身属行政文件，不受著作权法保护。

<details>
<summary><strong>各专业方向明细（共 369 条 · 点击展开）</strong></summary>

### 建筑与住区（31）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 建筑装饰装修工程施工标准 | DGJ08-2135-2013 | 2026-03-02 | 沪建标定〔2025〕637 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/d0339b1539ea42bda4f488d94e2b73cc.html) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/347%E5%BB%BA%E7%AD%91%E8%A3%85%E9%A5%B0%E8%A3%85%E4%BF%AE%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E8%A7%84%E7%A8%8B.pdf) |
| 建筑地面工程施工标准 | DG/TJ08-2008-2006 | 2025-09-16 | 沪建标定〔2025〕459号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=35275cc33093483c9fcd0d21658ccd59&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/151%E5%BB%BA%E7%AD%91%E5%9C%B0%E9%9D%A2%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E8%A7%84%E7%A8%8B.pdf) |
| 上海市住宅建筑绿色设计施工图设计文件审查要点 | - | 2025-06-27 | 沪建建材〔2025〕315 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250627/e9d93793550e41acb320a7d9a52cabf4.html) | [PDF](https://zjw.sh.gov.cn/cmsres/5a/5ae547e5964b4a5c9d045bd1a4e66275/4060c833a776f669c61169987a7be8f9.pdf) |
| 上海市公共建筑绿色设计施工图设计文件审查要点 | - | 2025-06-27 | 沪建建材〔2025〕315 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250627/e9d93793550e41acb320a7d9a52cabf4.html) | [PDF](https://zjw.sh.gov.cn/cmsres/5a/5ae547e5964b4a5c9d045bd1a4e66275/4060c833a776f669c61169987a7be8f9.pdf) |
| 住宅工程套内质量验收标准 | DG/TJ08-2062-2017 | 2025-03-19 | 沪建标定〔2025〕164号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=2578304689ef4726ba88aae3ca4c5955&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/6f/6ff579ca284d4a1abfc688accd7a4e4f/a9cdfe0014419e9078022e0ae738be1a.pdf) |
| 建筑装饰工程石材应用技术标准 | DG/TJ08-2134-2013 | 2025-01-08 | 沪建标定〔2025〕11号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4c3ca37d672d47fab83442063f36bbfc&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/341%E5%BB%BA%E7%AD%91%E8%A3%85%E9%A5%B0%E5%B7%A5%E7%A8%8B%E7%9F%B3%E6%9D%90%E5%BA%94%E7%94%A8%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83.pdf) |
| 施工现场建筑工人从业管理标准 | - | 2024-06-11 | 沪建标定〔2024〕291号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=0814a2d004aa4656b7dd0954564e5222&siteId=0011) | - |
| 电动自行车集中充电和停放场所设计标准 | - | 2024-04-11 | 沪建标定〔2024〕179号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=1fa9488d11564c1ba872e46f4326f9cb&siteId=0011) | - |
| 建筑隔热涂料应用技术标准 | - | 2024-03-07 | 沪建标定〔2024〕114号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=9dabae95b52049939f83e3258102098c&siteId=0011) | - |
| 民用建筑外窗应用技术标准 | DG/TJ08-2242-2017 | 2023-12-29 | 沪建标定〔2023〕706号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e3cf26e367b149d3a728fefe80a3c332&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/6d/6d198277bb364e98957a475220a6a503/adc14207c18fc2f09e9e4e9d035fc6db.pdf) |
| 市域铁路设计标准 | - | 2023-06-01 | 沪建标定〔2023〕276号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=47f35af81d574ce883257b17e966c66f&siteId=0011) | - |
| 应急避难场所设计标准 | - | 2023-06-01 | 沪建标定〔2023〕277号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=93eee867d55242d6a18f341c33a8c29d&siteId=0011) | - |
| 保障性住房设计标准（保障性租赁住房改建分册） | DG/TJ08-2291C-2022 | 2022-09-06 | 沪建标定〔2022〕448号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4d5998d6d1a94f69a3d72669aa8866cb&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/ed/edc21b3ab20445b3b90cb1920f6e8e02/f92a6c8516ba3cf5ac4bb499b00fe3e1.pdf) |
| 公共租赁住房运行管理标准 | DG/TJ08-2368-2022 | 2022-08-08 | 沪建标定〔2022〕366号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=a1ed4b03d41e4bdebca161f52e52db3a&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/ea/eae0fa61d1634898bb28e14b06907211/c697794e2b6d18fa9b0f768516d1ce11.pdf) |
| 多层住宅平屋面改坡屋面工程技术标准 | - | 2022-01-28 | 沪建标定〔2022〕78号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=559a2baba51742b5bdf097b76014cf7d&siteId=0011) | - |
| 胶轮路轨系统设计标准 | - | 2022-01-05 | 沪建标定〔2022〕12号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b9d2656b55d04760bfe5e0fc254ee4fe&siteId=0011) | - |
| 建筑墙面涂料涂饰工程技术标准 | - | 2021-09-03 | 沪建标定〔2021〕559号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=88fc1cf6115246ccacc05cd28b6caf74&siteId=0011) | - |
| 建筑工程施工质量资料管理标准 | - | 2021-08-10 | 沪建标定〔2021〕518号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=7d22371f540f4244b992d4f4e58d99b6&siteId=0011) | - |
| 建筑工程装饰抹灰技术标准 | DG/TJ08-2357-2021 | 2021-06-28 | 沪建标定〔2021〕88 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/d58e31b6a0674ebd852987a7014f0252.html) | [PDF](https://zjw.sh.gov.cn/cmsres/12/12e601de11dd4d06b5a024c54dc46bcb/a2256a8cdf046f2e10f1afbae918057c.pdf) |
| 建筑起重机械安全检验与评估标准 | DG/TJ08-2080-2021 | 2021-06-28 | 沪建标定〔2021〕86 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/5d0c6a0b2e2c455fa82809bd187f942a.html) | [PDF](https://zjw.sh.gov.cn/cmsres/f4/f436c2c3c8104717bc2e45a30270247c/244b0dbeee97347ee3defa84aeb88a04.pdf) |
| 内河航道工程设计标准 | DG/TJ08-2116-2020 | 2021-06-28 | 沪建标定〔2021〕84 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/c949de7859c3460daf3137b75d0c629a.html) | [PDF](https://zjw.sh.gov.cn/cmsres/1f/1f0b1469e1d44cefa91c3f363148c11f/99f96ef0f117349899ebbb6f555d1db4.pdf) |
| 住宅建筑绿色设计标准 | DGJ08-2139-2021 | 2021-06-28 | 沪建标定〔2021〕63 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/071b9c361065447d94bfa1a824b0b749.html) | [PDF](https://zjw.sh.gov.cn/cmsres/f3/f393b7748b084324aa98ec37a68c423d/12894cd15fc07589507a6b6450115fb8.pdf) |
| 公共建筑绿色设计标准 | DGJ08-2143-2021 | 2021-06-28 | 沪建标定〔2021〕62 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/469d7bb981434dc18885f117116cb2b6.html) | [PDF](https://zjw.sh.gov.cn/cmsres/fd/fd2c40e843e1417f8cad4134754dcd7e/e5abd7ff3043946324c0ce84654a6dc1.pdf) |
| 上海市保障性住房（共有产权保障住房和征收安置房）施工图设计文件技术审查要点 | - | 2021-06-28 | 沪建质安〔2021〕8 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/75c23c78d2194fe5b3478d4a34fbdd22.html) | [PDF](https://zjw.sh.gov.cn/cmsres/d2/d286997293424e36a62517d994667f0d/4b687a67a7ba0226c43278a13c347aea.pdf) |
| 餐饮单位清洁设计技术标准 | DG/TJ08-110-2021 | 2021-05-31 | 沪建标定〔2021〕331号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=6558abe9ada94f838dd59e72b724c1ed&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/7a/7a0fd29a95514ec5a9e99be9fa0db634/6cdc53b6a210cd058e06e86c7079053b.pdf) |
| 全装修住宅室内装修设计标准 | DG/TJ08-2178-2021 | 2021-04-15 | 沪建标定〔2021〕229 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210415/dbd4ad07eaed42309f6b926f624f8da9.html) | [PDF](https://zjw.sh.gov.cn/cmsres/dc/dcc9ba7ed16b4982837fb054b4e1c731/554b47c0aad67ad1687d9fdd9bab7114.pdf) |
| 养老设施建筑设计标准 | DG/TJ08-82-2020 | 2020-06-15 | 沪建标定〔2020〕185 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200615/77d8926ca0e649899e92f2c49c7d6eb5.html) | [PDF](https://zjw.sh.gov.cn/cmsres/2d/2df36620720842649f6fc2ea6c8363a4/a3426086ca29845f2aec787038ddbf7c.pdf) |
| 住宅设计标准 | DGJ08-20-2019 | 2019-11-08 | 沪建标定〔2019〕615 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20191108/0011-71452.html) | [PDF](https://zjw.sh.gov.cn/cmsres/0a/0a2db6d53a7f419ead2ad76584ada1fc/3884665e2cbca772db93c30985f3773f.pdf) |
| 住宅建筑绿色设计标准 | DGJ08-2139-2021 | 2019-02-25 | 沪建标定〔2019〕67 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190225/0011-57965.html) | [PDF](https://zjw.sh.gov.cn/cmsres/f3/f393b7748b084324aa98ec37a68c423d/12894cd15fc07589507a6b6450115fb8.pdf) |
| 公共建筑绿色设计标准 | DGJ08-2143-2021 | 2019-02-25 | 沪建标定〔2019〕66 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190225/0011-57964.html) | [PDF](https://zjw.sh.gov.cn/cmsres/fd/fd2c40e843e1417f8cad4134754dcd7e/e5abd7ff3043946324c0ce84654a6dc1.pdf) |
| 上海市村民住房方案图集 | - | 2019-01-14 | 沪建村镇〔2018〕827 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56114.html) | - |

### 结构与抗震（45）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 桥梁结构监测系统技术标准 | DG/TJ08-2194-2016 | 2026-08-06 | 沪建标定〔2026〕283 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260806/7667667e741343a4b43684d9be964dac.html) | [PDF](https://zjw.sh.gov.cn/cmsres/67/674460c42d01429ca8c06b30cd1331f7/2b61c8f526e6c2510d9c5fecb2095e76.pdf) |
| 道路隧道结构健康监测技术标准 | - | 2026-08-06 | 沪建标定〔2026〕280 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260806/d214cc9661e5415d8e3b34d7f62ab616.html) | [PDF](https://zjw.sh.gov.cn/cmsres/b7/b74c448f7e1e4104b70476a1f9a48fba/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城市轨道交通结构监护测量标准 | DG/TJ08-2170-2015 | 2026-04-13 | 沪建标定〔2026〕139号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=219abd40fd70448bbb4fe12132235d07&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/%E5%9F%8E%E5%B8%82%E8%BD%A8%E9%81%93%E4%BA%A4%E9%80%9A%E7%BB%93%E6%9E%84%E7%9B%91%E6%8A%A4%E6%B5%8B%E9%87%8F%E8%A7%84%E8%8C%8320160217095330.pdf) |
| 基坑工程轴力主动调控式支撑技术标准 | - | 2026-03-02 | 沪建标定〔2026〕26 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/c92d7f53a9d747169fbb2b3efe560666.html) | [PDF](https://zjw.sh.gov.cn/cmsres/95/9572355d08b640e3a7eabfb6e313f1a6/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 高层建筑钢结构设计标准 | - | 2025-11-10 | 沪建标定〔2025〕562号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=9abd25d61f2d4a729aba30d897f34515&siteId=0011) | - |
| 箱式钢结构临时活动房 | - | 2025-10-11 | 沪建标定〔2025〕518号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=a78f014fede8482580507953f40327c5&siteId=0011) | - |
| 轻型钢结构制作及安装验收标准 | DG/TJ08-010-2018 | 2025-09-16 | 沪建标定〔2025〕460号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=039be4f84d6245ef87d6f3919532c483&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/be/bea1e7d6edb244adb8df133188768250/f092b7153d77e0a709d504196df88cda.pdf) |
| 城镇污水处理工程混凝土结构耐久性技术标准 | - | 2025-08-28 | 沪建标定〔2025〕426号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=5161d2a7dc5f4791922c0af7bd5b809c&siteId=0011) | - |
| 城市轨道交通上盖建筑结构设计标准 | - | 2025-08-20 | 沪建标定〔2025〕409号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=04c930331f7d40eeb151131e4d90b4e8&siteId=0011) | - |
| 人工砂在混凝土中的应用技术标准 | DG/TJ08-506-2017 | 2025-08-04 | 沪建标定〔2025〕388号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c06d3e4fe39047e2b139a30a469feaee&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/4e/4e36539b1ab742b7aca8382d1911be8d/e0a39e8a853e0f0510f860d15322c8e4.pdf) |
| 城市通信基础设施规划技术标准 | - | 2025-07-23 | 沪建标定〔2025〕375号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=6752b5f5fe2f49019aedf4151909a7b4&siteId=0011) | - |
| 干混砌筑砂浆抗压强度现场检测技术标准 | - | 2025-03-26 | 沪建标定〔2025〕95 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250326/1e61c7c68bf0498b8fb683670f7a94b6.html) | [PDF](https://zjw.sh.gov.cn/cmsres/67/671dc14aee784c1a9bb435eed33d6de4/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 智能驾驶道路基础框架数据标准 | - | 2025-03-19 | 沪建标定〔2025〕167号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=f29d124011de47849a0e25c9c5f9e363&siteId=0011) | - |
| 干混砌筑砂浆抗压强度现场检测技术标准 | - | 2025-02-18 | 沪建标定〔2025〕95号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=8e32e2be5f9548c68807af1ffc87ed5a&siteId=0011) | - |
| 道路桥梁和隧道结构安全保护技术标准 | - | 2024-07-02 | 沪建标定〔2024〕330号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=8acfca3d16474289b2cce148878342d0&siteId=0011) | - |
| 工程木结构设计标准 | - | 2024-06-11 | 沪建标定〔2024〕287号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=65d7f9a455894e10aba6d3087779d9b4&siteId=0011) | - |
| 缓粘结预应力混凝土结构技术标准 | - | 2024-02-06 | 沪建标定〔2024〕74号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=abe38a3ea8e442b7a0304dd237224c7d&siteId=0011) | - |
| 城市轨道交通结构安全保护技术标准 | - | 2023-09-26 | 沪建标定〔2023〕354 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20230926/abe40251eef6461da697e2cda054736a.html) | [PDF](https://zjw.sh.gov.cn/cmsres/24/24462de8becd4355b65d985b01d6d4af/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 桥梁抗震设计标准 | - | 2023-09-11 | 沪建标定〔2023〕476号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=6ad265233e474aac9d8fea431a1ac9f0&siteId=0011) | - |
| 户外招牌结构设计与安装 | - | 2023-06-01 | 沪建标定〔2023〕272号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=793f26531c6349f4aa6dbc347f8c2ff8&siteId=0011) | - |
| 成型钢筋混凝土结构设计标准 | - | 2023-05-09 | 沪建标定〔2023〕227号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=f493cb40ecb14a2abd7a0ea61ffe0539&siteId=0011) | - |
| 道路声屏障结构技术标准 | DG/TJ08-2086-2011 | 2023-01-31 | 沪建标定〔2023〕58号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c87581bf65fe45d2812601d54f2dfb20&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/266%E9%81%93%E8%B7%AF%E5%A3%B0%E5%B1%8F%E9%9A%9C%E7%BB%93%E6%9E%84%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83.pdf) |
| 粒化高炉矿渣粉在水泥混凝土中应用技术标准 | DG/TJ08-501-2023 | 2023-01-17 | 沪建标定〔2023〕25号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=9e5d34170cda4a6abf806f54a36d70e5&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/e6/e66a945e86d640fca4de8f12bda69734/b3ba90bf2cb18b85fabaafc1bbdb3e45.pdf) |
| 建筑抗震设计标准 | DG/TJ08-9-2023 | 2023-01-12 | 沪建标定〔2023〕17号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=cfba3332dba34d0c9b8723004d8470b9&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/00/007f14f3eb2341ffb407844dde0ce4b2/bda7bdd4527111d51b62a369226f9ef6.pdf) |
| 纤维增强复合材料筋混凝土结构技术标准 | - | 2022-08-03 | 沪建标定〔2022〕356号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=bccb8ffe4f9c4be5ae1317fd820936fd&siteId=0011) | - |
| 地下铁道结构抗震设计标准 | - | 2022-06-23 | 沪建标定〔2022〕272号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=9c0728b936df4895a4e0e447a9ffb29b&siteId=0011) | - |
| 桥梁工程超高性能混凝土应用技术标准 | DG/TJ08-2401-2022 | 2022-02-15 | 沪建标定〔2022〕103号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e3fcd64ae7e140f28d52f4a67d10efcd&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/c1/c1fdeee8b55a419c89987dd0cb829371/11e1dd4057b89f2a97806f6b4aab0bae.pdf) |
| 轻型木结构建筑技术标准 | DG/TJ08-2059-2009 | 2022-01-28 | 沪建标定〔2022〕79号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=225c6f599fed4356a30d288d8c9077e4&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/223%E8%BD%BB%E5%9E%8B%E6%9C%A8%E7%BB%93%E6%9E%84%E5%BB%BA%E7%AD%91%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83.pdf) |
| 市域铁路结构安全保护技术标准 | DG/TJ08 2397-2022 | 2022-01-17 | 沪建标定〔2022〕51号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=09435d0cb9104ced9482d40b330448d1&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/12/1251d091192a47ff99931f987ead3fe9/61c53d08636b08d09b04188c62d35743.pdf) |
| 电动汽车充电基础设施建设技术标准 | DG/TJ08-2093-2019 | 2021-12-24 | 沪建标定〔2021〕843号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c0fef928a00f4efc87dff57bfa2c3f74&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/5f/5f1dcdc5764146d5b050bd901116616d/7057caa8e26b1cd0a46795abbf39c36a.pdf) |
| 轨道交通及隧道工程混凝土结构耐久性设计施工技术标准 | DG/TJ08-2128-2021 | 2021-07-06 | 沪建标定〔2021〕352号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=61cbd40726d44d6ab444e077b095f75b&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/07/071599930c4b42b6b9cdb4f7dae638e8/374400a3820dc84e9174f63efe41384a.pdf) |
| 基坑工程微变形控制技术标准 | DG/TJ08-2364-2021 | 2021-07-06 | 沪建标定〔2021〕246 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210706/bcf66f09656e45699e38c7d497bf0df6.html) | [PDF](https://zjw.sh.gov.cn/cmsres/da/da27c996f8ea4ef98b787869dd608d9f/ff7e2b71e196731b8074a95bbe2910ed.pdf) |
| 人造山工程技术标准 | DG/TJ08-2358-2021 | 2021-07-06 | 沪建标定〔2021〕244 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210706/d9e4b0144b474f7caee9c50a9c799b81.html) | [PDF](https://zjw.sh.gov.cn/cmsres/65/6502195e0d86405ebc0b0c562bfb0bcc/afdcef4f6b9885152e0d0c57af8557b6.pdf) |
| 大跨度建筑空间结构抗连续倒塌设计标准 | DG/TJ08-2350-2021 | 2021-06-28 | 沪建标定〔2021〕11 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/fdf729bb5c2a44cf9f9fdee67ede1260.html) | [PDF](https://zjw.sh.gov.cn/cmsres/37/37ae0e21afef46b68a1ea1212a93f5e2/24d3a2a3507a7e499531e79cfab7b0c6.pdf) |
| 多高层钢结构住宅技术标准 | DG/TJ08-2029-2021 | 2021-05-31 | 沪建标定〔2021〕332号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e3387b05109c4fb581224542e0a0390b&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/f6/f640dd264cae40b3a0ef2dcf0b09d2da/aef768257b850cd075073ca76fa53729.pdf) |
| 混凝土模卡砌块建筑和结构构造 | - | 2020-06-15 | 沪建标定〔2020〕234 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200615/a47fe38a816c4f86b3a1075f81916409.html) | - |
| 预拌砂浆应用技术标准 | DG/TJ08-502-2020 | 2020-06-15 | 沪建标定〔2020〕208 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200615/bbfcb6ce30994474ab8e2099c8c706fc.html) | [PDF](https://zjw.sh.gov.cn/cmsres/85/852ddae118eb4d2785aa84a49b87bf82/81b7abe3117b0f2d542618b4ba78bf16.pdf) |
| 铝合金格构结构技术标准 | DG/TJ08-95-2020 | 2020-04-13 | 沪建标定〔2020〕136 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200413/694b37dcab1b43648205476db6df81d3.html) | [PDF](https://zjw.sh.gov.cn/cmsres/4e/4ec5c7f8a74b4622aa7260487582a497/f49ee5d97481096f495b29d2b03b0a5d.pdf) |
| 膜结构技术标准 | DG/TJ08-97-2019 | 2020-03-10 | 沪建标定〔2020〕39 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200310/aba5a22b38374ed18958822d93e12b29.html) | [PDF](https://zjw.sh.gov.cn/cmsres/65/652ddb28eda2461aa9c589abc9d73e3c/863a66c1fe95140a1e667fbce148b599.pdf) |
| 膜结构检测标准 | DG/TJ08-2019-2019 | 2020-03-10 | 沪建标定〔2020〕37 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200310/3d5be981d98c4416bf29443cdbcd0a7f.html) | [PDF](https://zjw.sh.gov.cn/cmsres/a2/a234d98a9afa4295abb9e86d5c4d8615/89e120360572a4c992f6681a8133791e.pdf) |
| 混凝土结构工程施工标准 | DG/TJ08-020-2019 | 2019-11-08 | 沪建标定〔2019〕沪建标定〔2019〕514号 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20191108/0011-71451.html) | [PDF](https://zjw.sh.gov.cn/cmsres/b5/b5a897b883e1449988be97fb14857148/840a94c337d4d432d3feb910ba311e1c.pdf) |
| 地基基础设计标准 | DGJ08-11-2018 | 2019-02-25 | 沪建标定〔2019〕69 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190225/0011-57967.html) | [PDF](https://zjw.sh.gov.cn/cmsres/61/61ce445b195840b6aecf936275a1dd4d/725ffd47336d7a09823f78f641ada513.pdf) |
| 建筑索结构技术标准 | DG/TJ08-019-2018 | 2019-01-14 | 沪建标定〔2018〕813 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56116.html) | [PDF](https://zjw.sh.gov.cn/cmsres/ca/ca2703fe7c1841f1913a1860b8fd9106/c0e3c4c0a1e862ca46a1aac1c6d78214.pdf) |
| 高强混凝土抗压强度无损检测技术标准 | DG/TJ08-507-2018 | 2019-01-14 | 沪建标定〔2018〕845 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56112.html) | [PDF](https://zjw.sh.gov.cn/cmsres/81/8191b46dc7bc40f998fe6ed2f484451c/f850475a782e1d8b59290c385e7a694d.pdf) |
| 高层建筑钢-混凝土混合结构设计规程 | DG/TJ08-015-2018 | 2019-01-14 | 沪建标定〔2018〕812 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56117.html) | [PDF](https://zjw.sh.gov.cn/cmsres/a9/a97fda7cb60541109b4ef056db4e50be/61b8587605f40133ff01bb23d9aecc08.pdf) |

### 消防与人防（18）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 地质灾害危险性评估技术标准 | DGJ08-2007-2016 | 2026-08-10 | 沪建标定〔2026〕343号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b9bd3426b3d24417b01d85c1fef2be11&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2007%E5%9C%B0%E8%B4%A8%E7%81%BE%E5%AE%B3%E5%8D%B1%E9%99%A9%E6%80%A7%E8%AF%84%E4%BC%B0%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B20160620144631.pdf) |
| 人防防护设备安装质量技术标准 | - | 2026-03-02 | 沪建标定〔2026〕6 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/76bbfe9bf8dd4214b9182d3dbdd48a50.html) | [PDF](https://zjw.sh.gov.cn/cmsres/a6/a6d556daaa024c21a1c270b8106f612d/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 人民防空工程安全风险评估技术标准 | - | 2025-03-05 | 沪建标定〔2025〕135号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=44d1af2c147444e8bb3d6c4d1dcab86a&siteId=0011) | - |
| 上海市智造空间防火设计导则 | - | 2025-01-17 | 沪建质安联〔2024〕639号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=2a5770dc8c144c29a1319989ea4cc8e2&siteId=0011) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/ca/cae1f79037474249bc7b418746308a77/8f2bdfcc52f12cd48b761d967ff5d1f7.pdf&filename=%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%99%BA%E9%80%A0%E7%A9%BA%E9%97%B4%E9%98%B2%E7%81%AB%E8%AE%BE%E8%AE%A1%E5%AF%BC%E5%88%99%E3%80%8B.pdf) |
| 建筑信息模型技术应用标准（人防工程） | - | 2024-09-26 | 沪建标定〔2024〕288 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20240926/bb2daab7734f4f7fa04ed4d708bc5b00.html) | [PDF](https://zjw.sh.gov.cn/cmsres/55/55abb2699c314ad6970974a185f7b8d5/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 民用建筑电气防火设计标准 | - | 2024-03-12 | 沪建标定〔2024〕128号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d32801339a41403092bac20176adc3af&siteId=0011) | - |
| 民防工程平战功能转换技术标准 | - | 2023-05-30 | 沪建标定〔2023〕266号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=bcaa60a7fb7f4e358bed7378795dc407&siteId=0011) | - |
| 大空间建筑铝合金结构防火技术标准 | - | 2023-05-22 | 沪建标定〔2023〕249号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c1085bc11adf41dbb5dea8f81f914c18&siteId=0011) | - |
| 民防工程运行维护技术标准 | - | 2023-02-13 | 沪建标定〔2023〕76号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=cea9a60e18ee4876b766d1b9afd315b5&siteId=0011) | - |
| 城市综合体消防技术标准 | DG/TJ08-2408-2022 | 2022-09-09 | 沪建标定〔2022〕453号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=cabb0803cfe6419ba91b126eeb08f746&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/a5/a5875f7a69e04e81b67105359f7326e6/23cbc0d0ccef9c194b4ecbe219f94b98.pdf) |
| 文物和优秀历史建筑消防技术标准 | DG/TJ08-2410-2022 | 2022-09-09 | 沪建标定〔2022〕451号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=114f319aff8d422091e49b9f32dfddc8&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/77/7793080f3bbd4857ac900944a7089a25/62a7bbdff0dbff79e1215a742768782c.pdf) |
| 老旧住宅小区消防改造技术标准 | DG/TJ08-2409-2022 | 2022-08-22 | 沪建标定〔2022〕414号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c1f16b08dd6c42db8871db40b3e5b731&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/a3/a33d0fd6ca9f48ea836ba10acd2f36f0/44a5c7afbe6fda4be3f3485d6d07e62d.pdf) |
| 道路隧道消防设施养护技术标准 | - | 2021-09-15 | 沪建标定〔2021〕585号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=6ceaecce1a7d4b51a24c843cc37f1925&siteId=0011) | - |
| 城市灾害损失评估技术标准 | DG/TJ 08-2383-2021 | 2021-09-06 | 沪建标定〔2021〕556号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=42e95ae454f44660904326f74d983fb5&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/34/346b3a0f11e64bb18b7a1c763f6318c3/3e49eae9dc9d823cd39faf446ac49da4.pdf) |
| 大型物流建筑消防设计标准 | DG/TJ08-2343-2020 | 2021-06-28 | 沪建标定〔2021〕66 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/404ff595a10a4f7597a7959812972c28.html) | [PDF](https://zjw.sh.gov.cn/cmsres/c0/c027665a23a24cf3a2ca4700b97c4062/95a6e6af71d970d4a218d96e2cb0771b.pdf) |
| 人民防空警报设施专用房图集 | - | 2021-06-28 | 沪建标定〔2021〕33 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/d7c7328d7e81416f87dbdbf71c715936.html) | [PDF](https://zjw.sh.gov.cn/cmsres/fa/fa9ac42c5f5d431db09dca05d16793b4/a33b57666b8f586124775637a0352c4c.pdf) |
| 建筑防排烟系统设计标准 | DG/TJ08-88-2021 | 2021-04-15 | 沪建标定〔2021〕228 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210415/ba5d1395a88a468b9db10788bdaff13c.html) | [PDF](https://zjw.sh.gov.cn/cmsres/c5/c560c9556c8f4fa499b5e4d3a60fafbc/011ab52ef7c9d5a9c63fc8eb6a160954.pdf) |
| 油浸式电力变压器火灾报警与灭火系统技术标准 | DG/TJ08-2022-2020 | 2020-06-15 | 沪建标定〔2020〕207 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200615/cb1fbb3d705d495497339cbb63b93923.html) | [PDF](https://zjw.sh.gov.cn/cmsres/4e/4eda6a79662a4fb384c6c2a20a0b4c73/45b44445a2cef99996006188609b1f8c.pdf) |

### 绿色建筑与节能（24）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 民用建筑可再生能源综合利用核算标准 | DG/TJ08-2329-2020 | 2026-04-13 | 沪建标定〔2026〕138号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ce853583a4a2456b9a8f12b261b282d5&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/02/025d43da7b76476d8f166e1cc7af49be/418d6536fcef9ed31242b3e70262b325.pdf) |
| 上海市建筑光储直柔系统技术导则 | - | 2026-03-02 | 沪建建材〔2026〕5 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/c22e3004ee934a35813c9b5c62bd05d2.html) | [PDF](https://zjw.sh.gov.cn/cmsres/6e/6ed262ebc52049709a0bfd723d127b60/b296bb576728fafce711ec7d8cae333c.docx) |
| 绿色建筑检测技术标准 | DG/TJ08-2199-2016 | 2026-03-02 | 沪建标定〔2026〕528 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/c7f9c0d48d7a488194841655305861b3.html) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2199%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E6%A3%80%E6%B5%8B%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%8620161206142208.pdf) |
| 绿色建筑检测技术标准 | DG/TJ08-2199-2016 | 2025-12-23 | 沪建标定〔2025〕528 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20251223/bd90238f327e43f9b94fd603f834f045.html) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2199%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E6%A3%80%E6%B5%8B%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%8620161206142208.pdf) |
| 既有建筑改造项目节能量核定标准 | - | 2025-11-07 | 沪建标定〔2025〕563号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=8fd47f0707bd48458f359687d08b1f09&siteId=0011) | - |
| 绿色建筑检测技术标准 | DG/TJ08-2199-2016 | 2025-10-17 | 沪建标定〔2025〕528号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=01b84919ca3d41ae8f12ba0a6810da62&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2199%E7%BB%BF%E8%89%B2%E5%BB%BA%E7%AD%91%E6%A3%80%E6%B5%8B%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%8620161206142208.pdf) |
| 上海市绿色建筑工程设计文件编制深度规定 | - | 2025-06-27 | 沪建建材〔2025〕315 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250627/e9d93793550e41acb320a7d9a52cabf4.html) | [PDF](https://zjw.sh.gov.cn/cmsres/5a/5ae547e5964b4a5c9d045bd1a4e66275/4060c833a776f669c61169987a7be8f9.pdf) |
| 超低能耗建筑设计标准（居住建筑） | - | 2025-06-03 | 沪建标定〔2025〕226 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250603/5dc0c184973f4b3cb4d8a13b2a7c216f.html) | [PDF](https://zjw.sh.gov.cn/cmsres/fb/fbf84998f0684c7785a04d54c94d4f71/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 超低能耗建筑设计标准（公共建筑） | - | 2025-04-23 | 沪建标定〔2025〕227号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=62a5033caf2349d1abb2f059a7807283&siteId=0011) | - |
| 太阳能热水系统应用图集 | - | 2024-05-21 | 沪建标定〔2024〕245号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=900d3fb4d7404ac6b91eb162e0bf0140&siteId=0011) | - |
| 公共建筑用能监测系统工程技术标准 | DGJ08-2068-2017 | 2024-02-02 | 沪建标定〔2024〕67号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=83da9a2540c9489385c97f6236764056&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/53/536a92f9c0154f0baedbaa52384d0e93/57410171a4b46db519a02557a68bc00d.pdf) |
| 办公建筑用能限额设计标准 | - | 2024-01-29 | 沪建标定〔2024〕51号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=dd374ec6e2d54b20bda501b76e6cc0ff&siteId=0011) | - |
| 绿色生态城区评价标准 | DG/TJ08-2253-2018 | 2024-01-16 | 沪建标定〔2024〕24号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b5800b8897c54cc29af18ace13acfba1&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/f7/f7b9e381512e4baa9fcf4fc582c08001/dc2de4ce6f131aee543ef1bc43908bca.pdf) |
| 绿色生态规划建设导则 | - | 2024-01-02 | 沪建建材联〔2023〕561号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c392f04e37334fecaa027efc119cfee8&siteId=0011) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/9e/9e960dc2a347471393c785c8c528f329/54d7d2b32369937d87c9afc7e3820f16.pdf&filename=%E5%A5%89%E8%B4%A4%E6%96%B0%E5%9F%8E%E7%BB%BF%E8%89%B2%E7%94%9F%E6%80%81%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E5%AF%BC%E5%88%99-%E5%AE%9A%E7%A8%BF.pdf) |
| 既有公共建筑节能改造技术标准 | DG/TJ08-2137-2022 | 2022-08-08 | 沪建标定〔2022〕369号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=db7e62f84df84535b2b72dea1aac9cfd&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/f9/f91e64892592436fa6967bf71697596a/f7d3dd2cc6748416e26f3db295774d13.pdf) |
| 既有居住建筑节能改造技术标准 | DG/TJ08-2136-2022 | 2022-08-08 | 沪建标定〔2022〕368号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ad7d236b63f24f44b304ffcd8f0154f6&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/9d/9d0121dd2c8f49c185007841cf728028/5c9c7bbb38857eca1825aefc3fc2d6ed.pdf) |
| 直膨式太阳能热泵热水系统应用技术标准 | DG/TJ08-2400-2022 | 2022-01-29 | 沪建标定〔2022〕87号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ae3a81a4ee784050b876105310fcfe8c&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/d6/d6e384def9ca4ea0b363d9fc2c4ab002/81c504f287dc2473c115cad69b83a5c4.pdf) |
| 绿色建材评价通用标准（第二册） | DG/TJ08-2352-2021 | 2021-07-06 | 沪建标定〔2021〕245 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210706/aa3d8ced291849b591819616affdfe31.html) | [PDF](https://zjw.sh.gov.cn/cmsres/57/5750f7243055414ba4830999730643cb/ca0573212a8567f33f336d50b90b9302.pdf) |
| 公共建筑绿色及节能工程智能化技术标准 | DG/TJ08-2040-2021 | 2021-06-28 | 沪建标定〔2021〕82 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/0b2a80b23cd9416e99251067455de03b.html) | [PDF](https://zjw.sh.gov.cn/cmsres/70/70ca03ac464c4de3bb12d5f4c1dddfac/5e3c2f581dbf5fd21c1461aa3ed87945.pdf) |
| 数据中心节能技术应用标准 | DG/TJ08-2347-2021 | 2021-06-28 | 沪建标定〔2021〕2 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/4fcc28b3f9e1425eb08ab357e052bffe.html) | [PDF](https://zjw.sh.gov.cn/cmsres/c1/c186dc6e5e66464481d7cdfc03d8537c/56c6aaf92f616672154fc1367e9ffc48.pdf) |
| 民用建筑可再生能源综合利用核算标准 | DG/TJ08-2329-2020 | 2020-10-29 | 沪建标定〔2020〕487 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20201029/51f8eec181b243ff8d575f6e41cf6e1c.html) | [PDF](https://zjw.sh.gov.cn/cmsres/02/025d43da7b76476d8f166e1cc7af49be/418d6536fcef9ed31242b3e70262b325.pdf) |
| 公共建筑能源审计标准 | DG/TJ08-2114-2020 | 2020-04-13 | 沪建标定〔2020〕142 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200413/de55603b632a41659dc157c54a886ff5.html) | [PDF](https://zjw.sh.gov.cn/cmsres/0a/0ad85125a98c44b39575c5d03dd964ab/7e2981cd395c2208f6b6c4b94c969251.pdf) |
| 太阳能与空气源热泵热水系统应用技术标准 | DG/TJ08-2316-2020 | 2020-04-13 | 沪建标定〔2020〕140 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200413/e94a819a2e484c72befd0ea24f18867d.html) | [PDF](https://zjw.sh.gov.cn/cmsres/e9/e90288094bf64f7190fa8eb2c9a7ab94/d028ea1a57640d9bc103d7e7a6ed6ea7.pdf) |
| 崇明世界级生态岛绿色生态城区规划建设导则 | - | 2019-11-08 | 沪建建材〔2019〕661  号 | [发布页](https://zjw.sh.gov.cn/csyx/20191108/0011-71448.html) | [PDF](https://zjw.sh.gov.cn/cmsres/2c/2ccae23f65734806a9e717069117dcc3/21da001734b0b197e60e5be34cbf2c24.pdf) |

### 装配式与外围护（27）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 装配式外挂墙板应用技术标准 | - | 2026-07-01 | 沪建标定〔2026〕294号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=8d4bff46a30d4de280e319f8332cc898&siteId=0011) | - |
| 上海市钢结构模块化建筑技术导则 | - | 2026-03-20 | 沪建建材〔2026〕99 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260320/a49ed43be8d04fdf84b47c09167ddbd0.html) | [PDF](https://zjw.sh.gov.cn/cmsres/0d/0d64a539ed114c45933bd889b13e2931/37d033ac302f59a84d8aaa83606a1abe.docx) |
| 上海市混凝土模块化建筑技术导则 | - | 2026-03-20 | 沪建建材〔2026〕99 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260320/a49ed43be8d04fdf84b47c09167ddbd0.html) | [PDF](https://zjw.sh.gov.cn/cmsres/0d/0d64a539ed114c45933bd889b13e2931/37d033ac302f59a84d8aaa83606a1abe.docx) |
| 上海市钢结构模块化建筑技术导则 | - | 2026-03-17 | 沪建建材〔2026〕99号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d8e6dcd374d74cefaac83c3b669980d9&siteId=0011) | [PDF](https://www.shanghai.gov.cn/cmsres/policy_resources/d8e6dcd374d74cefaac83c3b669980d9/3ab371c46e154d3ba03f2ae14b6df2a5/%E4%B8%8A%E6%B5%B7%E5%B8%82%E3%80%8A%E9%92%A2%E7%BB%93%E6%9E%84%E6%A8%A1%E5%9D%97%E5%8C%96%E5%BB%BA%E7%AD%91%E6%8A%80%E6%9C%AF%E5%AF%BC%E5%88%99%E3%80%8B%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89.docx) |
| 上海市混凝土模块化建筑技术导则 | - | 2026-03-17 | 沪建建材〔2026〕99号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d8e6dcd374d74cefaac83c3b669980d9&siteId=0011) | [PDF](https://www.shanghai.gov.cn/cmsres/policy_resources/d8e6dcd374d74cefaac83c3b669980d9/3ab371c46e154d3ba03f2ae14b6df2a5/%E4%B8%8A%E6%B5%B7%E5%B8%82%E3%80%8A%E9%92%A2%E7%BB%93%E6%9E%84%E6%A8%A1%E5%9D%97%E5%8C%96%E5%BB%BA%E7%AD%91%E6%8A%80%E6%9C%AF%E5%AF%BC%E5%88%99%E3%80%8B%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89.docx) |
| 预应力装配式混凝土框架结构技术标准 | - | 2026-03-02 | 沪建标定〔2026〕48 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/7561149ba4124b5d9774749ef48472f4.html) | [PDF](https://zjw.sh.gov.cn/cmsres/c5/c5debb925c564668aafc2d7d23fa3b81/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 装配式混凝土居住建筑设计标准 | - | 2025-12-12 | 沪建标定〔2025〕613号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=2bddab68d3ef4d8ea8eb37b9aab40950&siteId=0011) | - |
| 装配式混凝土预制构件设计--生产数据交互标准 | - | 2025-07-17 | 沪建标定〔2025〕365号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=8e374cb465944546ba3d69b9bf302d86&siteId=0011) | - |
| 地下工程预制装配技术标准（轨道交通工程） | - | 2024-09-26 | 沪建标定〔2024〕365 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20240926/2cffffe5cb4a427188557574050833bf.html) | [PDF](https://zjw.sh.gov.cn/cmsres/62/62c0c32a7298471e8542c7b78625f338/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 既有建筑幕墙检查及安全性鉴定技术标准 | - | 2024-07-22 | 沪建标定〔2024〕377号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e5d7f1165cc04242bbab204cb29b3de1&siteId=0011) | - |
| 装配式混凝土结构连接节点构造及构件图集 | - | 2024-06-11 | 沪建标定〔2024〕290号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=5ef0552898f94c838be87f60d08c267d&siteId=0011) | - |
| 外墙保温一体化系统应用技术标准（现浇混凝土保温外墙） | - | 2023-09-26 | 沪建标定〔2023〕345 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20230926/edd6fd31bfb1437fa729fbbea0043fb2.html) | [PDF](https://zjw.sh.gov.cn/cmsres/95/951a731e48804d70857098749be814aa/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 外墙外保温系统应用技术标准（岩棉） | - | 2023-07-31 | 沪建标定〔2023〕387号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b8f6583fc989423c8edd77703057fa32&siteId=0011) | - |
| 上海市既有建筑玻璃幕墙区级巡查工作导则 | - | 2023-07-31 | 沪建质安〔2023〕385号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=12e58e9dc3814e748be53b241c45ad12&siteId=0011) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/84/843c0cd3dad34ba0a1c70083765d8bb0/70ee00d9033881dcec57305311b3953f.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%97%A2%E6%9C%89%E5%BB%BA%E7%AD%91%E7%8E%BB%E7%92%83%E5%B9%95%E5%A2%99%E5%8C%BA%E7%BA%A7%E5%B7%A1%E6%9F%A5%E5%B7%A5%E4%BD%9C%E5%AF%BC%E5%88%99.pdf) |
| 外墙保温一体化系统应用技术标准（预制混凝土反打保温外墙） | DG/TJ08-2433A-2023 | 2023-07-11 | 沪建标定〔2023〕349号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=aed4debaa3b145128a72bb1f6941b8c6&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/3f/3f4174510125472b80b2b9a38d78c7dc/14d171af33d6c13792e1931753d2f180.pdf) |
| 外墙内保温系统应用技术标准（泡沫玻璃板） | - | 2023-06-01 | 沪建标定〔2023〕275号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c434b22277e54c198e9486c1d020c152&siteId=0011) | - |
| 装配式部分包覆钢-混凝土组合结构技术标准 | - | 2023-03-08 | 沪建标定〔2023〕118号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e33b9bffd06d4e409af7879fc7c7dab4&siteId=0011) | - |
| 装配式建筑工程设计文件编制深度标准 | - | 2022-01-29 | 沪建标定〔2022〕86号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d084d33bd0f34f7481ba0aef59c6ef97&siteId=0011) | - |
| 预制拼装桥梁结构标准设计图 | - | 2022-01-29 | 沪建标定〔2022〕85号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=099e98e1ceb4421f9ef06a515935cd8d&siteId=0011) | - |
| 预制装配式悬臂挡土墙技术标准 | DG/TJ08-2389-2021 | 2021-11-03 | 沪建标定〔2021〕696号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=32e8efbac0cd48938ca9585b64b9bccb&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/63/63a518e8a0a64cb68bae33dd0a6512ad/e3b63748933565bd45d2a714830a393e.pdf) |
| 预制拼装桥梁技术标准 | DG/TJ08-2160-2021 | 2021-09-15 | 沪建标定〔2021〕587号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=abafd1e3dc594ebcadaddc7ef0473c87&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/e4/e47f013d396e418a93926490490986e0/c370ffccb6f73f70d405611d16fbc7b9.pdf) |
| 建筑浮筑楼板保温隔声系统构造 | - | 2021-08-10 | 沪建标定〔2021〕512号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=22c4f8b87dd34c56a6b73f53c2cbc9b6&siteId=0011) | - |
| 装配整体式混凝土结构工程监理标准 | DG/TJ08-2360-2021 | 2021-07-06 | 沪建标定〔2021〕299 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210706/03c0db6097954d099b4e0132791ea38c.html) | [PDF](https://zjw.sh.gov.cn/cmsres/61/6122e3795f0e48f3a9aadd3446804174/db6823fbb85b6895a726585e8c719e1a.pdf) |
| 外墙保温系统及材料应用统一技术规定（暂行） | - | 2021-07-01 | 沪建建材〔2021〕113 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210701/661436f1be02428a9707580e8065f045.html) | [PDF](https://zjw.sh.gov.cn/cmsres/b0/b05ad55a273e40018f0c033a6b5dc9c1/b832225b04dfe0764367b0cb4794117a.pdf) |
| 保温装饰复合板墙体保温系统应用技术标准 | DG/TJ08-2122-2021 | 2021-05-31 | 沪建标定〔2021〕333号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=29cd2c013c8c425a8f495b75ca2af55c&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/57/5718f26de91c4890b12547eb2ee5da08/25228f97a5522c6f78474db5b3071c80.pdf) |
| 外墙保温系统及材料应用统一技术规定（暂行） | - | 2021-02-26 | 沪建建材〔2021〕113 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210226/fafadbf33561417da27658d830186d23.html) | [PDF](https://zjw.sh.gov.cn/cmsres/e5/e58335203f0e474ca9999efc932bb3fc/216c42e21a872dca2857d6beeecd4064.docx) |
| 预拌混凝土和预制混凝土构件生产质量管理标准 | DG/TJ08-2034-2019 | 2019-11-08 | 沪建标定〔2019〕513 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20191108/0011-71450.html) | [PDF](https://zjw.sh.gov.cn/cmsres/05/05fcf08f04d94f0fba0e5878890906ea/b736fb1ad0f59637c8f7d8a78ac27399.pdf) |

### 改造与历史建筑（18）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 房屋修缮工程施工质量验收标准 | - | 2026-04-14 | 沪建标定〔2026〕148号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4b8d3f626249441b9d040e08a0ca729d&siteId=0011) | - |
| 既有建筑实景三维建模技术标准 | - | 2026-03-02 | 沪建标定〔2026〕27 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/ce72b898d7b8478998ca5d6e121da496.html) | [PDF](https://zjw.sh.gov.cn/cmsres/a8/a8eb87b54c7b4971a1ee618b12e089d9/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 盾构法隧道结构服役性能鉴定标准 | DG/TJ08-2123-2013 | 2025-07-25 | 沪建标定〔2025〕383号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4af63eca3ac341b6ae02f78c1b30e6c8&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/322%E7%9B%BE%E6%9E%84%E6%B3%95%E9%9A%A7%E9%81%93%E7%BB%93%E6%9E%84%E6%9C%8D%E5%BD%B9%E6%80%A7%E8%83%BD%E9%89%B4%E5%AE%9A%E8%A7%84%E8%8C%83.pdf) |
| 优秀历史建筑数字化测绘技术标准 | - | 2025-06-11 | 沪建标定〔2025〕300号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4853f556bce74c938b66de1eee65d0cb&siteId=0011) | - |
| 优秀历史建筑保护修缮技术标准 | DG/TJ08-108-2014 | 2025-04-08 | 沪建标定〔2025〕201号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=003aadbdf0e244b2992c35aec11bbeb2&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/369%E4%BC%98%E7%A7%80%E5%8E%86%E5%8F%B2%E5%BB%BA%E7%AD%91%E4%BF%9D%E6%8A%A4%E4%BF%AE%E7%BC%AE%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B.pdf) |
| 旧住房更新改造查勘标准 | - | 2025-03-26 | 沪建标定〔2025〕111 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250326/e71540ea22434ff1b4605ebf56dcbd89.html) | [PDF](https://zjw.sh.gov.cn/cmsres/ad/ad5d705a61924460b6282436392a09ae/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 旧住房更新改造查勘标准 | - | 2025-02-25 | 沪建标定〔2025〕111号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=75a94fab5a4a42739c9e2068885f605e&siteId=0011) | - |
| 上海市既有住宅承重结构损坏及修复检测鉴定技术导则 | - | 2024-05-24 | 沪建城管联〔2024〕180号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=6d57dd92dfb343009eae055cae58d607&siteId=0011) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/6b/6b1d17a1953343228e4964803cd59c90/29301feddaff710782274c375e1b0428.pdf&filename=1.%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%97%A2%E6%9C%89%E4%BD%8F%E5%AE%85%E6%89%BF%E9%87%8D%E7%BB%93%E6%9E%84%E6%8D%9F%E5%9D%8F%E5%8F%8A%E4%BF%AE%E5%A4%8D%E6%A3%80%E6%B5%8B%E9%89%B4%E5%AE%9A%E6%8A%80%E6%9C%AF%E5%AF%BC%E5%88%99%EF%BC%88%E6%B8%85%E7%A8%BF%EF%BC%89.pdf) |
| 上海市既有住宅承重结构损坏修复技术导则 | - | 2024-05-24 | 沪建城管联〔2024〕180号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=6d57dd92dfb343009eae055cae58d607&siteId=0011) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/6b/6b1d17a1953343228e4964803cd59c90/29301feddaff710782274c375e1b0428.pdf&filename=1.%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%97%A2%E6%9C%89%E4%BD%8F%E5%AE%85%E6%89%BF%E9%87%8D%E7%BB%93%E6%9E%84%E6%8D%9F%E5%9D%8F%E5%8F%8A%E4%BF%AE%E5%A4%8D%E6%A3%80%E6%B5%8B%E9%89%B4%E5%AE%9A%E6%8A%80%E6%9C%AF%E5%AF%BC%E5%88%99%EF%BC%88%E6%B8%85%E7%A8%BF%EF%BC%89.pdf) |
| 房屋质量检测鉴定标准 | - | 2024-01-24 | 沪建标定〔2024〕42号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=a9b00f3cf77d4855872aa43b9df3aa62&siteId=0011) | - |
| 住宅修缮工程质量检测及评定标准 | - | 2023-05-19 | 沪建标定〔2023〕241号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=21932ece268945c683d931473c622854&siteId=0011) | - |
| 既有住宅小区宜居改造技术标准 | DG/TJ08-2374-2022 | 2022-08-03 | 沪建标定〔2021〕355号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d5a8cb5bb2534f4281ed8a8ad6ce2e5f&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/1e/1e0e8af6338a480c9ee6c2d2a47a6fb9/739b080dab1795ee362482b3744655e5.pdf) |
| 信息通信架空线缆隐蔽化改造工程技术标准 | - | 2022-06-27 | 沪建标定〔2022〕288号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=62aac419c76143ff96444e1bdc0a9d97&siteId=0011) | - |
| 地铁盾构法隧道衬砌加固技术标准 | - | 2021-12-02 | 沪建标定〔2021〕786号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=f275381207ab4c55b73497b77801e55b&siteId=0011) | - |
| 现有建筑抗震鉴定与加固标准 | DGJ08-81-2021 | 2021-06-28 | 沪建标定〔2021〕80 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/83118d5b004b45b2af818e03843a8503.html) | [PDF](https://zjw.sh.gov.cn/cmsres/70/70c1a5c3608141f7b12e22dda36f702a/0eb4335ec853a054ba763ada4704072e.pdf) |
| 既有建筑外立面整治设计标准 | DG/TJ08-2367-2021 | 2021-05-31 | 沪建标定〔2021〕335号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=3d979b039e6a4782820a47c16cc22e43&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/cf/cf25edbf08a54f77aed9303c53d78818/5ceb9f6b0e8ee38b1db84714fb60f36a.pdf) |
| 房屋修缮工程术语标准 | DG/TJ08-2288-2019 | 2019-11-08 | 沪建标定〔2019〕626 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20191108/0011-71457.html) | [PDF](https://zjw.sh.gov.cn/cmsres/40/406e7e80c4014414a63fc44083c8c366/1d927d5c2a267a1b72c845e60cea4fd9.pdf) |
| 上海市郊野乡村风貌规划设计和建设导则（二） | - | 2019-01-14 | 沪建村镇〔2018〕827 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56114.html) | - |

### 设备与智能化（50）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 建筑信息模型技术应用标准(港口航道工程) | - | 2026-08-06 | 沪建标定〔2026〕244 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260806/3b3694d5399641e694d85d433716ec56.html) | [PDF](https://zjw.sh.gov.cn/cmsres/dc/dc1ea17e4e174d629b43e3c1c0e82e53/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城镇排水泵站设计标准 | DGJ08-22-2018 | 2026-08-05 | 沪建标定〔2026〕330号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=bb6f254d99284cf99de00071c33826c7&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/67/6720573f7e764cd5b1171a810d9eff9a/99536544e0f15e5fbb8c6920c4988f21.pdf) |
| 城镇排水管道设计标准 | - | 2026-04-13 | 沪建标定〔2026〕140号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=51337c9d8b0148f1ae994edafdf084ab&siteId=0011) | - |
| 燃气分布式供能系统工程技术标准 | DG/TJ08-115-2016 | 2026-03-02 | 沪建标定〔2025〕628 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/8fc0f5dda0a84aba82eca687d7366037.html) | [PDF](https://zjw.sh.gov.cn/cmsres/42/423efbc2f6de44468fd833f26e95c028/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城市轨道交通通信传输系统技术标准 | - | 2025-11-14 | 沪建标定〔2025〕567号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=379c65d02a4645b39dec93e517e4376c&siteId=0011) | - |
| 建筑信息模型技术应用标准（民用建筑工程） | - | 2025-11-12 | 沪建标定〔2025〕458 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20251112/be2e8cb2a76d4f7885d80ac8f102fbe1.html) | [PDF](https://zjw.sh.gov.cn/cmsres/59/59678f3d0f754312a406b8f6fd899660/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 民用建筑空气源热泵供热系统应用技术标准 | - | 2025-11-07 | 沪建标定〔2025〕560号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=0cc8fc1295a94953b1219b9a3fdacbb5&siteId=0011) | - |
| 建筑信息模型技术应用标准（市政道路桥梁工程） | - | 2025-11-07 | 沪建标定〔2025〕558号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=73f0343aa5a340a69ed122526edecb53&siteId=0011) | - |
| 建筑信息模型技术应用标准（市政给水排水工程） | - | 2025-09-25 | 沪建标定〔2025〕372 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250925/6ed9ec4fde1b4de1a8f70b586f63dac6.html) | [PDF](https://zjw.sh.gov.cn/cmsres/bf/bf4d600920f942f99474986a691eb245/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 建筑信息模型技术应用标准（市政给水排水工程） | - | 2025-09-10 | 沪建标定〔2025〕372 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250910/4dac7fd900a44148909f6ee533e242fa.html) | [PDF](https://zjw.sh.gov.cn/cmsres/df/df40c511c13746dcb442bb2321d4bb34/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 道路照明设施运行养护标准 | DG/TJ08-2215-2016 | 2025-07-17 | 沪建标定〔2025〕364号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=3884bfe2b3744ad3b8ffe8c30014d4ac&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/d3/d3a92eee804f4c17b78a8511224904d9/86497e0ce327321de929d52f36ba6c13.pdf) |
| 道路交通信号设施技术标准 | - | 2025-06-03 | 沪建标定〔2025〕219 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250603/adc5bd75a58143558bd1e2fef75a9ef1.html) | [PDF](https://zjw.sh.gov.cn/cmsres/f9/f99ced042cc6486ea5b2c816e8387cdb/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 上海市城市生命线安全工程信息通信管线 风险排查与评估导则 | - | 2025-05-28 | 沪经信基〔2025〕318号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=dd455ce0463445c2b1dd7ac8cdade7a3&siteId=0020) | [PDF](https://www.shanghai.gov.cn/cmsres/policy_resources/dd455ce0463445c2b1dd7ac8cdade7a3/9e7945eb5fb24823843d2a85f1a1d923/%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%9F%8E%E5%B8%82%E7%94%9F%E5%91%BD%E7%BA%BF%E5%AE%89%E5%85%A8%E5%B7%A5%E7%A8%8B%E4%BF%A1%E6%81%AF%E9%80%9A%E4%BF%A1%E7%AE%A1%E7%BA%BF%E9%A3%8E%E9%99%A9%E6%8E%92%E6%9F%A5%E4%B8%8E%E8%AF%84%E4%BC%B0%E5%AF%BC%E5%88%99.doc) |
| 地面辐射供暖技术标准 | DGJ08-2161-2015 | 2025-04-08 | 沪建标定〔2025〕203号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=952b5f328e03489bbb6ceefb492df32c&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/%E5%9C%B0%E9%9D%A2%E8%BE%90%E5%B0%84%E4%BE%9B%E6%9A%96%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B20160217095557.pdf) |
| 地下管线探测技术标准 | DGJ08-2097-2012 | 2025-03-11 | 沪建标定〔2025〕147号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=63bb3b9de6024ba3914fbda2ca105c39&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/281%E5%9C%B0%E4%B8%8B%E7%AE%A1%E7%BA%BF%E6%8E%A2%E6%B5%8B%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B.pdf) |
| 建筑信息模型技术应用标准（城市轨道交通） | - | 2025-02-11 | 沪建标定〔2025〕50 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250211/117410708d7f4f5b8553285016054013.html) | [PDF](https://zjw.sh.gov.cn/cmsres/be/be4b4d377b3d4696934bd3b00e036cd0/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城镇排水工程施工质量验收标准 | DG/TJ08-2110-2012 | 2025-01-17 | 沪建标定〔2025〕35号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=420a9200bae347c28b0fdf61fb2aaf9f&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/300%E5%9F%8E%E9%95%87%E6%8E%92%E6%B0%B4%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E8%B4%A8%E9%87%8F%E9%AA%8C%E6%94%B6%E8%A7%84.pdf) |
| 城镇高压、超高压天然气管道工程技术标准 | DGJ08-102-2003 | 2024-07-10 | 沪建标定〔2024〕350号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=5aedba78cd55419e966e114e559816b8&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/76%E5%9F%8E%E9%95%87%E9%AB%98%E5%8E%8B%E3%80%81%E8%B6%85%E9%AB%98%E5%8E%8B%E5%A4%A9%E7%84%B6%E6%B0%94%E7%AE%A1%E9%81%93%E5%B7%A5%E7%A8%8B%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B.pdf) |
| 排水管道通用图集 | - | 2024-07-10 | 沪建标定〔2024〕348号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=716aefb18cf649ddbbd4a40de83fc934&siteId=0011) | - |
| 城镇燃气用户端安全技术标准 | - | 2024-06-11 | 沪建标定〔2024〕289号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=fdc5f11e86df4fd2851a4978055587eb&siteId=0011) | - |
| 建筑信息模型技术应用统一标准 | - | 2024-03-29 | 沪建标定〔2024〕21 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20240329/e94650a94e484fc083181e38f531d4f6.html) | [PDF](https://zjw.sh.gov.cn/cmsres/43/433305412e7f43d19960b9b7836e4f84/914e4a52cc55219a5a078633254fe067.pdf) |
| 多联式空调（热泵）工程施工技术标准 | DG/TJ08-2091-2012 | 2024-03-10 | 沪建标定〔2024〕65 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20240310/796daf4fdbe2447d93b82d5b9a42e166.html) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/274%E5%A4%9A%E8%81%94%E5%BC%8F%E7%A9%BA%E8%B0%83%EF%BC%88%E7%83%AD%E6%B3%B5%EF%BC%89%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B.pdf) |
| 多联式空调（热泵）工程施工技术标准 | DG/TJ08-2091-2012 | 2024-02-02 | 沪建标定〔2024〕65号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4061d9b195ed4d8ba5fd051210d4200d&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/274%E5%A4%9A%E8%81%94%E5%BC%8F%E7%A9%BA%E8%B0%83%EF%BC%88%E7%83%AD%E6%B3%B5%EF%BC%89%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B.pdf) |
| 上海市房屋建筑工程施工图设计文件技术审查要点（建筑设备篇） | - | 2024-01-29 | 沪建质安〔2024〕38 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20240129/75ce57f12921431798fb94a6745412e3.html) | [PDF](https://zjw.sh.gov.cn/cmsres/2f/2faf247ff3a048c6b601f2ef95484e6f/189af3f80e20c8e2996ec95b49abde5c.docx) |
| 道路照明工程建设技术标准 | DG/TJ08-2214-2016 | 2023-08-21 | 沪建标定〔2023〕439号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ab67fef557f246cf883afc7f7d90bb7b&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/3f/3fc00969eb7544d897ee609da4e52a37/d367c0c192ef688344584b4dc130a204.pdf) |
| 排水系统数学模型构建及应用标准 | - | 2023-07-11 | 沪建标定〔2023〕346号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=620889fc69ec48659e138ccfb86a1f46&siteId=0011) | - |
| 专用数字无线对讲通信系统工程技术标准 | - | 2022-12-19 | 沪建标定〔2022〕736号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=0b00d5a1d4534700a0ec9dc8dd1c6684&siteId=0011) | - |
| 城镇天然气管道工程技术标准 | DJ/TJ08-10-2022 | 2022-09-09 | 沪建标定〔2022〕452号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=988afab6b0224fe0a5552e6bd9d0e844&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/4e/4e596d8a277c419eb9eeb8d24fc9a565/897d8fd2c91ff1e3526e383e7e37a21b.pdf) |
| 大型泵站设备设施运行标准 | DG/TJ08-2045-2008 | 2022-08-11 | 沪建标定〔2022〕381号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=2a64472f386c497a97ea65e7cb8ecd67&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/207%E5%A4%A7%E5%9E%8B%E6%B3%B5%E7%AB%99%E8%AE%BE%E5%A4%87%E8%AE%BE%E6%96%BD%E8%BF%90%E8%A1%8C%E8%A7%84%E7%A8%8B.pdf) |
| 城市轨道交通专用无线通信系统技术标准 | DG/TJ08-104-2014 | 2022-08-08 | 沪建标定〔2022〕370号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=f613b33c0dbd4fe98491d4f28db3df77&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/370%E5%9F%8E%E5%B8%82%E8%BD%A8%E9%81%93%E4%BA%A4%E9%80%9A%E4%B8%93%E7%94%A8%E6%97%A0%E7%BA%BF%E9%80%9A%E4%BF%A1%E7%B3%BB%E7%BB%9F.pdf) |
| 管线定向钻进技术标准 | DG/TJ 08-2075-2022 | 2022-07-20 | 沪建标定〔2022〕328号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=6f6e13a3ed5e4a1b800c29f27adba60b&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/55/55bee00ba6fb4e7a94f8707f0837186f/1ad93977e649ad7d40fc901dca7c6069.pdf) |
| 轨道交通兼顾设防工程防护设备选用图集 | - | 2022-01-28 | 沪建标定〔2022〕80号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=9dec254e2c9d4c4aa3289ff3213a86a4&siteId=0011) | - |
| 公众移动通信室内信号覆盖系统设计与验收标准 | - | 2022-01-05 | 沪建标定〔2022〕13号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=be4f0b968bef431ca4bbf92b267fcfed&siteId=0011) | - |
| 上海市泵闸工程管线设计及施工技术导则 | - | 2021-12-27 | 沪水务〔2021〕916号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=3526f8a2a4bb4a23959549caf4557f8b&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/58/58e3901075b54594ace94c1bdf847158/910598a89a78438011d24671ae128d62.pdf&filename=%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%B3%B5%E9%97%B8%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%BA%BF%E8%AE%BE%E8%AE%A1%E5%8F%8A%E6%96%BD%E5%B7%A5%E6%8A%80%E6%9C%AF%E5%AF%BC%E5%88%99%E3%80%8B-%E5%8F%91%E5%B8%83%E7%89%88.pdf) |
| 光纤到户工程设计安装图集 | - | 2021-12-02 | 沪建标定〔2021〕792号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=cb43985b923a42129eee182ef0ff3a2d&siteId=0011) | - |
| 广电接入网工程技术标准 | - | 2021-11-17 | 沪建标定〔2021〕726号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=807186a143794b3298ac1dfdd4ed0354&siteId=0011) | - |
| 上海市排水检测井技术规程 | - | 2021-10-19 | 沪水务〔2021〕703号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=f12dc0b543544f3f9093b5be8d5ec18f&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/77/77d6d58f77ea4c248311ce53fbe365e1/761806a47f638b5864deca7d36a70e33.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%8E%92%E6%B0%B4%E6%A3%80%E6%B5%8B%E4%BA%95%E5%9B%BE%E9%9B%86-%E7%BB%88%E7%A8%BF.pdf) |
| 上海市排水检测井图集 | - | 2021-10-19 | 沪水务〔2021〕703号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=f12dc0b543544f3f9093b5be8d5ec18f&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/77/77d6d58f77ea4c248311ce53fbe365e1/761806a47f638b5864deca7d36a70e33.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%8E%92%E6%B0%B4%E6%A3%80%E6%B5%8B%E4%BA%95%E5%9B%BE%E9%9B%86-%E7%BB%88%E7%A8%BF.pdf) |
| 地源热泵系统工程技术标准 | DG/TJ08-2119-2021 | 2021-08-10 | 沪建标定〔2021〕514号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b183379187b046afb75ebfcc8f1b6c9e&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/6b/6be97a4255834810b8406ede38dcc0f5/7def06be63c4640b8417e9dc00f68ce3.pdf) |
| 燃气管道设施标识应用图集 | DG/TJ08-2012-2018 | 2021-06-28 | 沪建标定〔2021〕91 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/aaa9ed208b134d7dbbf9eeb3cb807a44.html) | [PDF](https://zjw.sh.gov.cn/cmsres/3f/3f0348b0c8ea44b194513a424a277e35/0458457391beabb91bb60eab82188a51.pdf) |
| 城市轨道交通机电设备安装工程质量验收标准 | DG/TJ08-2005-2023 | 2021-06-28 | 沪建标定〔2021〕87 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/999c6c085e454917921feaacd6453790.html) | [PDF](https://zjw.sh.gov.cn/cmsres/d1/d1ef616ddbd243c9a4de1b914c1b031c/2767b947cf4bafb5d0a68b5ce21255d8.pdf) |
| 上海市道路照明设施标准图集 | - | 2021-04-15 | 沪建标定〔2021〕224 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210415/00b7409d76e74bfc9ae8a85a269c821e.html) | [PDF](https://zjw.sh.gov.cn/cmsres/04/04aa649864104313915a2db2826cd868/a71c76a2c332fa8c7444fbf8e9b6312a.pdf) |
| 玻璃纤维增强塑料夹砂排水管道工程施工及验收标准 | DG/TJ08-234-2020 | 2020-10-29 | 沪建标定〔2020〕387 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20201029/7e1e81bec4fd4848982578f89a24229a.html) | [PDF](https://zjw.sh.gov.cn/cmsres/68/6804243f399640f08136bd0bee26912f/dbb33ad3219829b9b3c78f13a70db990.pdf) |
| 地下工程中空层排水及渗漏观察构造 | - | 2020-06-15 | 沪建标定〔2020〕205 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200615/f28bf5ea11f74597b1c5e2c45bfe9259.html) | - |
| 建筑同层排水系统应用技术标准 | DG/TJ08-2314-2020 | 2020-04-13 | 沪建标定〔2020〕144 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200413/44cc0b9801f54d71b051234f32c33192.html) | [PDF](https://zjw.sh.gov.cn/cmsres/e7/e757656ee0764aeab2403dbb9e190ac4/8af604bfc3af1bd19f92f56452022fef.pdf) |
| 市政地下空间建筑信息模型应用标准 | DG/TJ08-2311-2019 | 2020-03-10 | 沪建标定〔2020〕40 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200310/8b5794b1704a401bab651a6c280653d5.html) | [PDF](https://zjw.sh.gov.cn/cmsres/89/892a7fbec53d4dda94d32e43030e79e3/1eb321851e086732ad491a7fb60951d6.pdf) |
| 城镇排水泵站设计标准 | DGJ08-22-2018 | 2019-02-25 | 沪建标定〔2019〕68 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190225/0011-57966.html) | [PDF](https://zjw.sh.gov.cn/cmsres/67/6720573f7e764cd5b1171a810d9eff9a/99536544e0f15e5fbb8c6920c4988f21.pdf) |
| 液化天然气应急储备调峰站设计标准 | DG/TJ08-2014-2018 | 2019-01-14 | 沪建标定〔2018〕810 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56119.html) | [PDF](https://zjw.sh.gov.cn/cmsres/b9/b9ae9c40895b4697a9dd793e1671732f/3ea914a08f29dbdc8ef1526e8059b341.pdf) |
| 埋地塑料排水管道工程技术标准 | DG/TJ08-308-2018 | 2019-01-14 | 沪建标定〔2018〕811 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56118.html) | [PDF](https://zjw.sh.gov.cn/cmsres/7a/7afc45b5678742f28d9c4d1b073a9efc/1e2a1671fc036c6d20562b28ea92f500.pdf) |
| 上海市小型生活垃圾收集压缩站装运设备技术要求 | - | 2011-04-13 | 沪绿容(2011)112号 | [发布页](https://lhsr.sh.gov.cn/zcfg/20200728/218be9fdc8b342e5a7fa9032e3a92a59.html) | [PDF](https://www.shanghai.gov.cn/Plugins/ueditor_release-ueditor1_4_3_1-utf8-net/net/upload/file/20181204/63679534415048576717552090483013db.doc) |

### 轨道交通与地下工程（27）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 城市轨道交通地下车站与周边连通工程设计标准 | - | 2026-08-06 | 沪建标定〔2026〕282 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260806/bfd5c3eb9cd043e1937edc481fe66692.html) | [PDF](https://zjw.sh.gov.cn/cmsres/21/21367945bec7405390c260a94ccd1de8/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城市轨道交通无障碍设施建设技术标准 | - | 2026-08-06 | 沪建标定〔2026〕281 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260806/1c78ad2705f94112bbae5a5baffce442.html) | [PDF](https://zjw.sh.gov.cn/cmsres/e4/e449a2a061d64fa1bac9f1dd15303bfb/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城市轨道交通工程车辆选型技术标准 | DGJ08-106-2015 | 2026-06-08 | 沪建标定〔2026〕128 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260608/3e0a32a9878a446b88ad0b10c5af2637.html) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/106%E5%9F%8E%E5%B8%82%E8%BD%A8%E9%81%93%E4%BA%A4%E9%80%9A%E5%B7%A5%E7%A8%8B%E8%BD%A6%E8%BE%86%E9%80%89%E5%9E%8B%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%8320151228161323.pdf) |
| 地下空间一体化设计标准 | - | 2026-04-02 | 沪建标定〔2026〕127号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=862d772bfc46428db93c8202b54ea601&siteId=0011) | - |
| 城市综合管廊维护技术标准 | DG/TJ08-2168-2015 | 2026-04-02 | 沪建标定〔2026〕126号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b8a37e4ab5ca4a20912cb2b068f98acd&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/14%E5%9F%8E%E5%B8%82%E7%BB%BC%E5%90%88%E7%AE%A1%E5%BB%8A%E7%BB%B4%E6%8A%A4%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B20151028141202.pdf) |
| 地下连续墙施工标准 | DG/TJ08-2073-2016 | 2026-04-02 | 沪建标定〔2026〕125号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=84c8013b19f64b68ad0de6c4bd82da85&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/8f/8f8db447e0874e6b81875a5d5a6a15ef/33b08f06f827ca6b92f7ed79571d0573.pdf) |
| 综合管廊工程技术标准 | DGJ08-2017-2014 | 2026-03-02 | 沪建标定〔2026〕49 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/14fa3f8c083d45c59c79c71a83c7c9d9.html) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/373%E7%BB%BC%E5%90%88%E7%AE%A1%E5%BB%8A%E5%B7%A5%E7%A8%8B%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83.pdf) |
| 城市地下综合体设计标准 | - | 2026-03-02 | 沪建标定〔2025〕636 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/c3f6d3a60d194810bf9106c58c51e028.html) | [PDF](https://zjw.sh.gov.cn/cmsres/55/558c4d0ffb65440aae6908639a0c065c/e04dd2dfd4171c1d4d6ce631f63bdf9b.pdf) |
| 道路隧道养护技术标准 | - | 2025-11-07 | 沪建标定〔2025〕559号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4f1d0bc280914754b76ac184ee5dfd0a&siteId=0011) | - |
| 市政地下工程施工质量验收标准 | DG/TJ08-236-2013 | 2025-10-11 | 沪建标定〔2025〕519号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=dba41d434c1d4a2fb343649c1eedd092&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/337%E5%B8%82%E6%94%BF%E5%9C%B0%E4%B8%8B%E5%B7%A5%E7%A8%8B%E6%96%BD%E5%B7%A5%E8%B4%A8%E9%87%8F%E9%AA%8C%E6%94%B6%E8%A7%84%E8%8C%83.pdf) |
| 上海市小型综合管廊规划设计导则 | - | 2025-09-19 | 沪规划资源政〔2025〕367号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=abdb4b5471d843a3ac9403d0161270f2&siteId=0032) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/36/36f3e63823874c5bba372fbeaf2a6b36/8a59baed8f95c3f478bd728b523f315c.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%B0%8F%E5%9E%8B%E7%BB%BC%E5%90%88%E7%AE%A1%E5%BB%8A%E8%A7%84%E5%88%92%E8%AE%BE%E8%AE%A1%E5%AF%BC%E5%88%99.pdf) |
| 盾构隧道壁后注浆质量检测技术标准 | - | 2025-09-16 | 沪建标定〔2025〕461号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=08b74e07f8c94ce988e4f9e0119a71d0&siteId=0011) | - |
| 微型顶管法施工技术规程 | - | 2025-07-28 | 沪水务〔2025〕300号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=0f832dff210d4e57a781bca17d28dea1&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/8c/8c04c69a95844385935be313359791fa/fe90defcf2838d146ced343cd9781217.pdf&filename=%E6%B2%AA%E6%B0%B4%E5%8A%A1%E3%80%942025%E3%80%95300%E5%8F%B7%E9%99%84%E4%BB%B6.pdf) |
| 建设工程地下水控制技术标准 | - | 2025-05-30 | 沪建标定〔2025〕285号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e816572395a54ad2b43fbf8ccc5fc446&siteId=0011) | - |
| 地下车库联络道设计标准 | - | 2024-01-16 | 沪建标定〔2024〕25号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=14c0df7911084fe89de279a3c3282fbd&siteId=0011) | - |
| 城市轨道交通钢弹簧浮置板轨道施工质量验收标准 | - | 2023-05-09 | 沪建标定〔2023〕228号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=129b39b1b98c41cf9f1c64c0b014faaa&siteId=0011) | - |
| 道路隧道养护运行评价技术标准 | - | 2023-04-13 | 沪建标定〔2023〕191号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=1284dcebb04548a8b4134748bca239a0&siteId=0011) | - |
| 城市轨道交通智慧车站技术标准 | - | 2021-12-24 | 沪建标定〔2021〕845号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=55754113408a46308175cf9740d008e2&siteId=0011) | - |
| 城市轨道交通CBTC信号系统技术标准 | - | 2021-08-10 | 沪建标定〔2021〕519号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=fdb26e12ee45424bb87a550168ddbbb2&siteId=0011) | - |
| 地铁盾构法隧道施工技术标准 | DG/TJ08-2041-2021 | 2021-06-28 | 沪建标定〔2021〕10 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/6f2a69b5b59e4cfa9ec2801cc5181fe3.html) | [PDF](https://zjw.sh.gov.cn/cmsres/5a/5aa7c900bcce40b19f9039ebd24c8524/bc682f5638d105df1d9ff38be049679e.pdf) |
| 轨道交通轨道精测网技术标准 | DG/TJ08-2333-2020 | 2021-06-28 | 沪建标定〔2021〕1 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/a52dedb1914842d18f520780dee16824.html) | [PDF](https://zjw.sh.gov.cn/cmsres/3e/3e13bd28a0374459a26cd615b874daec/d1f4bbb67170cb3a6d996e55842b40e0.pdf) |
| 临港新片区地下空间规划设计导则（试行） | - | 2020-11-11 | 沪自贸临管委〔2020〕922号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b88352e4c5524690b688dfbe255e3a16&siteId=0058) | - |
| 轨道交通规划设计标准 | DG/TJ08-2325-2020 | 2020-10-29 | 沪建标定〔2020〕497 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20201029/6dca86ff5afa486386d40ca578ecbd65.html) | [PDF](https://zjw.sh.gov.cn/cmsres/e5/e516387c96b54037afc701470285346f/0c35b8e1900a43cde15bed20fc21b169.pdf) |
| 地下工程橡胶防水材料成品检测及工程应用验收标准 | DG/TJ08-2132-2020 | 2020-10-29 | 沪建标定〔2020〕478 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20201029/49226809ed0d4a5eb5c7a2019d0db5c4.html) | [PDF](https://zjw.sh.gov.cn/cmsres/6e/6e16dbbdc38b4ee89d8818950d8c2d0f/03d3c65e8b870b3610b9079e394b1adf.pdf) |
| 城市轨道交通乘客信息系统技术标准 | DG/TJ08-2313-2020 | 2020-03-10 | 沪建标定〔2020〕38 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200310/3945737ef4bb49bfaa330b8e09542cdb.html) | [PDF](https://zjw.sh.gov.cn/cmsres/86/867e119da7ca4fc4bb613e69c949d270/716c126c554d4e9316622753dfa72e15.pdf) |
| 顶管工程设计标准 | DG/TJ08-2268-2019 | 2019-02-25 | 沪建标定〔2019〕5 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190225/0011-56688.html) | [PDF](https://zjw.sh.gov.cn/cmsres/0b/0b69413443af4722a8ebf1cf33bffb3a/cbcceb69d2cf82c7a076c75618b3ce8e.pdf) |
| 顶管工程设计标准 | DG/TJ08-2268-2019 | 2019-01-28 | 沪建标定〔2019〕5 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190128/0011-56224.html) | [PDF](https://zjw.sh.gov.cn/cmsres/0b/0b69413443af4722a8ebf1cf33bffb3a/cbcceb69d2cf82c7a076c75618b3ce8e.pdf) |

### 市政与道路（43）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 桥梁改扩建技术标准 | - | 2026-03-02 | 沪建标定〔2026〕47 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/7f255f5093e142e397954f87828180ab.html) | [PDF](https://zjw.sh.gov.cn/cmsres/4a/4a99c3a925044e22ae6f30c965f30ca5/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 高速公路改扩建设计标准 | - | 2026-03-02 | 沪建标定〔2026〕33 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/d0962bb3554a4958aed07254eec30fa4.html) | [PDF](https://zjw.sh.gov.cn/cmsres/61/616706dc330b4650b5b7be404919a261/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 建设项目交通影响评价技术标准 | DG/TJ08-2165-2015 | 2026-03-02 | 沪建标定〔2026〕25 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/2a32ed799c8c43018d1684afaffcf567.html) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/4%E5%BB%BA%E8%AE%BE%E9%A1%B9%E7%9B%AE%E4%BA%A4%E9%80%9A%E5%BD%B1%E5%93%8D%E8%AF%84%E4%BB%B7%E6%8A%80%E6%9C%AF%E6%A0%87%E5%87%8620151028140117.pdf) |
| 上海市综合杆搭载无轨电车设施设置导则（试行） | - | 2026-03-02 | 沪建设施联〔2025〕527 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/0c35997dfdaf4cba91e44b1982620955.html) | [PDF](https://zjw.sh.gov.cn/cmsres/f9/f91a4202af80476f92d5d9c4bd76cfc7/66ed7912afe02423bd58de5ce3012c66.pdf) |
| 城市客运交通枢纽设计标准 | - | 2025-11-12 | 沪建标定〔2025〕515 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20251112/73fc5c4cbaac4a6287df90f39e6267f1.html) | [PDF](https://zjw.sh.gov.cn/cmsres/54/54a826a474554f0697aa95495bc3dad0/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城市道路设计标准 | - | 2025-06-27 | 沪建标定〔2025〕235 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250627/0c21d7f857354b7280fb5cd86daa9fa8.html) | [PDF](https://zjw.sh.gov.cn/cmsres/3d/3d440474dbeb4894af1e2d4156200b4c/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城市道路设计标准 | - | 2025-06-17 | 沪建标定〔2025〕235 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250617/0b22055766074bd2b3e012bfe9cc8b7a.html) | [PDF](https://zjw.sh.gov.cn/cmsres/82/82c5906926b94359bf521658081a8062/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城市道路设计标准 | - | 2025-06-03 | 沪建标定〔2025〕235 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250603/efaeaeb00cb44b46ac92cf30086a04c3.html) | [PDF](https://zjw.sh.gov.cn/cmsres/d7/d7b77667a416444cb0f5b1ee8b0588da/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 桥梁顶推技术标准 | - | 2025-05-30 | 沪建标定〔2025〕291号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=7b65c5411d0c44a8955f01c36d2903be&siteId=0011) | - |
| 堤防工程安全评价及养护技术标准 | - | 2025-04-29 | 沪建标定〔2025〕237号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=47d8010fb54c492996e55f65bf16eac3&siteId=0011) | - |
| 城市道路设计标准 | - | 2025-04-27 | 沪建标定〔2025〕235号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ca0e8f97c17e45279a4c286b5fcdfa42&siteId=0011) | - |
| 公共汽车和电车中途站候车设施配置标准 | - | 2025-04-08 | 沪建标定〔2025〕205号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=3e49ab5fa6894cf39d45096cb44194d0&siteId=0011) | - |
| 公路养护工程质量检验评定标准 | - | 2025-03-26 | 沪建标定〔2025〕110 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250326/f9b78e833634487bb6ad7aea01b065e4.html) | [PDF](https://zjw.sh.gov.cn/cmsres/09/095a580b753b4569910eb7c8c2672bde/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 航道养护技术标准 | - | 2024-09-26 | 沪建标定〔2024〕370 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20240926/05d5a3022fdc4604bbd362acc0a14d02.html) | [PDF](https://zjw.sh.gov.cn/cmsres/da/daa9d45c4130416ca134612222f90f24/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 沥青路面预防养护技术标准 | - | 2024-05-24 | 沪建标定〔2024〕252号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=880009782ef645fcace29e7bb393422f&siteId=0011) | - |
| 上海市保障性住房（大型居住社区）配套建设管理导则（基地内市政公建配套）（2024年修订版） | - | 2024-05-22 | 沪建房管联〔2024〕243号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=939717ffe7414ae4a491d6c795c5c094&siteId=0011) | [PDF](https://www.shanghai.gov.cn/cmsres/policy_resources/939717ffe7414ae4a491d6c795c5c094/2a18f14955ca4a7493cc38f586312f6b/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BF%9D%E9%9A%9C%E6%80%A7%E4%BD%8F%E6%88%BF%EF%BC%88%E5%A4%A7%E5%9E%8B%E5%B1%85%E4%BD%8F%E7%A4%BE%E5%8C%BA%EF%BC%89%E9%85%8D%E5%A5%97%E5%BB%BA%E8%AE%BE%E7%AE%A1%E7%90%86%E5%AF%BC%E5%88%99%EF%BC%88%E5%9F%BA%E5%9C%B0%E5%86%85%E5%B8%82%E6%94%BF%E5%85%AC%E5%BB%BA%E9%85%8D%E5%A5%97%EF%BC%89%EF%BC%882024%E5%B9%B4%E4%BF%AE%E8%AE%A2%E7%89%88%EF%BC%89.docx) |
| 公路绿化建设与养护标准 | - | 2023-09-26 | 沪建标定〔2023〕317 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20230926/cc1abb095d9447f492967b3edae78bc1.html) | [PDF](https://zjw.sh.gov.cn/cmsres/ac/ac1879a36c6249c2a581b84f72b13e89/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 水闸与水利泵站维修养护技术标准 | - | 2023-09-11 | 沪建标定〔2023〕477号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=a4b53abdd01c4b8bba11e8abcc3242ee&siteId=0011) | - |
| 海塘维修养护技术标准 | - | 2023-05-30 | 沪建标定〔2023〕265号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=df5d9daf664e4490ad0172a72d923ceb&siteId=0011) | - |
| 园林绿化养护标准 | - | 2023-05-22 | 沪建标定〔2023〕248号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4de82b3b41104cbb8cda37cf2dfc7988&siteId=0011) | - |
| 桥梁工业化评价标准 | - | 2023-05-22 | 沪建标定〔2023〕247号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=41e255130b81453589ba9467f642a0dd&siteId=0011) | - |
| 上海市道路、公共广场等废物箱配置导则（2023版） | - | 2023-05-05 | 沪绿容〔2023〕175号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=8ed278f4-e75c-45bf-b33c-663df742a1b7&siteId=0039) | - |
| 上海市河道维修养护技术规程 | - | 2022-11-09 | 沪水务〔2022〕901号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ee9dfc13e126437087633912d4872e49&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/16/16ab30bd436d4b4a9b5dd7d6af92c137/3bb69317a84c9463536f17708293c0d2.pdf&filename=%E6%B2%AA%E6%B0%B4%E5%8A%A1%E3%80%942022%E3%80%95901%E5%8F%B7%E9%99%84%E4%BB%B6.pdf) |
| 行道树栽植与养护技术标准 | - | 2022-08-08 | 沪建标定〔2022〕367号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4104dc551c584dc9bceaeef81c6b6a18&siteId=0011) | - |
| 城市道路平面交叉口规划与设计标准 | - | 2022-07-20 | 沪建标定〔2022〕332号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=470fbc14c7ab48fc9e7b45886ecdf50f&siteId=0011) | - |
| 出租汽车站点设置标准 | DG/TJ08-2108-2012 | 2022-05-09 | 沪建标定〔2023〕229号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=a8eb298c455f4efbbf92f153bc174981&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/295%E5%87%BA%E7%A7%9F%E6%B1%BD%E8%BD%A6%E7%AB%99%E7%82%B9%E8%AE%BE%E7%BD%AE%E8%A7%84%E8%8C%83.pdf) |
| 道路可变信息标志技术标准 | - | 2022-01-26 | 沪建标定〔2022〕69号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d12df50cdc324fbb804f95ba969f44bf&siteId=0011) | - |
| 路面设计标准 | - | 2022-01-05 | 沪建标定〔2022〕10号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d240d021db5e4b7496c67559d304f159&siteId=0011) | - |
| 道路与交通设施规划标准 | - | 2021-12-24 | 沪建标定〔2021〕842号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b78336bef78c40f9a478f409ebe0b753&siteId=0011) | - |
| 钢桥面铺装工程应用技术标准 | DG/TJ08-2353-2020 | 2021-07-01 | 沪建标定〔2021〕183 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210701/1a1a6feeb49c4ce49c673009a80e8c5e.html) | [PDF](https://zjw.sh.gov.cn/cmsres/ff/ff2f81bb6eb5476aa854f4ee636cb059/6dc36b93c04e3c5ea3e985a89985ef94.pdf) |
| 桥梁顶升施工技术标准 | - | 2021-07-01 | 沪建标定〔2021〕182 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210701/c2be611411844d2eba6daf394d3fae49.html) | [PDF](https://zjw.sh.gov.cn/cmsres/da/dab022bb25304a9e90393a9651b51691/6ee052b61c7ca17fdbc36bf0d1ca768c.pdf) |
| 综合杆设施技术标准 | DG/TJ08-2362-2021 | 2021-06-28 | 沪建标定〔2021〕83 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/7aebc86490554ecf8687dad519509496.html) | [PDF](https://zjw.sh.gov.cn/cmsres/de/deaa94199cfc40d5b8f7ee015cf5a467/bb3bbffe1d839012e700ed95cfb9974c.pdf) |
| 城市综合交通规划技术标准 | DG/TJ08-2039-2021 | 2021-06-28 | 沪建标定〔2021〕9 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/294b270e2e96441ebcb4421a0127616b.html) | [PDF](https://zjw.sh.gov.cn/cmsres/b6/b6b723acf90044568764eeb74373dded/fc2cbb6b99a716d4c3ce1f85730b83ac.pdf) |
| 桥梁顶升施工技术标准 | - | 2021-04-15 | 沪建标定〔2021〕182 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210415/69f795279a7b4563a1e0963cfaec3faf.html) | [PDF](https://zjw.sh.gov.cn/cmsres/34/3473f17ca1c34e64b3f4325f142f3572/6ee052b61c7ca17fdbc36bf0d1ca768c.pdf) |
| 钢桥面铺装工程应用技术标准 | DG/TJ08-2353-2020 | 2021-04-15 | 沪建标定〔2021〕183 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210415/7647f7357f2d4f96bab0439adaf55a8a.html) | [PDF](https://zjw.sh.gov.cn/cmsres/ff/ff2f81bb6eb5476aa854f4ee636cb059/6dc36b93c04e3c5ea3e985a89985ef94.pdf) |
| 公交场站规划用地及建设标准 | DG/TJ08-2057-2020 | 2020-10-29 | 沪建标定〔2020〕496 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20201029/a82612cbff1c4fc393f5f8b097e29b15.html) | [PDF](https://zjw.sh.gov.cn/cmsres/96/965bbb06a6694548b7ae820fdfffcf88/612ba888251ac27329a4bec17089ba86.pdf) |
| 原位利用疏浚泥建设生态护岸技术标准 | DG/TJ08-2331-2020 | 2020-10-29 | 沪建标定〔2020〕495 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20201029/2c1491fee2944a5c94b4003575d85eb8.html) | [PDF](https://zjw.sh.gov.cn/cmsres/3e/3e665929e9bd4bfc8882e17eeaf7ad5a/98c4a4253a0170833e4761be56905f21.pdf) |
| 道路视频监控信息系统联网技术标准 | DG/TJ08-2319-2020 | 2020-07-08 | 沪建标定〔2020〕256 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200708/97e1c92a3ac04f7cb3ae9392cc365d40.html) | [PDF](https://zjw.sh.gov.cn/cmsres/9c/9cbcedb3f24c49edb0fd58657e33db7d/67f3aac18874ef9fb6286c00a8897bbf.pdf) |
| 彩色路面技术标准 | DG/TJ08-2318-2020 | 2020-06-15 | 沪建标定〔2020〕209 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200615/30b8db1fcbbe4d06811f7bc4476562c6.html) | [PDF](https://zjw.sh.gov.cn/cmsres/38/38a14994676844198f13a6c8518c3f86/95d8082ca4e504208821b06c9238b391.pdf) |
| 上海市保障性住房（大型居住社区）配套建设管理导则（基地内市政公建配套）（2019 年修订版） | - | 2019-11-08 | 沪建房管联〔2019〕430 号 | [发布页](https://zjw.sh.gov.cn/fwgl/20191108/0011-71446.html) | [PDF](https://zjw.sh.gov.cn/cmsres/27/27879ae077e54bb3a7637ab83d7fa3f5/4bd179f0bc43d2498eff719c87d6da5f.docx) |
| 市政道路建设及整治工程全要素技术规定 | - | 2019-07-18 | 沪建设施联〔2019〕440号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=09f145a7201d4176a9a192d9e11597da&siteId=0011) | [PDF](https://www.shanghai.gov.cn/cmsres/policy_resources/09f145a7201d4176a9a192d9e11597da/05e88691df4c467f9f396a9678839e5a/%E3%80%8A%E5%B8%82%E6%94%BF%E9%81%93%E8%B7%AF%E5%BB%BA%E8%AE%BE%E5%8F%8A%E6%95%B4%E6%B2%BB%E5%B7%A5%E7%A8%8B%E5%85%A8%E8%A6%81%E7%B4%A0%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%E3%80%8B.doc) |
| 城市道路立体交叉规划与设计标准 | DG/TJ08-2283-2018 | 2019-01-14 | 沪建标定〔2018〕809 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56120.html) | [PDF](https://zjw.sh.gov.cn/cmsres/e8/e843d2051eb341588b9ace61fe4e3390/f288914a1602e7f4c363b5a04bd8c391.pdf) |
| 城市道路和桥梁数据采集标准 | DG/TJ08-2284-2018 | 2019-01-14 | 沪建标定〔2018〕844 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56113.html) | [PDF](https://zjw.sh.gov.cn/cmsres/f4/f405fe9f31724692b2e21dfc0ddd6b57/7f2ec25e91191219113d8a0d1d4b3075.pdf) |

### 水务与海绵（24）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 上海市海绵城市建设景观设计导则 | - | 2025-10-23 | 沪建综规〔2025〕540号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=6ef7fb25befc44a68b44f65c74d7e203&siteId=0011) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0011/67/67bebdbfcb2c4f21a2c4d9ae89adb7cf/dcb1becd71fba3be8a41c53e4d1f7da7.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%B5%B7%E7%BB%B5%E5%9F%8E%E5%B8%82%E5%BB%BA%E8%AE%BE%E6%99%AF%E8%A7%82%E8%AE%BE%E8%AE%A1%E5%AF%BC%E5%88%99.pdf) |
| 城镇污水处理厂分类技术标准 | DG/TJ08-2140-2014 | 2025-06-16 | 沪建标定〔2025〕317号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=13421f493c6546308b9f23e96f75c614&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/350%E5%9F%8E%E9%95%87%E6%B1%A1%E6%B0%B4%E5%A4%84%E7%90%86%E5%8E%82%E5%88%86%E7%B1%BB%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83.pdf) |
| 原水引水管渠监测技术规程 | - | 2025-04-06 | 沪水务〔2025〕129号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=a116e2865b5b4657a98b8cf0f4dd6fb8&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/cd/cda2da9bf4164ce09612dd8a93cd57eb/6a48f13d74a9145b7f94965dd946807b.pdf&filename=%E6%B2%AA%E6%B0%B4%E5%8A%A1%E3%80%942025%E3%80%95129%E5%8F%B7%E9%99%84%E4%BB%B6.pdf) |
| 上海市公园、绿地与“一江一河”滨水开放空间设施配建管理导则 | - | 2025-01-21 | 沪规划资源建〔2025〕15号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=569e5a462c0040948573c7ede95b987c&siteId=0032) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/9e/9e69134e509244f88da561ed58364a1b/d71c125e580c7482a6ac01bc272c0312.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%85%AC%E5%9B%AD%E3%80%81%E7%BB%BF%E5%9C%B0%E4%B8%8E%E2%80%9C%E4%B8%80%E6%B1%9F%E4%B8%80%E6%B2%B3%E2%80%9D%E6%BB%A8%E6%B0%B4%E5%BC%80%E6%94%BE%E7%A9%BA%E9%97%B4%E8%AE%BE%E6%96%BD%E9%85%8D%E5%BB%BA%E7%AE%A1%E7%90%86%E5%AF%BC%E5%88%99.pdf) |
| 城镇供水厂超滤膜处理工程技术标准 | - | 2025-01-03 | 沪建标定〔2025〕5号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c96f4a3779814c308c23cb7712b3611c&siteId=0011) | - |
| 港口船舶压载水接收设施技术标准 | - | 2024-09-26 | 沪建标定〔2024〕364 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20240926/28e507fa2d8842b5b5230dd6cb356c1e.html) | [PDF](https://zjw.sh.gov.cn/cmsres/ee/ee7dd47aaf1e4521bf21cbbbf75571be/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 城市供水管网泵站远程监控系统技术标准 | DG/TJ08-2207-2016 | 2024-03-07 | 沪建标定〔2024〕111号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ab922f6e67f74f078bd57712742230f6&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2207%E5%9F%8E%E5%B8%82%E4%BE%9B%E6%B0%B4%E7%AE%A1%E7%BD%91%E6%B3%B5%E7%AB%99%E8%BF%9C%E7%A8%8B%E7%9B%91%E6%8E%A7%E7%B3%BB%E7%BB%9F%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B20161010103248.pdf) |
| 上海市苏州河滨水公共空间户外招牌设置导则 | - | 2023-09-04 | 沪绿容〔2023〕343号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b4685be9-15d0-4e04-86ac-78878a18afb6&siteId=0039) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0039/79/7911bba4530d4206b13512266d567475/22a4c902b95d9e2b376bc585ffcfbc4a.pdf&filename=%E9%99%84%E4%BB%B61_%E8%8B%8F%E5%B7%9E%E6%B2%B3%E6%BB%A8%E6%B0%B4%E5%85%AC%E5%85%B1%E7%A9%BA%E9%97%B4%E6%88%B7%E5%A4%96%E6%8B%9B%E7%89%8C%E8%AE%BE%E7%BD%AE%E5%AF%BC%E5%88%99.pdf) |
| 平板膜生物反应器法污水处理工程技术标准 | DG/TJ08-2190-2015 | 2023-06-20 | 沪建标定〔2023〕315号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=07f430840d0d4f8bad2934f3bf4639a9&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/2190%E5%B9%B3%E6%9D%BF%E8%86%9C%E7%94%9F%E7%89%A9%E5%8F%8D%E5%BA%94%E5%99%A8%E6%B3%95%E6%B1%A1%E6%B0%B420160803141005.pdf) |
| 上海市小型水闸安全评价导则 | - | 2023-06-12 | 沪水务〔2023〕388号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=35e0ec695f2945e1b3a943ee96e42ecc&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/81/81ddb49793ee49c9ac3ed5990f24e339/253271679b0276422cf282cfee265e71.pdf&filename=%E6%B2%AA%E6%B0%B4%E5%8A%A1%E3%80%942023%E3%80%95388%E5%8F%B7%E9%99%84%E4%BB%B6.pdf) |
| 雨水调蓄设施技术标准 | - | 2023-06-01 | 沪建标定〔2023〕274号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=3ee7df6695774e97bb848742a5bf894e&siteId=0011) | - |
| 上海市圩区治理导则（试行） | - | 2023-05-15 | 沪水务〔2023〕336号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=8708556fc9d345d3b48e768228237ff6&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/58/58e855749c8a49019aed499d2283e072/c023e713ac1a9ff924a1f925b2ccd1a8.pdf&filename=%E6%B2%AA%E6%B0%B4%E5%8A%A1%E3%80%942023%E3%80%95336%E5%8F%B7%E9%99%84%E4%BB%B6.pdf) |
| 上海市新建居民住宅饮用水高品质入户工程技术规程 | - | 2022-12-02 | 沪水务〔2022〕1034号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=cdedd1001f624b9287f49baf6fcd71bc&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/9d/9d7e0a57d1b74a4d8c80e277bcfd3170/e6f80218deac33ea63ce4eff69f902de.pdf&filename=%E6%B2%AA%E6%B0%B4%E5%8A%A1%E3%80%942022%E3%80%951034%E5%8F%B7%E9%99%84%E4%BB%B6.pdf) |
| 上海市水利工程前期成果审查技术导则 | - | 2022-07-29 | 沪水务〔2022〕587号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=7f15aa824aad452e9f297ab6428c5cd2&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/00/00f63cb138274ae6a1bac7f7ff26a3d2/0cf81a54411a61effd1a00b7c3335532.pdf&filename=%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E6%B0%B4%E5%88%A9%E5%B7%A5%E7%A8%8B%E5%89%8D%E6%9C%9F%E6%88%90%E6%9E%9C%E5%AE%A1%E6%9F%A5%E6%8A%80%E6%9C%AF%E5%AF%BC%E5%88%99%E3%80%8B.pdf) |
| 上海市应急供水（回灌）深井建设与运行技术导则 | - | 2022-06-29 | 沪水务〔2022〕340号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=555a4dc5a60d42458d16c55a9ed0689c&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/99/99041ccc865c4081a7417fa6caaefe9d/736880e3f8896838df9114be326efd44.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%BA%94%E6%80%A5%E4%BE%9B%E6%B0%B4%EF%BC%88%E5%9B%9E%E7%81%8C%EF%BC%89%E6%B7%B1%E4%BA%95%E5%BB%BA%E8%AE%BE%E4%B8%8E%E8%BF%90%E8%A1%8C%E6%8A%80%E6%9C%AF%E5%AF%BC%E5%88%99-%E5%8F%91%E5%B8%83.pdf) |
| 城镇污水处理厂污泥干化焚烧处理工程建设标准 | - | 2022-03-01 | 沪建标定〔2022〕129号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=7ca762240cd74183852637d3a48348cf&siteId=0011) | - |
| 水利工程施工质量验收标准 | DG/TJ08-90-2021 | 2021-12-24 | 沪建标定〔2021〕846号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=b7f6ec7d959746b682498970154cfb9e&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/8e/8ef3fc4b53d5426aa91bc5d4d65f0248/c94e89bc03f0b66b78853a2c3227d40f.pdf) |
| 上海市雨水口截污过滤装置技术规程 | - | 2021-10-20 | 沪水务〔2021〕710号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=2b078f196cb044e7af032dc2c77d2d11&siteId=0004) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0004/b7/b70c995d4c6b4293a7ed49a16ef4527b/f71f5f960bb5f14f697a99dd1f404e95.pdf&filename=%E4%B8%8A%E6%B5%B7%E5%B8%82%E9%9B%A8%E6%B0%B4%E5%8F%A3%E6%88%AA%E6%B1%A1%E8%BF%87%E6%BB%A4%E8%A3%85%E7%BD%AE%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B%EF%BC%88%E5%8F%91%E5%B8%83%E7%A8%BF%EF%BC%89.pdf) |
| 城镇污水处理厂恶臭气体治理技术标准 | - | 2021-08-17 | 沪建标定〔2021〕528号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=9b415e54d19a4c2d8fa2b3ac86923086&siteId=0011) | - |
| 城镇污水深度处理反硝化砂滤池技术标准 | DG/TJ08-2351-2021 | 2021-06-28 | 沪建标定〔2021〕89 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/30d53d510e764eaaaf99764ff830cb85.html) | [PDF](https://zjw.sh.gov.cn/cmsres/26/26350fb5149f45d289c5e770563dcd37/fc5c15803050214f9f404dbe8ec88531.pdf) |
| 海绵城市设施施工验收与运行维护标准 | DG/TJ08-2370-2021 | 2021-05-31 | 沪建标定〔2021〕334号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=9bd835ced61f45589fe45b000dbd996f&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/80/80826f3a76ab4b02b8a2c564c90164a7/c08cb9ac30da3b2db3c4b329303366d7.pdf) |
| 海绵城市建设技术标准图集 | - | 2020-03-10 | 沪建标定〔2020〕36 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200310/544e0a7b2bde4092ba2b530989414537.html) | - |
| 上海市水务设施（厂/站）海绵城市建设技术导则 | - | 2018-07-23 | 沪水务〔2018〕664号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=f04562de51c04e0f87b58fc4864a546d&siteId=0004) | - |
| 上海水面清扫船技术要求 | - | 2012-04-12 | 沪绿容(2012)107号 | [发布页](https://lhsr.sh.gov.cn/zcfg/20200728/83cef740a3e14c8184032ff3bf26c5cd.html) | [PDF](https://www.shanghai.gov.cn/warehouse/upload/ck/files/20120426144800187.doc) |

### 绿化与市容（16）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 工程渣土资源化利用技术标准 | - | 2025-07-10 | 沪建标定〔2025〕350号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d1d0f744cbb34bf08b83f663e8f9dc42&siteId=0011) | - |
| 单位附属绿地开放共享建设技术标准 | - | 2025-05-13 | 沪建标定〔2025〕255号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=fc2a1bbf40dd4b919bb2bd71d685a9e7&siteId=0011) | - |
| 上海市休闲森林公园规划建设导则（试行） | - | 2025-03-26 | 沪绿容〔2025〕42号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=c0c24607db324badb16d78e6d4cea4a7&siteId=0039) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0039/e5/e5dbd5217b914df7b06530d2f1ed7c51/44205297c6d67075dc0e5149d00410fa.pdf&filename=%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BC%91%E9%97%B2%E6%A3%AE%E6%9E%97%E5%85%AC%E5%9B%AD%E8%A7%84%E5%88%92%E5%BB%BA%E8%AE%BE%E5%AF%BC%E5%88%99%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B.pdf) |
| 绿化植物保护技术标准 | DG/TJ08-35-2014 | 2025-03-26 | 沪建标定〔2025〕118 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20250326/3e217605e6f346709b41bb449cf7c7a2.html) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/3%E7%BB%BF%E5%8C%96%E6%A4%8D%E7%89%A9%E4%BF%9D%E6%8A%A4%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B20151028140043.pdf) |
| 生态公益林建设技术标准 | DG/TJ08-2058-2017 | 2025-03-11 | 沪建标定〔2025〕145号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=90691207ef054dc8aca0c14850782ce3&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/4c/4c8022f4208642db808c045741bef45d/cdc7e499b211a8cc6682d2e5314a84c1.pdf) |
| 绿化植物保护技术标准 | DG/TJ08-35-2014 | 2025-02-28 | 沪建标定〔2025〕118号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=5f5686bfaa2c470e81f387aabd29b98f&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/3%E7%BB%BF%E5%8C%96%E6%A4%8D%E7%89%A9%E4%BF%9D%E6%8A%A4%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B20151028140043.pdf) |
| 湿垃圾厌氧消化处理工程技术标准 | - | 2023-05-30 | 沪建标定〔2023〕264号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e45a350088314648bf2c3cddfa43257c&siteId=0011) | - |
| 上海市体育公园建设运营管理导则 | - | 2023-04-07 | 沪体财〔2023〕65号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=f05532b6a0f9489ba5e7085fb4869a38&siteId=0027) | [PDF](https://www.shanghai.gov.cn/cmsres/policy_resources/f05532b6a0f9489ba5e7085fb4869a38/e04ea26042964d67a57d7f496080a3a8/%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%BD%93%E8%82%B2%E5%85%AC%E5%9B%AD%E5%BB%BA%E8%AE%BE%E8%BF%90%E8%90%A5%E7%AE%A1%E7%90%86%E5%AF%BC%E5%88%99%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89.docx) |
| 上海市单位附属绿地开放共享建设技术导则（试行） | - | 2023-01-20 | 沪绿委办〔2023〕1号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=2280ebd7-2945-49e2-9276-68e6bb4280a4&siteId=0039) | - |
| 生活垃圾收集站（压缩式）设置标准 | - | 2021-12-24 | 沪建标定〔2021〕844号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=69d0fb14fc1c421d82593af6163a134c&siteId=0011) | - |
| 园林绿化栽植土质量标准 | DG/TJ 08-231-2021 | 2021-08-10 | 沪建标定〔2021〕511号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e44ef4ae8b914aa4b0d841e123eefdd6&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/52/5202de016568449da70e1a253069727f/f6ee8f38330dbdc0cea3db180196ea6b.pdf) |
| 园林绿化工程施工质量验收标准 | DG/TJ08-701-2020 | 2020-04-13 | 沪建标定〔2020〕145 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200413/b541c6e2197642f4bd88204832656c8c.html) | [PDF](https://zjw.sh.gov.cn/cmsres/12/12230ee675894cc0b6a20fa254f0bf6e/25434355b11f41723696428211220d6f.pdf) |
| 上海市行道树悬铃木果毛防控管理技术导则 | - | 2020-03-17 | 沪绿容〔2020〕106号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=0039-3C968351-22A0-49F0-BE90-AD05F5706B7A&siteId=0039) | [PDF](https://www.shanghai.gov.cn/cmsres/policy_resources/0039-3C968351-22A0-49F0-BE90-AD05F5706B7A/2271c4eaf0084c6abd9684d8da1209da/%E4%B8%8A%E6%B5%B7%E5%B8%82%E8%A1%8C%E9%81%93%E6%A0%91%E6%82%AC%E9%93%83%E6%9C%A8%E6%9E%9C%E6%AF%9B%E9%98%B2%E6%8E%A7%E7%AE%A1%E7%90%86%E6%8A%80%E6%9C%AF%E5%AF%BC%E5%88%99.docx) |
| 上海市智慧公厕建设导则（试行） | - | 2019-09-29 | 沪绿容(2019)373号 | [发布页](https://lhsr.sh.gov.cn/fzwj/20190929/0039-085A0FB6-50CA-467D-995B-DEBC6071A8E1.html) | [PDF](https://www.shanghai.gov.cn/cmsres/f6/f63988c89eb64616aa84f8fe51334525/27bdaf248eb96c96d3c8915de5d3d20b.docx) |
| 上海市绿道建设导则（试行） | - | 2016-01-04 | 沪绿容(2016)1号 | [发布页](https://lhsr.sh.gov.cn/zcfg/20160104/0039-EA9F2B42-264B-4E5C-BBE6-CD2FFA2C44CB.html) | - |
| 上海市环卫电动机具技术要求 | - | 2012-11-29 | 沪绿容(2012)368号 | [发布页](https://lhsr.sh.gov.cn/zcfg/20200728/45ca376bfc8b4e89abc6b866fcc56d10.html) | [PDF](https://www.shanghai.gov.cn/warehouse/upload/ck/files/20121214144439921.doc) |

### 勘察与测绘（11）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 工程物探技术标准 | DG/TJ08-2271-2018 | 2026-04-02 | 沪建标定〔2026〕124号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e8aa16c92814422bb798a21c4495b5d1&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/f9/f9583025d17a4370b75c8be3fbdf5f3d/c3be844a9eb49a065906efd7e79d698c.pdf) |
| 岩土工程监测数字化技术标准 | - | 2026-03-02 | 沪建标定〔2026〕46 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20260302/c20415682f7a4ae884d1204239e35a7a.html) | [PDF](https://zjw.sh.gov.cn/cmsres/23/23f98732f54e4d9cbe19543cbc47f589/b80791aa8c389e36eb5f8dc5f0058ce6.pdf) |
| 上海市智能网联汽车测绘地理信息安全管理导则（试行） | - | 2025-08-25 | 沪规划资源调〔2025〕328号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=7fb303a0931747f9a4f24b34dc4bfe60&siteId=0032) | - |
| 地面沉降监测设施维护维修技术标准 | - | 2025-05-13 | 沪建标定〔2025〕254号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=1290c56f2b0c4b9cb244fee5cfc994ed&siteId=0011) | - |
| 上海市房屋建筑工程施工图设计文件技术审查要点（岩土工程勘察篇） | - | 2024-01-29 | 沪建质安〔2024〕38 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20240129/75ce57f12921431798fb94a6745412e3.html) | [PDF](https://zjw.sh.gov.cn/cmsres/2f/2faf247ff3a048c6b601f2ef95484e6f/189af3f80e20c8e2996ec95b49abde5c.docx) |
| 岩土工程勘察标准 | DGJ08-37-2012 | 2023-05-22 | 沪建标定〔2023〕250号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=13d55c15901843efbdaa9796e1ea511f&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/285%E5%B2%A9%E5%9C%9F%E5%B7%A5%E7%A8%8B%E5%8B%98%E5%AF%9F%E8%A7%84%E8%8C%83.pdf) |
| 1:500 1:1000 1:2000数字地形测绘标准 | - | 2022-01-05 | 沪建标定〔2022〕14号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=645fb9ada53644db81a3a448fa06c0b3&siteId=0011) | - |
| 地面沉降监测与防治技术标准 | DG/TJ08-2051-2008 | 2021-05-31 | 沪建标定〔2021〕338号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ca4fd6c81e7549fe822a5055ac63bdd7&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/212%E5%9C%B0%E9%9D%A2%E6%B2%89%E9%99%8D%E7%9B%91%E6%B5%8B%E4%B8%8E%E9%98%B2%E6%B2%BB%E6%8A%80%E6%9C%AF%E8%A7%84%E7%A8%8B.pdf) |
| 地质信息数据标准 | DG/TJ08-2320-2020 | 2020-07-08 | 沪建标定〔2020〕258 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200708/e4a76121d7824a659eccd4545e0e7cd9.html) | [PDF](https://zjw.sh.gov.cn/cmsres/f9/f963ce96be434c2196b8654d819c4fa6/beec998da519f60aab8c8cc73dbfe4e1.pdf) |
| 城市工程测量标准 | DG/TJ08-2312-2019 | 2020-03-10 | 沪建标定〔2020〕63 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200310/084014b8b64d49978d76e0f863078f48.html) | [PDF](https://zjw.sh.gov.cn/cmsres/82/82d3d8fd811a4ee195da678355223bf5/8b32929ce131dedb78dfa53d28b234d1.pdf) |
| 岩土工程信息模型技术标准 | DG/TJ08-2278-2018 | 2019-01-14 | 沪建标定〔2018〕682 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20190114/0011-56130.html) | [PDF](https://zjw.sh.gov.cn/cmsres/29/297314a54fa043dcb7c20205a197463a/376a723491ddf3d86831b3a28f6b1abc.pdf) |

### 施工与质量安全（14）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 建设工程数智化检测技术标准 | - | 2025-07-23 | 沪建标定〔2025〕377号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=748528bc4b20420db032606a81f08513&siteId=0011) | - |
| 扣件式钢管模板垂直支撑系统安全技术标准 | - | 2025-05-30 | 沪建标定〔2025〕286号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=64d2d64241df4bf2a2691daa43a21c9f&siteId=0011) | - |
| 建设工程检测管理标准 | DG/TJ08-2042-2008 | 2025-01-17 | 沪建标定〔2025〕34号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=011db43d49bf4d17b92c641a6da45aad&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/205%E5%BB%BA%E8%AE%BE%E5%B7%A5%E7%A8%8B%E6%A3%80%E6%B5%8B%E7%AE%A1%E7%90%86%E8%A7%84%E7%A8%8B.pdf) |
| 沉井与沉箱施工技术标准 | - | 2023-08-04 | 沪建标定〔2023〕403号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=37827d03d1b3484f981cf7e028469472&siteId=0011) | - |
| 上海市建设工程施工图无障碍设计文件技术审查要点 | - | 2023-07-03 | 沪建质安〔2023〕312 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20230703/6850041267f7448585db4694e1a05933.html) | [PDF](https://zjw.sh.gov.cn/cmsres/13/130fa280a78b4d6984e10f6d198fa77a/9b2bceb8866d815dd1c382c5716c5854.docx) |
| 市域铁路工程施工质量验收标准 | - | 2023-06-01 | 沪建标定〔2023〕273号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=d435044bf15e46d88faa23443a3917f2&siteId=0011) | - |
| 建设工程招标代理标准 | DG/TJ08-2072-2022 | 2023-01-17 | 沪建标定〔2023〕35号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=55500a111b5c45c3a86a2386f171f848&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/bd/bdca8778320a4ab1a6ffac57eb340476/a1807ba4fa2c9348b46dfc0f817ab7ac.pdf) |
| 现场施工安全生产管理标准 | DG/TJ08-903-2022 | 2022-06-23 | 沪建标定〔2022〕271号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=0eee73cc110243218b5908d37bac51d5&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/de/dedfb141a3804c2d942fd487e343acf1/71c108c10de97ce0cfd91b660d19f43f.pdf) |
| 危险性较大的分部分项工程安全管理标准 | DG/TJ 082077-2021 | 2021-10-09 | 沪建标定〔2021〕630号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e47f529ad7154cf9a7db057d4df5593f&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/f5/f52e44bb77924a0c8f88f1d36643a468/23875c19f24a5a662e7c7cda4a756893.pdf) |
| 假山叠石工程施工标准 | DG/TJ08-211-2020 | 2021-06-28 | 沪建标定〔2021〕81 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/e9c6b59bb8c9436ea6c8b6843f7ed016.html) | [PDF](https://zjw.sh.gov.cn/cmsres/e8/e88dc61af5674aeeb61c01738fe3f12e/8a4bf276738f5043a000fdabbecc2c41.pdf) |
| 逆作法施工技术标准 | DG/TJ08-2113-2021 | 2021-04-15 | 沪建标定〔2021〕222 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210415/fac91705cf624165b3f2d47c5e8bd11f.html) | [PDF](https://zjw.sh.gov.cn/cmsres/ec/ec3fdfcbf8b64042beab960de2ebc34b/684de3a6b5bec2bb3db53bf0d5e3be55.pdf) |
| 建设工程班组安全管理标准 | DG/TJ08-2061-2020 | 2020-10-29 | 沪建标定〔2020〕380 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20201029/a6e22588c53a4dddbf98c0a27497d5a7.html) | [PDF](https://zjw.sh.gov.cn/cmsres/7f/7fca92d1436642169401d5c45d3eb32d/b79c579d40eadfa4baf203ba30973e2d.pdf) |
| 建设工程班组安全管理标准 | DG/TJ08-2061-2020 | 2020-09-11 | 沪建标定〔2020〕380 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200911/70473a9068d84bf8a8d911afbd296d49.html) | [PDF](https://zjw.sh.gov.cn/cmsres/7f/7fca92d1436642169401d5c45d3eb32d/b79c579d40eadfa4baf203ba30973e2d.pdf) |
| 建设工程造价指标指数分析标准 | DG/TJ08-2135-2020 | 2020-04-13 | 沪建标定〔2020〕143 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200413/8b5c152900d4410fb7f54437f2456ca4.html) | [PDF](https://zjw.sh.gov.cn/cmsres/a9/a9b6b6fde2774dd0bfa2d222d163ebfc/ba147f0cea9ae1aafd38f380312b9f86.pdf) |

### 规划与不动产（18）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 上海市不动产登记技术规定 | - | 2026-02-14 | 沪规划资源规〔2026〕1号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=db31db6e49e0416583d048531bfa5c8e&siteId=0032) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/26/2612779d7807474e863cebb9b8a8360f/86a4b2e6247b58a2ee94c1bda35f9723.pdf&filename=%E9%99%84%E4%BB%B6%EF%BC%9A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%B8%8D%E5%8A%A8%E4%BA%A7%E7%99%BB%E8%AE%B0%E6%8A%80%E6%9C%AF%E8%A7%84%E5%AE%9A%EF%BC%882026%E7%89%88%EF%BC%89.pdf) |
| 公共厕所规划和设计标准 | DG/TJ08-401-2016 | 2025-08-28 | 沪建标定〔2025〕425号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=933ad6164d924b83a0c7b10f82ebed07&siteId=0011) | [PDF](https://zjw.sh.gov.cn/cmsres/15/15d1e30fce6a486da09b453aaac2fcff/6c31d4056b2d72cfa98694f1db100a70.pdf) |
| 上海市城市规划管理技术规定（土地使用 建筑管理）应用解释 | - | 2025-04-16 | 沪规划资源建〔2025〕131号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=72d2cd5662b54f14b2375a5e984867a3&siteId=0032) | - |
| 国土空间综合整治工程技术标准 | - | 2025-04-08 | 沪建标定〔2025〕200号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=59617b927b2a484ebabdf255710eb9aa&siteId=0011) | - |
| 集体土地所有权调查技术标准 | DG/TJ08-2120-2013 | 2025-03-11 | 沪建标定〔2025〕146号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e31199f39a7b471ea10c5b14417fe37a&siteId=0011) | [PDF](https://zjw.sh.gov.cn/shsd/userfiles/315%E9%9B%86%E4%BD%93%E5%9C%9F%E5%9C%B0%E6%89%80%E6%9C%89%E6%9D%83%E8%B0%83%E6%9F%A5%E6%8A%80%E6%9C%AF%E8%A7%84%E8%8C%83.pdf) |
| 城市地理实体信息智能采集与建库技术标准 | - | 2025-03-05 | 沪建标定〔2025〕134号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=360e1daeb299470bb4ccd8559a4ca291&siteId=0011) | - |
| 上海市出让农村集体经营性建设用地使用权不动产登记技术规定（试行） | - | 2024-12-20 | 沪规划资源规〔2024〕6号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=01952fcd120c41bdbcd0e21fb73d31e8&siteId=0032) | - |
| 上海市城市规划管理技术规定（土地使用 建筑管理）应用解释 | - | 2024-10-23 | - | [发布页](https://ghzyj.sh.gov.cn/zcwj/cxgh/20241023/e84deddfcf674440b2c8b10f2393334f.html) | [PDF](https://ghzyj.sh.gov.cn/cmsres/77/7787afe47a05413abbfce95d0bb6e259/3fe8c445260a67090d47ac2f46ab65ab.pdf) |
| 国土空间生态修复基底调查技术标准 | - | 2024-04-30 | 沪建标定〔2024〕215号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=3e062e0cad274a8cbe0487f0c3ed6544&siteId=0011) | - |
| 节约集约建设用地标准 | - | 2023-03-08 | 沪建标定〔2023〕115号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=e437541c8b1343a08f6f03bd87d3a6d1&siteId=0011) | - |
| 关于购买共有产权保障住房（经济适用住房）满五年后续相关不动产登记技术规定 | - | 2022-12-28 | 沪规划资源规〔2022〕11号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=5f56ede00285413e99f9ad01a83460ac&siteId=0032) | - |
| 城市设计编制标准 | - | 2022-02-15 | 沪建标定〔2022〕102号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=ad47e85f65644482bb0d1cbdb8cd4d66&siteId=0011) | - |
| 上海市不动产登记技术规定的补充规定 | - | 2022-01-07 | - | [发布页](https://ghzyj.sh.gov.cn/zcwj/gfxwj/20220107/0afaa89697f541cebdc8c2c852e04475.html) | [PDF](https://ghzyj.sh.gov.cn/cmsres/a8/a81bb04f0a474ad0bc4a3d414ad2192d/6cc99ff857ba8c7d2677a4efa7564416.pdf) |
| 国土分类标准 | - | 2021-12-28 | 沪建标定〔2021〕850号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=4d5c3c361386464191c9acb35d8a4104&siteId=0011) | - |
| 上海市乡村社区生活圈规划导则（试行） | - | 2021-12-03 | 沪规划资源乡〔2021〕450号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=fde7d67b4de740bf8a67d67669888854&siteId=0032) | [PDF](https://www.shanghai.gov.cn/gwk/resource/file?pathname=2/0032/9f/9fbe541329104f02bee5f0b8c99c9d34/a0989ebc12f4f574f711fd10e9acdd88.pdf&filename=%E3%80%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E4%B9%A1%E6%9D%91%E7%A4%BE%E5%8C%BA%E7%94%9F%E6%B4%BB%E5%9C%88%E8%A7%84%E5%88%92%E5%AF%BC%E5%88%99%EF%BC%88%E8%AF%95%E8%A1%8C%EF%BC%89%E3%80%8B.pdf) |
| 土地整治生态工程规划设计标准 | DG/TJ08-2344-2020 | 2021-06-28 | 沪建标定〔2021〕4 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20210628/ec95aeb9cf904a3592a1dc83ba6fb702.html) | [PDF](https://zjw.sh.gov.cn/cmsres/01/0156735585c24218ad18769dc8d048a6/49d83f610372c1529f7e84fa06184e9b.pdf) |
| 上海市租赁住房规划建设导则 | - | 2020-12-08 | 沪建房管联〔2020〕483 号 | [发布页](https://zjw.sh.gov.cn/fwgl/20201208/33161ea39a58430ab4e88cfd935ee07b.html) | [PDF](https://zjw.sh.gov.cn/cmsres/d8/d80fda9aa2d7425daa9febb1d37223dc/ed807ad160205b9b9e196edf38f5bf7f.docx) |
| 土地整治项目工程质量验收规范 | DG/TJ08-2317-2020 | 2020-04-13 | 沪建标定〔2020〕146 号 | [发布页](https://zjw.sh.gov.cn/jsgl/20200413/6c5088441b164a69a8b18657f98023b7.html) | [PDF](https://zjw.sh.gov.cn/cmsres/1f/1ffa761689d147e785120d14ca80aa6a/6882c843d51aee1d613233ff51024402.pdf) |

### 其他（3）

| 标准名 | 编号 | 批准日期 | 文号 | 批准通知 | 全文 |
|---|---|---|---|---|---|
| 上海市建设工程采用尚无国家技术标准的新技术、新材料技术论证管理办法 | - | 2024-09 | - | [发布页](https://zjw.sh.gov.cn/gfxwj/20240926/a224c3deb44b4721ace63e6a10a1382e.html) | - |
| 黄浦江两岸滨江公共空间建设标准 | - | 2023-01-31 | 沪建标定〔2023〕56号 | [发布页](https://www.shanghai.gov.cn/zhengce/detail?businessId=5dc2b0a0a94549c0bbf7119efcb6eac7&siteId=0011) | - |
| 上海市建设工程采用尚无国家技术标准的新技术、新材料技术论证管理办法 | - | 2020-11 | - | [发布页](https://zjw.sh.gov.cn/gfxwj/20201110/fed36604a9c041e5893e34136f12ceac.html) | - |

</details>

---

## 六、官方免费查阅渠道

| 渠道 | 网址 | 覆盖范围 | 能否下载 |
|---|---|---|---|
| 国家标准全文公开系统 | https://openstd.samr.gov.cn/bzgk/gb/ | 国标（不含工程/食品/环保） | 2025-02 起开放 3 万余项在线阅读+下载 |
| 全国标准信息公共服务平台 | https://std.samr.gov.cn/ | 国标/行标/地标/团标题录 | 部分可在线读 |
| 住房和城乡建设部 | https://www.mohurd.gov.cn/ | **工程建设标准（含 38 本强规）** | ✅ 强规可免费下载 PDF |
| 国家工程建设标准化信息网 | https://www.ccsn.org.cn/ | 工程建设国标 + 行标 | 依标准而定 |
| 上海市住房和城乡建设管理委员会 | https://zjw.sh.gov.cn/xxbz/index.html | **上海工程建设规范（DGJ08 / DG/TJ08）** | ✅ 现行标准栏目提供全文 PDF 直链 |
| 上海市统一政策发布平台 | https://www.shanghai.gov.cn/zhengce/list | **市/区/街镇三级政府发文**（非标准） | ✅ 原文可下载 |

> 提醒：官方提供免费下载 ≠ 你可以再分发。免费下载解决的是「获取」问题，
> 不解决「传播」问题。二者的法律边界在《著作权法》第 10 条。

---

## 七、目录结构

仓库只跟踪**数据源 + 生成器 + 说明书**。由脚本产出的内容一律不入库，
克隆后跑一次 `build_index.py` 即可完整重建 —— 这样仓库里永远不会出现
「数据源改了、产物忘了重新生成」的不一致状态。

```
Arch-Standards-Index/
├── README.md                  本文件（脚本生成；入库，作仓库首页）
├── LICENSE                    双许可：脚本 MIT / 数据 CC BY 4.0
├── .gitattributes             换行符策略（仓库内统一 LF）
├── .gitignore                 生成产物排除规则
├── build_index.py             索引生成器（零第三方依赖）
├── build_sh_local.py          上海工程建设规范：提取 + 链接验证（零第三方依赖）
├── build_sh_notices.py        规范批准通知索引：从 gov_docs.csv 抽取 + 补编号（零第三方依赖）
├── check_links.py             官方链接巡检工具（零第三方依赖）
├── data/
│   ├── standards.csv          ★ 数据源一：国标 / 行标（手工维护）
│   ├── sh_std_raw.json        上海住建委官网原始抓取结果（489 条，只读缓存）
│   ├── sh_local.tsv           ★ 数据源二：上海工程建设规范（由脚本生成）
│   └── sh_notices.tsv         ★ 数据源三：规范批准 / 发布通知（由脚本生成）
└── 〔以下为生成产物，不入库，跑脚本即重建〕
    ├── data/standards_excel.csv   Excel 友好版（UTF-8 BOM）
    ├── data/sh_notices_excel.csv  批准通知 Excel 版（UTF-8 BOM，列结构不同于标准表）
    └── obsidian/
        ├── 标准索引.md             Obsidian 主索引页
        └── standards/              每条标准一个笔记（143 个）
```

> README 本身也是脚本产物，但它被特意保留入库 —— GitHub 打开仓库即渲染它，
> 访客无需运行任何脚本就能看到完整索引表。

---

## 八、怎么用

### 克隆本仓库

```bash
git clone https://github.com/zhiyao87/Arch-Standards-Index.git
cd Arch-Standards-Index
```

### 重建生成产物

`obsidian/` 与 `data/standards_excel.csv` 不入库，克隆后跑一次生成器即可：

```bash
python build_index.py     # 零依赖，标准库即可，约 1 秒跑完
```

> 想建自己的副本？fork 本仓库，或本地 `git init` 后推到你自己的仓库。
> 记得把 `build_index.py` 顶部的 `TITLE` 与 `REPO` 两个常量改成你的仓库名，
> 否则下次生成 README 时标题和 clone 地址会被写回本仓库的值。

### 日常维护

三个数据源，各改各的，改完跑一次生成器即可：

```bash
python build_sh_local.py --verify   # ① 上海现行规范：重新抓取 + 验证链接（可选）
python build_sh_notices.py --src <gov_docs.csv 路径>   # ② 批准通知：重新抽取（可选）
python build_index.py               # ③ 合并三个源，生成全部产物
```

| 数据源 | 维护方式 |
|---|---|
| `data/standards.csv` | 国标 / 行标，手工编辑后跑 `build_index.py` |
| `data/sh_local.tsv` | 上海工程建设规范，由 `build_sh_local.py` 从官网生成，**不要手改** |
| `data/sh_notices.tsv` | 规范批准 / 发布通知，由 `build_sh_notices.py` 从 `gov_docs.csv`（配套仓库）生成，**不要手改** |

三处产出（README 表格 / Obsidian 笔记 / Excel CSV）会自动保持同步。

### 定期巡检链接

政府网站改版频繁，链接会静默失效（返回 404 但没人发现）。
`check_links.py` 逐个访问并检查页面内容是否确实对应该标准：

```bash
python check_links.py              # 巡检全部 143 条
python check_links.py --limit 10   # 快速自检
python check_links.py --strict     # 把「可疑」也视为失败，人工复核用
python check_links.py --json out.json
```

退出码：**只有存在真正失效的链接才返回 1**，可直接接进 CI。
「可疑」（返回 200 但内容不匹配）默认不判失败 —— 本库有若干条目因原公告页已从住建部
CMS 移除而有意降级为栏目入口，属预期状态，不该让 CI 变红。要严查时加 `--strict`。

```yaml
# .github/workflows/link-check.yml
on:
  schedule: [{cron: '0 1 * * 1'}]   # 每周一 09:00 (UTC+8)
  workflow_dispatch:
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python check_links.py
```

> 巡检判定口径：**仅返回 200 不算通过**，还要求页面标题或正文确实含该标准编号/名称。
> 那种「200 但跳到栏目首页」的链接对使用者没有价值，会被标为「可疑」单独列出。

### 作为 Obsidian 笔记库

先跑一次 `python build_index.py` 生成 `obsidian/`，再把该目录整体复制进 vault，即可获得：

- 每条标准一个笔记，带 YAML frontmatter，可按标签 / 属性筛选
- `标准索引.md` 作为入口页
- 笔记里留有「个人笔记」区，可随手记录项目上的使用经验

> 直接把 `obsidian/standards/` 拖进 vault 根目录也可以，笔记之间靠标签关联。

---

## 九、数据来源与核实方法

| 字段 | 来源 | 核实方式 |
|---|---|---|
| 编号、名称（国标 / 行标） | 住建部发布公告 / 国标委公告 | 官方公告原文 |
| 编号、名称（上海） | 上海市住建委「现行标准」栏目 | 栏目内嵌数据，由 `build_sh_local.py` 解析 |
| 实施日期 | 发布公告 / 上海栏目 | 公告正文；同日批次发布的标准实施日期通常一致 |
| 现行/废止 | 最新公告的废止清单 | 新强规实施时会在公告中列明废止的标准与条文 |
| 官方链接 | 住建部官网发布页 / 上海市住建委官网 | 见下节；全部链接已逐条联网验证 |
| 批准 / 发布通知（上海） | 配套仓库 Shanghai-Gov-Docs-Index 的 `gov_docs.csv` | 由 `build_sh_notices.py` 抽取；编号与全文 PDF 用 `sh_std_raw.json` 按名称回填 |

**上海数据的抓取方式**：上海市住建委「现行标准」栏目（`zjw.sh.gov.cn/xxbz/`）
的列表由前端渲染，页面内嵌完整 JSON 数据（字段 `bh` 编号 / `mc` 名称 / `pz` 批准 /
`ss` 实施 / `url` 全文 PDF）。`build_sh_local.py` 直接解析该数据，
无需逐条翻页，也不会因页面改版而失效得太突然。原始抓取结果存于
`data/sh_std_raw.json`（489 条），从中挑选建筑设计常用条目生成 `data/sh_local.tsv`。

> ⚠️ **该栏目名为「现行标准」，但实测混有新老版本**（例如《住宅设计标准》同时存在
> DGJ08-20-2019 的两条记录、《建筑抗震设计规程》DGJ08-9-2013 与其替代者
> DG/TJ08-9-2023 并存）。本库只收录**实施日期最新**的版本，
> 引用前请仍以官方公告为准。

**批准通知的抽取方式**：`build_sh_notices.py` 从配套仓库的 `gov_docs.csv` 里
按标题模式挑出规范类发文（`批准《X》为上海市工程建设规范` / `发布《X导则》` /
`印发《X技术规定》`），再用 `sh_std_raw.json` 按名称回填编号与全文 PDF。
名称比对会先去掉标点与「上海市」前缀、再去掉尾部的「标准 / 规范 / 导则」，
因此《上海市住宅设计标准》与《住宅设计标准》能对上。
**约 42% 能对上编号** —— 对不上的多半是 2026 年新批准、栏目尚未更新的，
这正是第五节存在的意义。

**已知待核实项**：GB 55033-2022《城市轨道交通工程项目规范》的实施日期在公开资料中未获确证，
表中留空。GB 55026/55027 的实施日期按住建部同期公告批次整理，正式的引用前请以官方公告为准。

**一个重要提示**：工程建设标准体系处于持续重构期（全文强制性规范替代分散强条），
标准之间的废止/替代关系比标准本身更容易出错。用于正式设计文件前，
请在国家工程建设标准化信息网核对最新状态。

---

## 十、关于官方链接：一次真实的链接失效排查

本仓库的官方链接全部指向住建部官网的**标准发布公告页**（公告页附标准全文 PDF）。
初次建库时曾指向「国家标准全文公开系统」，后经核查发现该系统**不收录工程建设类标准**：

```
openstd 站内检索  GB 5749  →  count = 1   ✓ 收录（非工程建设类）
openstd 站内检索  GB 50352 →  count = 0   ✗ 不收录（工程建设类）
openstd 站内检索  GB 50016 →  count = 0   ✗ 不收录（工程建设类）
```

> 住房和城乡建设部主管的工程建设标准，与市场监管总局主管的一般国家标准走的是两套体系。
> 全文公开系统的排除范围里明确包含工程建设类。

### 住建部 CMS 改版后的 URL 规律

住建部官网在 2024 年前后更换了内容管理系统，**文档 ID 不变、路径前缀全变**：

```
旧（2024 年前，现全部 404）
  /gongkai/zhengce/zhengcefilelib/{YYYYMM}/{YYYYMMDD}_{文档ID}.html

新（现行有效）
  /gongkai/zc/wjk/art/{YYYY}/art_17339_{文档ID}.html
```

其中 `{YYYY}` 取旧路径前四位，栏目前缀固定为 `art_17339_`。
**知道文档 ID 就能拼出新链接** —— 文档 ID 在第三方转载页的「来源」一行里往往还留着旧格式 URL。

### 两条容易搞错的事实

**1. 部分标准在 2024 年局部修订时改了编号和名称**（强制性 GB → 推荐性 GB/T）：

| 原编号 / 名称 | 现编号 / 名称 | 生效 | 依据 |
|---|---|---|---|
| GB 50011-2010《建筑抗震设计规范》 | **GB/T 50011-2010《建筑抗震设计标准》** | 2024-08-01 | 住建部公告 2024 年第 61 号 |
| GB 50010-2010《混凝土结构设计规范》 | **GB/T 50010-2010《混凝土结构设计标准》** | 2024-08-01 | 住建部公告 2024 年第 62 号 |

**2. 本站不用「某某标准 2024 版」这类传言做数据源。**
排查过程中遇到网上流传的「GB 50974-2024《消防给水及消火栓系统技术规范》」，
经核对住建部官方公告**并无此标准**（GB 50974-2014 现行有效），未予采信。

### 尚缺深链的条目

有 8 条标准的原发布公告页在住建部现行 CMS 中检索不到（多为 2010 年前后发布、
公告未随改版迁移）。这些条目的链接降级为住建部文件库栏目入口，
并在「备注」列注明原因。**宁可给栏目入口，也不给一条点进去 404 的假链接。**

---

## 十一、配套仓库：上海建设工程政府发文索引

技术标准之外，施工图设计还有一层依据是**政府发文**——规划管理技术规定、
施工图审查办法、抗震设防审查办法、消防设计审查验收办法、既有建筑装饰装修管理规定等。
这类文件不属于本仓库范围（本仓库只管标准），单独建了一个配套仓库：

### [zhiyao87/Shanghai-Gov-Docs-Index](https://github.com/zhiyao87/Shanghai-Gov-Docs-Index)

| 项目 | 情况 |
|---|---|
| 收录范围 | 上海市 **建筑、规划、工程建设** 领域的政府规章与行政规范性文件 |
| 数据源 | 市政府规章库 + 市住建委规范性文件 + 上海市统一政策发布平台（市/区/街镇三级）+ 国家法律法规数据库（上海市地方性法规） |
| 规模 | 2,600+ 条（含市/区/街镇三级 + 地方性法规），覆盖上海 16 个区 |
| 正文 | **收录全文**（有实质约束力的文件），另附官方链接；核心文件还附**红头文件 PDF / 附表附图**原件直链 |
| 时间跨度 | 1985 – 2026 |
| 主题速查 | 屋顶绿化 / 立体绿化、屋顶分布式光伏 / BIPV、建筑光伏 / 太阳能、绿色建筑 / 节能、海绵城市、既有建筑改造 —— 六大主题按正文全文检索归类 |

### 两个仓库的版权处理为什么不一样

| | 本仓库（标准） | 配套仓库（政府发文） |
|---|---|---|
| 文件性质 | 技术标准（推荐性为主） | 具有立法、行政性质的文件 |
| 著作权法适用 | **适用**，受保护 | **不适用**（第 5 条第（一）项） |
| 因此的处理 | 只存索引，不存正文 | **可全文收录** |

同一套「只给链接 vs 给全文」的判断，差别不在保守程度，而在法律性质。
政府规章和行政规范性文件依《著作权法》第 5 条第（一）项被排除在保护范围之外，
收录正文不构成侵权；而 JGJ、DGJ08、GB/T 这类推荐性技术标准仍是受保护作品。

> 与上海市住建委「规范性文件」栏目的区别：该栏目是**发布渠道**，
> 配套仓库是**按设计报建主题重组的索引**，并额外覆盖了区级、街镇级发文。

### 两个仓库之间的数据流

本节第五节那 369 条批准 / 发布通知，正是从配套仓库的 `gov_docs.csv` 里
抽出来的 —— 由 `build_sh_notices.py` 按标题模式筛出规范类发文，
再用本仓库的 `sh_std_raw.json` 回填编号与全文 PDF。
两个仓库因此形成闭环：**配套仓库负责把文件抓全，本仓库负责把标准理顺**。

所以想查某本规范的**批准文号或通知原件**，去配套仓库按标题搜；
想查它**是否有全文 PDF、编号是多少**，看本仓库第四节与第五节。

---

## 许可证

- 本仓库的**元数据与索引内容**（标准编号、名称、链接等事实性信息）：CC BY 4.0
- **生成脚本** `build_index.py`：MIT
- **标准正文**：不在本仓库范围内，版权归各自权利人所有
