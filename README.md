# 建筑设计规范索引

> 本仓库**只收录标准的元数据与官方查阅链接，不包含任何标准正文内容**。
> 所有标准文本请通过下方官方渠道获取。

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

按版权分层统计：

| 分层 | 含义 | 数量 |
|---|---|---|
| A | 不受著作权法保护（强制性国家标准） | 64 |
| B | 受著作权法保护（推荐性国家标准 GB/T） | 8 |
| C | 受著作权法保护（行业标准 JGJ、上海工程建设规范） | 71 |

数据来源：住房和城乡建设部官网发布公告、上海市住房和城乡建设管理委员会「现行标准」栏目，
以及实际施工图设计说明中的现行规范引用表。详见文末「数据来源与核实方法」。

> 本仓库不引用「国家标准全文公开系统」作为数据源 —— 该系统**不收录工程建设类标准**，
> 用它核对建筑国标会得到空结果。原因见第九节。

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

## 五、官方免费查阅渠道

| 渠道 | 网址 | 覆盖范围 | 能否下载 |
|---|---|---|---|
| 国家标准全文公开系统 | https://openstd.samr.gov.cn/bzgk/gb/ | 国标（不含工程/食品/环保） | 2025-02 起开放 3 万余项在线阅读+下载 |
| 全国标准信息公共服务平台 | https://std.samr.gov.cn/ | 国标/行标/地标/团标题录 | 部分可在线读 |
| 住房和城乡建设部 | https://www.mohurd.gov.cn/ | **工程建设标准（含 38 本强规）** | ✅ 强规可免费下载 PDF |
| 国家工程建设标准化信息网 | https://www.ccsn.org.cn/ | 工程建设国标 + 行标 | 依标准而定 |
| 上海市住房和城乡建设管理委员会 | https://zjw.sh.gov.cn/xxbz/index.html | **上海工程建设规范（DGJ08 / DG/TJ08）** | ✅ 现行标准栏目提供全文 PDF 直链 |

> 提醒：官方提供免费下载 ≠ 你可以再分发。免费下载解决的是「获取」问题，
> 不解决「传播」问题。二者的法律边界在《著作权法》第 10 条。

---

## 六、目录结构

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
├── check_links.py             官方链接巡检工具（零第三方依赖）
├── data/
│   ├── standards.csv          ★ 数据源一：国标 / 行标（手工维护）
│   ├── sh_std_raw.json        上海住建委官网原始抓取结果（489 条，只读缓存）
│   └── sh_local.tsv           ★ 数据源二：上海工程建设规范（由脚本生成）
└── 〔以下为生成产物，不入库，跑脚本即重建〕
    ├── data/standards_excel.csv   Excel 友好版（UTF-8 BOM）
    └── obsidian/
        ├── 标准索引.md             Obsidian 主索引页
        └── standards/              每条标准一个笔记（143 个）
```

> README 本身也是脚本产物，但它被特意保留入库 —— GitHub 打开仓库即渲染它，
> 访客无需运行任何脚本就能看到完整索引表。

---

## 七、怎么用

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

两个数据源，各改各的，改完跑一次生成器即可：

```bash
python build_sh_local.py --verify   # ① 上海数据：重新抓取 + 验证链接（可选）
python build_index.py               # ② 合并两个源，生成全部产物
```

| 数据源 | 维护方式 |
|---|---|
| `data/standards.csv` | 国标 / 行标，手工编辑后跑 `build_index.py` |
| `data/sh_local.tsv` | 上海工程建设规范，由 `build_sh_local.py` 从官网生成，**不要手改** |

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

## 八、数据来源与核实方法

| 字段 | 来源 | 核实方式 |
|---|---|---|
| 编号、名称（国标 / 行标） | 住建部发布公告 / 国标委公告 | 官方公告原文 |
| 编号、名称（上海） | 上海市住建委「现行标准」栏目 | 栏目内嵌数据，由 `build_sh_local.py` 解析 |
| 实施日期 | 发布公告 / 上海栏目 | 公告正文；同日批次发布的标准实施日期通常一致 |
| 现行/废止 | 最新公告的废止清单 | 新强规实施时会在公告中列明废止的标准与条文 |
| 官方链接 | 住建部官网发布页 / 上海市住建委官网 | 见下节；全部链接已逐条联网验证 |

**上海数据的抓取方式**：上海市住建委「现行标准」栏目（`zjw.sh.gov.cn/xxbz/`）
的列表由前端渲染，页面内嵌完整 JSON 数据（字段 `bh` 编号 / `mc` 名称 / `pz` 批准 /
`ss` 实施 / `url` 全文 PDF）。`build_sh_local.py` 直接解析该数据，
无需逐条翻页，也不会因页面改版而失效得太突然。原始抓取结果存于
`data/sh_std_raw.json`（489 条），从中挑选建筑设计常用条目生成 `data/sh_local.tsv`。

> ⚠️ **该栏目名为「现行标准」，但实测混有新老版本**（例如《住宅设计标准》同时存在
> DGJ08-20-2019 的两条记录、《建筑抗震设计规程》DGJ08-9-2013 与其替代者
> DG/TJ08-9-2023 并存）。本库只收录**实施日期最新**的版本，
> 引用前请仍以官方公告为准。

**已知待核实项**：GB 55033-2022《城市轨道交通工程项目规范》的实施日期在公开资料中未获确证，
表中留空。GB 55026/55027 的实施日期按住建部同期公告批次整理，正式的引用前请以官方公告为准。

**一个重要提示**：工程建设标准体系处于持续重构期（全文强制性规范替代分散强条），
标准之间的废止/替代关系比标准本身更容易出错。用于正式设计文件前，
请在国家工程建设标准化信息网核对最新状态。

---

## 九、关于官方链接：一次真实的链接失效排查

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

## 许可证

- 本仓库的**元数据与索引内容**（标准编号、名称、链接等事实性信息）：CC BY 4.0
- **生成脚本** `build_index.py`：MIT
- **标准正文**：不在本仓库范围内，版权归各自权利人所有
