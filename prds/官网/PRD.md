# 素灵AI 官网 PRD

> **文档版本**：v1.0  
> **创建日期**：2026-07-01  
> **状态**：待评审  
> **关联文档**：[信息架构规划](./素灵ai官网信息架构_abe92dc7.plan.md) · [冯老师实施计划](./素灵官网PLAN_冯老师.md) · [首页原型](./原型/素灵AI官网-首页.html)

---

## 1. 背景与目标

### 1.1 背景

用户在百度搜索「素灵AI」及相关关键词时，无法找到品牌官方站点，流量被百度及第三方页面截留，导致：

- 品牌无法建立官方认知入口
- 用户难以找到微信小程序与工具体验路径
- AI 引擎缺乏可引用的结构化品牌信息（GEO 缺失）

### 1.2 产品目标

| 目标 | 衡量指标 | MVP 目标值 |
|------|----------|------------|
| 品牌官方入口 | 百度「素灵AI」品牌词自然排名第一 | 上线 30 天内收录并首位 |
| 用户转化 | 二维码曝光→扫码 / 工具 CTA 点击率 | 基线建立，首月 PV→CTA ≥ 15% |
| GEO 可见性 | AI 引擎回答「素灵AI 是什么」时引用官网信息 | 上线 60 天内 ≥ 2 个主流 AI 平台正确引用 |
| 专业信任 | 用户停留时长、FAQ 展开率 | 平均停留 ≥ 45s |

### 1.3 产品定位

- **品牌**：素灵AI（C 端产品品牌）
- **Slogan**：以人工智能重构中医科技
- **背书**：成都青羊榕树家互联网医院（机构化表达，弱化个人医生）
- **形态**：响应式官网（PC + 移动端），首页长滚动 + SEO 独立子页

### 1.4 不在范围内

- 后端 API、用户登录、在线支付
- 官网内嵌真实问诊/开方功能
- 融资、估值、营收、商业模式、市场规模等商业计划内容
- 个人医生头像/姓名/「专家坐诊」类营销

---

## 2. 目标用户与场景

### 2.1 用户画像

| 用户类型 | 来源 | 核心诉求 |
|----------|------|----------|
| 品牌搜索用户 | 百度大搜「素灵AI」 | 确认品牌真实性、找到官方入口 |
| 功能搜索用户 | 「素灵AI 舌诊」「AI 中医」 | 了解功能、快速体验 |
| AI 对话用户 | DeepSeek/Kimi/ChatGPT 等 | 通过 AI 回答了解品牌后访问官网 |
| 专业关注者 | 行业/技术关键词 | 了解中医 AI 技术能力 |

### 2.2 核心场景

1. **场景 A：品牌确认** — 用户搜「素灵AI 是什么」→ 进入官网 → 阅读实体定义 + 合规背书 → 扫码进小程序
2. **场景 B：工具体验** — 用户搜「素灵AI 舌诊」→ 进入工具详情页 → 点击体验 → 跳转 H5/小程序
3. **场景 C：信任建立** — 用户浏览技术底座/诊疗流程 → 阅读 FAQ → 消除安全疑虑 → 转化
4. **场景 D：AI 引用** — AI 引擎抓取官网结构化数据 → 在对话中引用品牌定义与能力描述

---

## 3. 信息架构

### 3.1 站点地图

```
/                     首页（长滚动，10 模块）
├── #tech             技术底座
├── #pipeline         多模态诊疗流程
├── #agent            专家智能体
├── #health           全周期健康算法
├── #tools            工具体验入口
├── #compliance       合规安全
└── #faq              FAQ 精选

/faq                  完整 FAQ 页
/tools                产品体验目录
/tools/tongue-diagnosis   AI 舌诊详情
/tools/health-agent       AI 健康问诊详情
/about                关于素灵AI
/privacy              隐私政策
/terms                用户协议
```

### 3.2 全局导航

| 导航项 | 类型 | 说明 |
|--------|------|------|
| 技术底座 | 锚点 | 滚动至 #tech |
| 诊疗流程 | 锚点 | 滚动至 #pipeline |
| 产品体验 | 锚点 | 滚动至 #tools |
| 合规安全 | 锚点 | 滚动至 #compliance |
| 常见问题 | 锚点/链接 | 首页 #faq 或 /faq |
| 微信体验 | CTA | PC 悬停二维码弹层；Mobile 跳转 #tools |

---

## 4. 功能需求

### 4.1 首页模块需求

#### F-01 Hero 首屏

| 字段 | 要求 |
|------|------|
| 主标题 | 以人工智能重构中医科技 |
| 副标题 | 素灵AI — 融合中医语义系统、知识图谱与多模态识别的智能健康平台 |
| 实体定义段 | 50–80 字，plain text，供 GEO 引用；见原型文案 |
| 主 CTA | 微信扫一扫 + 小程序二维码（≥ 160×160px） |
| 次 CTA | 「了解技术底座」「体验 AI 工具」 |
| 信任条 | 成都青羊榕树家互联网医院 · 卫健委备案 · 数据加密传输 |
| 视觉 | Three.js 全屏背景（正式版）；原型用 CSS 粒子背景占位 |
| 布局 | Desktop 左 60% 文 + 右 40% 码；Mobile 单列 |

**验收**：首屏 3 秒内可见品牌名、实体定义、二维码（Mobile 滚动 1 屏内）。

#### F-02 技术底座

4 张能力卡片，配置驱动：

| ID | 标题 | 描述 |
|----|------|------|
| tech-1 | 中医语义系统 | 面向中医领域的语义理解与术语标准化，支撑问诊、辨证等场景的结构化表达 |
| tech-2 | 中医知识图谱 | 融合经典理论与临床知识的关系网络，为 AI 推理提供可解释的知识基础 |
| tech-3 | 多模态识别 | 舌象图像、语音问诊、文本病历等多源信息的联合感知与分析 |
| tech-4 | 隐私计算与数据安全 | 健康数据加密传输与存储，遵循医疗数据合规要求 |

**布局**：Desktop 4 列；Tablet 2×2；Mobile 1 列。

#### F-03 多模态诊疗流程

5 步流程，强调第 5 步「医师复核」：

1. 舌象采集 → 2. 问诊语音转写 → 3. 病历信息抽取 → 4. 辨证辅助 → 5. 医师复核

**布局**：Desktop 横向步骤条；Mobile 纵向卡片。  
**Schema**：输出 HowTo JSON-LD。

#### F-04 专家智能体

- 标题：专家智能体 — 名医辨证思路的结构化沉淀
- 正文：结构化建模辨证逻辑、经验方义与临证要点；持续临床反馈校准
- **禁止**：具体医生头像/姓名/职称

#### F-05 全周期健康算法

4 项能力：体质辨识、慢病管理、随访调衡、治未病。

#### F-06 工具体验入口

| 工具 | CTA | 跳转 |
|------|-----|------|
| AI 舌诊 | 立即体验 | /tools/tongue-diagnosis 或 H5 深链 |
| AI 健康问诊 | 立即体验 | /tools/health-agent 或 H5 深链 |
| 更多工具 | 敬请期待 | 无链接（占位） |

带来源参数：`?from=official_site`

#### F-07 合规安全

必含 6 项：医师审核、诊疗留痕、数据安全、医疗合规、AI 边界声明、资质信息（含外链）。

#### F-08 关于素灵AI（摘要）

150 字内品牌介绍 + 「了解更多 →」链至 /about。

#### F-09 FAQ 精选

首页展示 6 条，`<dl>/<dt>/<dd>` 结构，可展开交互。完整版见 /faq。

#### F-10 Footer

导航链接、ICP 备案占位、版权、二维码二次曝光、隐私政策/用户协议。

### 4.2 子页面需求

| 页面 | 核心内容 | SEO Title |
|------|----------|-----------|
| /faq | 25–35 问，5 分类 | 素灵AI常见问题 - 是什么/怎么用/安全吗 \| 素灵AI |
| /tools | 工具目录 + 场景对比 | 产品体验 - AI中医健康工具 \| 素灵AI |
| /tools/tongue-diagnosis | 功能/步骤/注意/体验入口 | 素灵AI舌诊 - 多模态舌象AI分析 \| 素灵AI |
| /tools/health-agent | 功能/场景/合规/体验入口 | 素灵AI健康问诊 - 7×24 AI智能问诊 \| 素灵AI |
| /about | 品牌/关系链/技术/合规 | 关于素灵AI - AI中医科技品牌 \| 榕树家旗下 |
| /privacy | 数据收集/用途/权利 | — |
| /terms | 服务范围/免责/争议 | — |

### 4.3 交互需求

| ID | 交互 | 规则 |
|----|------|------|
| I-01 | 锚点平滑滚动 | 点击导航滚动至对应 section，offset 考虑 fixed header |
| I-02 | 微信体验 CTA | PC：hover 显示二维码 popover；Mobile：scroll 至二维码区 |
| I-03 | FAQ 展开/收起 | 点击 dt 切换 dd 可见性；支持键盘 Enter |
| I-04 | 滚动入场动画 | section 进入视口 fade-in；`prefers-reduced-motion` 时禁用 |
| I-05 | 移动端菜单 | < 768px 汉堡菜单展开/收起导航 |
| I-06 | Hero 背景 | Three.js 粒子/流体；降级为 CSS 静态渐变 |

---

## 5. GEO / SEO 需求

### 5.1 TDK 规范

**Description 公式**：`[痛点解决] + [核心功能] + [权威背书] + [行动号召]`

**首页示例**：
- Title：`素灵AI - 以人工智能重构中医科技 | AI舌诊·智能问诊`
- Description：`想了解 AI 中医健康服务但找不到官方入口？素灵AI 提供 AI 舌诊与智能问诊，由成都青羊榕树家互联网医院合规背书，微信扫码立即体验。`
- Keywords：`素灵AI, AI舌诊, 智能问诊, 中医AI, 素灵AI是什么`

### 5.2 结构化数据（JSON-LD）

| Schema | 页面 | 优先级 |
|--------|------|--------|
| Organization | 首页、/about | P0 |
| MedicalOrganization | 首页合规模块 | P0 |
| FAQPage | 首页 FAQ、/faq | P0 |
| HowTo | 诊疗流程模块 | P0 |
| SoftwareApplication | /tools/* | P0 |
| WebSite | 首页 | P1 |
| BreadcrumbList | 子页 | P1 |
| SpeakOnly | answer-capsule 段落 | P1 |

### 5.3 技术 SEO 文件

| 文件 | 要求 |
|------|------|
| robots.txt | Allow Baiduspider + 14+ AI 爬虫；声明 Sitemap |
| llms.txt | H1 + blockquote 实体定义 + 核心页面链接（≤ 12 条/类） |
| sitemap.xml | 全站 URL + lastmod |
| IndexNow | P1，内容更新时推送 |

### 5.4 性能指标

| 指标 | 目标 |
|------|------|
| LCP | < 2.5s |
| FID | < 100ms |
| CLS | < 0.1 |
| TTFB | < 0.8s |

### 5.5 内容写作规范

- 每模块 H2 下首段为 answer-capsule（40–60 字，首句直接回答）
- 首次出现专业术语即定义
- 禁止代词指代（「它」「上述」）
- 关键信息不全依赖图片（alt 必填）

---

## 6. 视觉与响应式规范

### 6.1 设计风格

- 参考 Apple / SpaceX 科技感：黑场、渐变发光、电路几何
- 主色：深空黑 `#0a0e17` + 科技青 `#00d4aa` + 渐变紫蓝
- 字体：系统字体栈（PingFang SC / -apple-system）
- Logo：抽象几何标识 + 「素灵AI」文字（暂无正式 Logo）

### 6.2 响应式断点

| 断点 | 宽度 | 布局 |
|------|------|------|
| Mobile | < 768px | 单列、汉堡菜单 |
| Tablet | 768–1279px | 双列卡片 |
| Desktop | ≥ 1280px | 多列网格、Hero 双栏 |

### 6.3 无障碍

- CTA 热区 ≥ 44×44px
- 色彩对比度 WCAG AA
- `prefers-reduced-motion` 动画降级
- 语义 HTML + aria-label

---

## 7. 技术方案

### 7.1 技术栈

- **框架**：React + Vite + TypeScript
- **渲染**：SSG（首页 + 子页静态生成）
- **动效**：Three.js（Hero 背景，可配置降级）
- **部署**：静态 CDN + HTTPS
- **数据**：前端配置驱动，无后端

### 7.2 配置数据结构

```typescript
interface SiteConfig {
  navItems: { label: string; href: string }[];
  hero: { title: string; subtitle: string; entityDefinition: string; trustBar: string };
  techPillars: { id: string; title: string; description: string; icon: string }[];
  diagnosisSteps: { step: number; title: string; description: string }[];
  agentSection: { title: string; body: string };
  healthAlgorithms: { title: string; description: string }[];
  tools: { id: string; title: string; description: string; href: string; status: 'live' | 'coming' }[];
  complianceItems: { title: string; description: string }[];
  faqItems: { question: string; answer: string }[];
  footer: { icp: string; links: { label: string; href: string }[] };
}
```

### 7.3 埋点（P1）

| 事件 | 参数 |
|------|------|
| page_view | page_path, device_type |
| qr_exposure | section（hero/footer/popover） |
| tool_click | tool_id, from=official_site |
| faq_expand | question_id |
| cta_click | cta_type（wechat/hero/tools） |

---

## 8. 验收标准

### 8.1 功能验收

- [ ] 首页 10 模块内容完整，与 PRD 文案一致
- [ ] PC / Tablet / Mobile 三断点布局正确，无横向滚动
- [ ] 锚点导航、FAQ 展开、Mobile 菜单交互正常
- [ ] 二维码在 Hero + Footer 双曝光
- [ ] 工具 CTA 携带 `from=official_site` 参数

### 8.2 内容验收

- [ ] 文案审计：无融资/估值/营收/商业模式等禁止内容
- [ ] 合规表达齐全：AI 辅助、医师复核、数据安全、诊疗留痕、AI 边界
- [ ] 无个人医生头像/姓名/「专家坐诊」

### 8.3 SEO/GEO 验收

- [ ] 每页独立 TDK
- [ ] JSON-LD 通过 Rich Results Test
- [ ] robots.txt + llms.txt + sitemap.xml 可访问
- [ ] 语义 HTML：main/section/dl/article 结构正确
- [ ] Lighthouse Performance ≥ 80，SEO ≥ 90

### 8.4 性能验收

- [ ] LCP < 2.5s（4G 模拟）
- [ ] Three.js 不阻塞 LCP；reduced-motion 降级可用
- [ ] 图片/二维码预留尺寸，CLS < 0.1

---

## 9. 里程碑

| 阶段 | 周期 | 交付物 |
|------|------|--------|
| M1 需求确认 | 第 1 周 | PRD 评审通过、原型确认 |
| M2 设计与开发 | 第 2–3 周 | 首页 + 子页开发、Schema 部署 |
| M3 SEO 配置 | 第 3 周 | TDK/robots/llms/sitemap、百度站长提交 |
| M4 上线验收 | 第 4 周 | 性能达标、收录验证、AI 引用首次抽检 |

---

## 10. 待确认项

| # | 事项 | 影响 |
|---|------|------|
| 1 | 正式 Logo / 品牌字体 | 视觉定稿 |
| 2 | 互联网医院资质编号、信用代码 | 合规模块 |
| 3 | 域名与 ICP 备案主体 | 上线 |
| 4 | 小程序正式名称与 AppID | 二维码生成 |
| 5 | H5 工具体验深链 URL | 工具 CTA |
| 6 | Three.js MVP 必做 or V1.1 | 开发排期 |
| 7 | 「200 万用户」等数据是否对外展示 | 文案定稿 |

---

## 附录 A：首页 FAQ 完整文案

| 问题 | 答案 |
|------|------|
| 素灵AI 是什么？ | 素灵AI 是面向消费者的 AI 中医健康产品品牌，基于中医语义系统与多模态识别技术，提供 AI 舌诊与智能问诊服务，由成都青羊榕树家互联网医院提供合规医疗资质背书。 |
| 素灵AI 的核心技术是什么？ | 素灵AI 以四大技术底座为支撑：中医语义系统、中医知识图谱、多模态识别、隐私计算与数据安全，为 AI 辅助诊疗提供可解释、合规的技术基础。 |
| 素灵AI 如何保证诊疗安全？ | 素灵AI 定位为 AI 辅助工具，关键诊疗环节保留执业医师复核，问诊、分析、复核全流程留痕，确保服务合规可追溯。 |
| 素灵AI 怎么用？ | 用户可通过微信扫描官网小程序二维码进入素灵AI，选择 AI 舌诊或 AI 健康问诊即可开始体验；也可通过官网工具体验入口访问。 |
| 素灵AI 和榕树家是什么关系？ | 素灵AI 是榕树家旗下的 AI 中医健康产品品牌，医疗服务与合规资质由成都青羊榕树家互联网医院提供。 |
| 使用素灵AI 安全吗？ | 素灵AI 对健康数据采用加密传输与存储，遵循医疗数据合规要求，不对外出售用户数据，详见官网隐私政策。 |

## 附录 B：参考文档

- [素灵ai官网信息架构规划](./素灵ai官网信息架构_abe92dc7.plan.md)
- [素灵官网PLAN_冯老师.md](./素灵官网PLAN_冯老师.md)
- [搜索结果过度页规划](../搜索结果过度页/搜索结果过度页规划-6b159a.md)
- 易研研究院《AI时代网站建设 GEO+SEO 标准规范蓝皮书》（2025年10月）
