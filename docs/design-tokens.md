# 素灵 AI Design Tokens

> 版本：1.0.0 · 来源：移动端 App 设计稿 + 用色规范  
> 结构：**Primitive（原始）→ Semantic（语义）→ Component（组件，可选）**

---

## 1. 架构说明

```
Primitive Token（原始值）
  color-primary-700: #6F8E6C
       ↓ 引用
Semantic Token（语义别名）
  color-bg-brand-subtle: var(--color-primary-100)
       ↓ 引用
Component Token（组件，禁止硬编码）
  --chat-bubble-user-bg: var(--color-bg-brand-subtle)
```

**命名规范**：`{分类}-{层级}`，如 `color-primary-500`、`spacing-16`、`radius-lg`。

**文件对应关系**：

| 文件 | 用途 |
|------|------|
| `src/theme/tokens.json` | W3C DTCG 标准 JSON，供构建工具 / Figma 同步 |
| `src/theme/vars.css` | 运行时 CSS 变量，组件直接引用 |
| `docs/design-tokens.md` | 人类可读说明文档 |

---

## 2. 品牌色 Brand

### Primitive

| Token | Light | Dark | 使用场景 |
|-------|-------|------|---------|
| `color-primary-900` | `#4A5F48` | `#AFC4AD` | 深色强调、报告结论区背景 |
| `color-primary-700` | `#6F8E6C` | `#8FB28C` | **次要主色**，品牌标识、专家解读标题 |
| `color-primary-500` | `#8DA789` | `#6F8E6C` | 用户聊天气泡、示例徽章 |
| `color-primary-200` | `#CFD7CE` | `#4A5F48` | 分割线、禁用态边框 |
| `color-primary-100` | `#E8F2E9` | `#2A3D28` | 医生卡片浅底、成功浅背景 |
| `color-primary-50`  | `#F3F8F3` | `#1E2A1D` | 页面局部渐变终点 |
| `color-accent-700`  | `#53A0A8` | `#7BB8BE` | **点缀色**，链接、数据高亮 |
| `color-accent-500`  | `#729A93` | `#53A0A8` | 渐变起点 |
| `color-accent-100`  | `#E6F4F1` | `#1A3335` | Hero 区渐变顶色 |
| `color-neutral-900` | `#1A1A1A` | `#F6F6F6` | 主 CTA 按钮、一级标题 |
| `color-neutral-800` | `#222222` | `#ECECEC` | **主要主色**（规范定义） |
| `gradient-brand-hero` | `#729A93 → #FBFEE5` | `#1A3335 → #1E2A1D` | 望诊/舌诊 Hero 背景 |

---

## 3. 中性色 Neutral

| Token | Light | Dark | 语义 |
|-------|-------|------|------|
| `color-neutral-700` | `#333333` | `#E0E0E0` | 正文/主要内容 |
| `color-neutral-600` | `#666666` | `#B0B0B0` | 正文/次要内容 |
| `color-neutral-500` | `#999999` | `#888888` | 次要说明、未选中 Tab |
| `color-neutral-400` | `#BDBDBD` | `#666666` | 输入框占位符 |
| `color-neutral-300` | `#D6D6D6` | `#444444` | 不重要内容 |
| `color-neutral-200` | `#ECECEC` | `#333333` | 按钮描边、分割线 |
| `color-neutral-100` | `#F6F6F6` | `#222222` | 次级表面、子卡片底 |
| `color-neutral-50`  | `#F7F8FA` | `#1A1A1A` | 页面背景 |
| `color-neutral-0`   | `#FFFFFF` | `#121212` | 卡片/气泡表面 |

---

## 4. 功能色 Functional

| Token | Light | Dark | 场景 |
|-------|-------|------|------|
| `color-success-500` | `#76A07B` | `#8FB28C` | 健康/正常、图表绿线 |
| `color-success-100` | `#E8F2E9` | `#1E2A1D` | 成功浅底 |
| `color-warning-500` | `#E5AF5D` | `#E5AF5D` | 关注项、图表橙线 |
| `color-warning-100` | `#FDF2E9` | `#3D2E1A` | 职称标签底（主任医师） |
| `color-warning-600` | `#D48344` | `#E5AF5D` | 职称标签文字 |
| `color-error-500`   | `#E98A83` | `#E98A83` | 异常指示、图表红线 |
| `color-error-100`   | `#FDEDEC` | `#3D1A18` | 错误浅底 |
| `color-info-500`    | `#7BA4E8` | `#7BA4E8` | 肾/肠数据条、信息态 |

---

## 5. 文字 Typography

### 字号 Primitive（px → rem，基准 16px）

| Token | 值 | 场景 |
|-------|-----|------|
| `font-size-32` | 32px / 2rem | 望诊 Hero 大标题 |
| `font-size-28` | 28px / 1.75rem | 模块页标题 |
| `font-size-24` | 24px / 1.5rem | 报告标题、姓名 |
| `font-size-20` | 20px / 1.25rem | 医生名、数据值 |
| `font-size-18` | 18px / 1.125rem | 区块标题、主按钮 |
| `font-size-16` | 16px / 1rem | 正文、导航标题 |
| `font-size-15` | 15px / 0.9375rem | 聊天气泡正文 |
| `font-size-14` | 14px / 0.875rem | 副标题、卡片标签 |
| `font-size-13` | 13px / 0.8125rem | Tag 文字 |
| `font-size-12` | 12px / 0.75rem | 辅助说明、时间戳 |

### 字重

| Token | 值 |
|-------|-----|
| `font-weight-regular` | 400 |
| `font-weight-medium`  | 500 |
| `font-weight-semibold`| 600 |
| `font-weight-bold`    | 700 |

### 行高

| Token | 值 | 场景 |
|-------|-----|------|
| `line-height-tight`   | 1.25 | 大标题 |
| `line-height-normal`  | 1.5  | 正文（默认） |
| `line-height-relaxed` | 1.6  | 长文报告 |

### 语义文字色

| Token | 引用 |
|-------|------|
| `color-text-primary`    | `color-neutral-900` |
| `color-text-secondary`  | `color-neutral-600` |
| `color-text-tertiary`   | `color-neutral-500` |
| `color-text-placeholder`| `color-neutral-400` |
| `color-text-inverse`    | `color-neutral-0` |
| `color-text-brand`      | `color-primary-700` |
| `color-text-link`       | `color-accent-700` |

---

## 6. 间距 Spacing（4px 基准）

| Token | 值 | 场景 |
|-------|-----|------|
| `spacing-4`  | 4px  | Tag 内间距、图标间隙 |
| `spacing-8`  | 8px  | 元素内小间距 |
| `spacing-12` | 12px | 气泡间距、子卡片 gap |
| `spacing-16` | 16px | 卡片内边距、页面水平边距（小） |
| `spacing-20` | 20px | 页面水平边距（标准） |
| `spacing-24` | 24px | 区块间距 |
| `spacing-32` | 32px | 大区块、Hero 下间距 |
| `spacing-56` | 56px | 主 CTA 按钮高度 |

### 语义间距

| Token | 引用 | 场景 |
|-------|------|------|
| `spacing-page-x`       | `spacing-20` | 页面左右边距 |
| `spacing-card-padding` | `spacing-16` | 卡片内边距 |
| `spacing-section-gap`  | `spacing-24` | 卡片之间 |
| `spacing-stack-sm`     | `spacing-8`  | 表单项内 |
| `spacing-stack-md`     | `spacing-16` | 段落间 |

---

## 7. 圆角 Radius

| Token | 值 | 场景 |
|-------|-----|------|
| `radius-4`   | 4px   | 小 Tag |
| `radius-6`   | 6px   | AI 助理 Tag |
| `radius-8`   | 8px   | 头像、小按钮 |
| `radius-12`  | 12px  | 聊天气泡、子卡片 |
| `radius-16`  | 16px  | 标准卡片 |
| `radius-24`  | 24px  | 大卡片、数据面板 |
| `radius-full`| 9999px | Pill 按钮、Segment |

### 语义

| Token | 引用 |
|-------|------|
| `radius-card`    | `radius-16` |
| `radius-card-lg` | `radius-24` |
| `radius-bubble`  | `radius-12` |
| `radius-button`  | `radius-full` |
| `radius-tag`     | `radius-6` |

---

## 8. 阴影 Shadow

| Token | 值 | 场景 |
|-------|-----|------|
| `shadow-sm` | `0 2px 8px rgba(0,0,0,0.04)` | 轻卡片 |
| `shadow-md` | `0 4px 12px rgba(0,0,0,0.05)` | 标准卡片 |
| `shadow-lg` | `0 4px 20px rgba(0,0,0,0.05)` | 大面板、浮动区 |

Dark 模式：`rgba(0,0,0,0.3~0.4)` 替代，spread 略增。

---

## 9. Z-Index

| Token | 值 | 场景 |
|-------|-----|------|
| `z-base`    | 0   | 页面背景 |
| `z-raised`  | 1   | 卡片、气泡 |
| `z-sticky`  | 100 | 顶栏、报告 Tab |
| `z-fixed`   | 200 | 底栏输入、固定 CTA |
| `z-overlay` | 300 | 遮罩 |
| `z-modal`   | 400 | 弹窗、菜单 |

---

## 10. 断点 Breakpoints

| Token | 值 | 说明 |
|-------|-----|------|
| `breakpoint-sm` | 375px | iPhone SE / 设计基准 |
| `breakpoint-md` | 414px | iPhone Plus / Pro Max |
| `breakpoint-lg` | 768px | 平板 |
| `breakpoint-xl` | 1024px | 桌面（官网扩展） |

---

## 11. 动画 Motion

| Token | 值 | 场景 |
|-------|-----|------|
| `duration-fast`    | 150ms | 按钮反馈、Tab 切换 |
| `duration-normal`  | 250ms | 卡片展开 |
| `duration-slow`    | 350ms | 页面过渡 |
| `easing-default`   | `cubic-bezier(0.4, 0, 0.2, 1)` | 标准 |
| `easing-decelerate`| `cubic-bezier(0, 0, 0.2, 1)` | 进入 |
| `easing-accelerate`| `cubic-bezier(0.4, 0, 1, 1)` | 退出 |

---

## 12. 硬编码去重对照表

设计稿中重复出现的未命名数值，已统一标准化：

| 原稿重复值 | 出现场景 | 统一 Token |
|-----------|---------|-----------|
| `#1A1A1A` / `#222222` / `#333333` | 主按钮、标题、正文 | `color-neutral-900` / `800` / `700` |
| `#F6F6F6` / `#F7F8FA` / `#F5F5F5` / `#F8F8F8` | 页面/子卡片背景 | `color-neutral-50` / `100` |
| `#6F8E6C` / `#8DA789` / `#76A07B` | 品牌绿、聊天气泡、成功态 | `color-primary-700` / `500` / `color-success-500` |
| `#E8F2E9` / `#E6F4F1` | 医生卡片、Hero 渐变顶 | `color-primary-100` / `color-accent-100` |
| `16px` / `20px` 边距 | 全局卡片边距 | `spacing-16` / `spacing-20` |
| `12px` / `16px` / `24px` 圆角 | 气泡/卡片/大卡片 | `radius-12` / `16` / `24` |
| `0 4px 12~20px rgba(0,0,0,0.05)` | 卡片阴影 | `shadow-sm` / `shadow-md` |
| `56px` 按钮高 | 主 CTA | `spacing-56` |
| `375~414px` | 移动端视口 | `breakpoint-sm` / `breakpoint-md` |

---

## 13. 明暗模式对照速查

| 语义 Token | Light | Dark |
|-----------|-------|------|
| `color-bg-page` | `#F7F8FA` | `#1A1A1A` |
| `color-bg-card` | `#FFFFFF` | `#121212` |
| `color-bg-subtle` | `#F6F6F6` | `#222222` |
| `color-text-primary` | `#1A1A1A` | `#F6F6F6` |
| `color-border-default` | `#ECECEC` | `#333333` |
| `color-action-primary` | `#1A1A1A` | `#F6F6F6` |

---

## 14. 使用规范

```css
/* ❌ 禁止硬编码 */
.card {
  background: #fff;
  padding: 16px;
  border-radius: 16px;
}

/* ✅ 使用语义别名 */
.card {
  background: var(--color-bg-card);
  padding: var(--spacing-card-padding);
  border-radius: var(--radius-card);
  box-shadow: var(--shadow-md);
}
```

在 HTML / 组件中引入：

```html
<link rel="stylesheet" href="/src/theme/vars.css" />
```

官网原型示例：`prds/官网/原型/素灵AI官网-首页.html`（相对路径 `../../../src/theme/vars.css`）。

官网扩展 token（`vars.css`）：`--site-header-h`、`--site-max-w`、`--site-section-py`。

---

## 15. 变更记录

| 版本 | 日期 | 说明 |
|------|------|------|
| 1.0.0 | 2026-07-01 | 初版，源自 6 张 App 稿 + 用色规范 |
