# 渠道管理与流量管理字段清单

- **文档类型**：字段清单
- **模块**：渠道管理与流量管理（channel-traffic-management）
- **版本**：V1.0
- **创建日期**：2026-05-17
- **最后更新**：2026-05-17
- **作者**：产品（AI辅助起草）

## 1. 字段类型说明

| 类型 | 说明 |
|------|------|
| String | 字符串 |
| Integer | 整数 |
| Decimal | 小数 |
| Boolean | 布尔值 |
| Enum | 枚举 |
| DateTime | 日期时间 |
| Ref<T> | 关联对象 |

## 2. Channel（渠道）

| 字段英文名 | 字段中文名 | 类型 | 必填 | 可编辑 | 展示位置 | 说明 |
|------------|------------|------|------|--------|----------|------|
| channel_id | 渠道ID | String | 是 | 否 | - | 系统生成唯一标识 |
| platform_name | 平台名称 | String | 是 | 是 | 列表/弹窗 | 如百度商业推广、广点通 |
| channel_name | 渠道名称 | String | 是 | 是 | 列表/弹窗 | 渠道展示名称 |
| channel_code | 渠道标识 | String | 是 | 是 | 列表/弹窗 | 全局唯一，如 `baidu_doctor_h5` |
| is_sub_channel | 是否子渠道 | Boolean | 是 | 是 | 弹窗 | 默认 false |
| sub_channel_info | 子渠道信息 | String | 否 | 是 | 列表 | 子渠道开启时填写 |
| app_summary | 应用列表 | String | 否 | 否 | 列表 | 已配置应用摘要 |
| status | 状态 | Enum | 是 | 是 | 列表 | ONLINE/OFFLINE |
| created_at | 创建时间 | DateTime | 是 | 否 | - | 系统生成 |
| created_by | 创建人 | String | 是 | 否 | - | 系统获取 |
| updated_at | 更新时间 | DateTime | 是 | 否 | - | 系统维护 |
| updated_by | 更新人 | String | 是 | 否 | - | 系统获取 |

## 3. App（应用）

| 字段英文名 | 字段中文名 | 类型 | 必填 | 可编辑 | 展示位置 | 说明 |
|------------|------------|------|------|--------|----------|------|
| app_id | 应用ID | String | 是 | 否 | - | 系统生成唯一标识 |
| app_name | 应用名称 | String | 是 | 是 | 列表/弹窗 | 如问诊、快测、舌诊 |
| app_code | 应用标识 | String | 是 | 是 | 列表/弹窗 | 全局唯一 |
| id_type | ID类型 | Enum | 否 | 是 | 列表/弹窗 | 如第三方传入 |
| id_value | ID取值 | String | 否 | 是 | 列表/弹窗 | 外部传入 ID |
| acquisition_method | 获客方式 | Enum | 否 | 是 | 列表/弹窗 | 如链接 |
| active_version_summary | 在用版本号 | String | 否 | 否 | 列表 | 开启状态版本摘要 |
| remark | 备注 | String | 否 | 是 | 列表/弹窗 | 最长500字符 |
| status | 状态 | Enum | 是 | 是 | 列表/弹窗 | ENABLED/DISABLED |
| latest_version_time | 最新版本时间 | DateTime | 否 | 否 | 列表 | 最新版本更新时间 |
| created_at | 创建时间 | DateTime | 是 | 否 | - | 系统生成 |
| updated_at | 更新时间 | DateTime | 是 | 否 | - | 系统维护 |

## 4. AppVersion（应用版本）

| 字段英文名 | 字段中文名 | 类型 | 必填 | 可编辑 | 展示位置 | 说明 |
|------------|------------|------|------|--------|----------|------|
| version_id | 版本ID | String | 是 | 否 | - | 系统生成唯一标识 |
| app_id | 应用ID | Ref<App> | 是 | 否 | 弹窗 | 所属应用 |
| version_no | 版本号 | String | 是 | 是 | 弹窗 | 如 default、V1、V2 |
| remark | 备注 | String | 否 | 是 | 弹窗 | 版本说明 |
| status | 状态 | Enum | 是 | 是 | 弹窗 | ENABLED/DISABLED |
| version_time | 版本时间 | DateTime | 是 | 否 | 弹窗 | 系统生成或维护 |

## 5. ChannelAppConfig（渠道应用配置）

| 字段英文名 | 字段中文名 | 类型 | 必填 | 可编辑 | 展示位置 | 说明 |
|------------|------------|------|------|--------|----------|------|
| config_id | 配置ID | String | 是 | 否 | - | 系统生成唯一标识 |
| channel_id | 渠道ID | Ref<Channel> | 是 | 否 | 弹窗 | 当前配置所属渠道 |
| app_id | 应用ID | Ref<App> | 是 | 是 | 弹窗 | 仅可选择开启应用 |
| version_id | 版本ID | Ref<AppVersion> | 是 | 是 | 弹窗 | 仅可选择开启版本 |
| status | 状态 | Enum | 是 | 否 | 弹窗 | 继承应用/版本有效性展示 |
| weight | 权重 | Integer | 是 | 是 | 弹窗 | 0-100 |
| version_time | 版本时间 | DateTime | 否 | 否 | 弹窗 | 版本时间 |

## 6. DoctorTrafficRule（医生流量分配）

| 字段英文名 | 字段中文名 | 类型 | 必填 | 可编辑 | 展示位置 | 说明 |
|------------|------------|------|------|--------|----------|------|
| rule_id | 规则ID | String | 是 | 否 | - | 系统生成唯一标识 |
| platform_name | 平台名称 | String | 是 | 是 | 列表/弹窗 | 筛选和组头展示 |
| channel_id | 渠道ID | Ref<Channel> | 是 | 是 | 列表/弹窗 | 关联渠道 |
| channel_name | 渠道名称 | String | 是 | 否 | 列表 | 冗余展示 |
| channel_code | 渠道标识 | String | 是 | 否 | 列表 | 冗余展示 |
| doctor_allocation_type | 医生分配类型 | Enum | 是 | 是 | 列表/弹窗 | WEIGHTED/SPECIFIED |
| doctor_id | 医生ID | String | 是 | 是 | 列表/弹窗 | 服务医生 |
| doctor_name | 医生名称 | String | 是 | 否 | 列表 | 展示字段 |
| weight | 权重 | Integer | 是 | 是 | 列表/弹窗 | 0-100 |
| ratio | 占比 | Decimal | 是 | 否 | 列表/弹窗 | 系统计算 |
| status | 状态 | Enum | 是 | 否 | - | ACTIVE/DELETED |

## 7. TeamTrafficRule（团队流量分配）

| 字段英文名 | 字段中文名 | 类型 | 必填 | 可编辑 | 展示位置 | 说明 |
|------------|------------|------|------|--------|----------|------|
| rule_id | 规则ID | String | 是 | 否 | - | 系统生成唯一标识 |
| platform_name | 平台名称 | String | 是 | 是 | 列表/弹窗 | 筛选和组头展示 |
| channel_id | 渠道ID | Ref<Channel> | 是 | 是 | 列表/弹窗 | 关联渠道 |
| doctor_id | 医生ID | String | 否 | 是 | 列表 | 上级医生 |
| doctor_name | 医生名称 | String | 否 | 否 | 列表 | 展示字段 |
| traffic_type | 流量类型 | Enum | 是 | 是 | 列表/弹窗 | TEAM_GENERAL/SPECIFIED_ASSISTANT |
| team_id | 服务团队ID | String | 是 | 是 | 列表/弹窗 | 服务团队 |
| team_name | 服务团队 | String | 是 | 否 | 列表 | 展示字段 |
| weight | 权重 | Integer | 是 | 是 | 列表/弹窗 | 0-100 |
| ratio | 占比 | Decimal | 是 | 否 | 列表/弹窗 | 系统计算 |
| status | 状态 | Enum | 是 | 否 | - | ACTIVE/DELETED |

## 8. AssistantTrafficRule（医助流量分配）

| 字段英文名 | 字段中文名 | 类型 | 必填 | 可编辑 | 展示位置 | 说明 |
|------------|------------|------|------|--------|----------|------|
| rule_id | 规则ID | String | 是 | 否 | - | 系统生成唯一标识 |
| allocation_type | 分配类型 | Enum | 是 | 是 | 列表/弹窗 | TEAM_GENERAL/SPECIFIED_ASSISTANT |
| platform_name | 平台名称 | String | 否 | 是 | 指定医助 | 指定医助必填 |
| channel_id | 渠道ID | Ref<Channel> | 否 | 是 | 指定医助 | 指定医助必填 |
| team_id | 服务团队ID | String | 是 | 是 | 列表/弹窗 | 所属服务团队 |
| team_name | 所属团队 | String | 是 | 否 | 列表 | 展示字段 |
| doctor_id | 所属医生ID | String | 否 | 否 | 列表 | 所属医生 |
| doctor_name | 所属医生 | String | 否 | 否 | 列表 | 展示字段 |
| assistant_id | 医助ID | String | 是 | 是 | 列表/弹窗 | 服务医助 |
| assistant_name | 医助名称 | String | 是 | 否 | 列表 | 展示字段 |
| weight | 权重 | Integer | 是 | 是 | 列表/弹窗 | 0-100 |
| ratio | 占比 | Decimal | 是 | 否 | 列表/弹窗 | 系统计算 |
| status | 状态 | Enum | 是 | 否 | - | ACTIVE/DELETED |

## 9. AllocationRecord（分配记录）

| 字段英文名 | 字段中文名 | 类型 | 必填 | 说明 |
|------------|------------|------|------|------|
| record_id | 记录ID | String | 是 | 系统生成唯一标识 |
| lead_id | 线索ID | String | 是 | 新进入流量或线索标识 |
| user_id | 用户ID | String | 否 | 已识别用户 |
| channel_id | 渠道ID | Ref<Channel> | 是 | 命中渠道 |
| app_id | 应用ID | Ref<App> | 否 | 命中应用 |
| version_id | 版本ID | Ref<AppVersion> | 否 | 命中版本 |
| doctor_id | 医生ID | String | 否 | 分配医生 |
| team_id | 服务团队ID | String | 否 | 分配团队 |
| assistant_id | 医助ID | String | 否 | 分配医助 |
| matched_rule_ids | 命中规则ID | String | 否 | 多个规则用逗号分隔 |
| allocation_result | 分配结果 | Enum | 是 | SUCCESS/FAILED/MANUAL_PENDING |
| fail_reason | 失败原因 | String | 否 | 失败或人工待处理原因 |
| allocated_at | 分配时间 | DateTime | 是 | 系统生成 |

## 10. 枚举值

### status（通用状态）

| 枚举值 | 说明 |
|--------|------|
| ENABLED | 开启 |
| DISABLED | 关闭 |
| ONLINE | 在线 |
| OFFLINE | 关闭 |
| ACTIVE | 生效 |
| DELETED | 已删除/停用 |

### id_type（ID类型）

| 枚举值 | 说明 |
|--------|------|
| THIRD_PARTY | 第三方传入 |
| INTERNAL | 内部生成 |

### acquisition_method（获客方式）

| 枚举值 | 说明 |
|--------|------|
| LINK | 链接 |
| QR_CODE | 二维码 |
| API | API传入 |

### doctor_allocation_type（医生分配类型）

| 枚举值 | 说明 |
|--------|------|
| WEIGHTED | 自主分配医生/按权重分配医生 |
| SPECIFIED | 指定医生 |

### traffic_type / allocation_type（流量或医助分配类型）

| 枚举值 | 说明 |
|--------|------|
| TEAM_GENERAL | 团队通用 |
| SPECIFIED_ASSISTANT | 指定医助 |

### allocation_result（分配结果）

| 枚举值 | 说明 |
|--------|------|
| SUCCESS | 分配成功 |
| FAILED | 分配失败 |
| MANUAL_PENDING | 待人工分配 |

## 11. 字段约束与规则

- `channel_code` 全局唯一，建议仅允许英文、数字、下划线。
- `app_code` 全局唯一，建议仅允许英文、数字、下划线。
- `version_no` 在同一应用下唯一。
- `weight` 仅允许 0-100 的整数。
- `ratio` 由系统计算，不允许手动编辑。
- 关闭状态的渠道、应用、版本不可被新增配置引用。
- 删除对象前必须校验是否存在生效配置。
- 权重修改只影响新进入流量，不追溯历史分配记录。

## 12. 修订记录

| 版本 | 日期 | 修订内容 | 修订人 |
|------|------|----------|--------|
| V1.0 | 2026-05-17 | 初始版本 | 产品（AI辅助起草） |

