# 数据中台与BI看板字段清单（逻辑字段）

> **文档类型**：字段清单（逻辑层，实施期与物理表对齐）  
> **版本**：V1.0  
> **创建日期**：2026-05-14  
> **关联**：[PRD.md](./PRD.md)、[analysis/data-platform/2026-05-14-DWD-DWS模型清单.md](../../analysis/data-platform/2026-05-14-DWD-DWS模型清单.md)、[2026-05-14-标签与画像日表设计.md](../../analysis/data-platform/2026-05-14-标签与画像日表设计.md)

---

## 1. 说明

- 本清单描述**面向BI与运营分析**的核心数据集字段逻辑类型；物理类型随数仓选型调整（如`BIGINT`/`STRING`）。  
- **枚举**列全量值；若业务扩展枚举，需同步更新本清单版本。  
- **审计字段**：所有分区表建议包含`pt`（业务日分区，STRING `yyyy-MM-dd`）。

---

## 2. 漏斗日汇总 `dws_funnel_channel_assistant_1d`（逻辑）

| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pt | STRING | 是 | 业务日分区 |
| channel_id | BIGINT | 否 | 渠道维度，可空表示未知 |
| assistant_id | BIGINT | 否 | 医助维度，可空表示未分配 |
| cnt_f01 | BIGINT | 是 | 漏斗步骤F01当日完成去重人数 |
| cnt_f02 | BIGINT | 是 | 同上，F02 |
| cnt_f03 | BIGINT | 是 | 同上，F03 |
| cnt_f04 | BIGINT | 是 | 同上，F04 |
| cnt_f05 | BIGINT | 是 | 同上，F05 |
| cnt_f06 | BIGINT | 是 | 同上，F06 |
| cnt_f07 | BIGINT | 是 | 同上，F07 |
| cnt_f08 | BIGINT | 是 | 同上，F08 |
| cnt_f09 | BIGINT | 是 | 同上，F09 |
| cnt_f10 | BIGINT | 是 | 同上，F10（支付成功） |

**枚举**：漏斗步骤编码`funnel_step`在明细层取值范围为`F01`～`F10`（定义见指标字典）。

---

## 3. GMV日汇总 `dws_trade_gmv_1d`（逻辑）

| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pt | STRING | 是 | 业务日分区 |
| channel_id | BIGINT | 否 | 来自用户维度 |
| role_id | BIGINT | 否 | 服务对象 |
| user_id | BIGINT | 否 | 账号 |
| order_cnt | BIGINT | 是 | 支付成功订单数 |
| gmv | DECIMAL(18,2) | 是 | 实付金额合计 |

---

## 4. 角色画像宽表 `ads_role_profile_wide_1d`（逻辑）

| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pt | STRING | 是 | 业务日分区 |
| role_id | BIGINT | 是 | 主键之一 |
| user_id | BIGINT | 是 | 关联账号 |
| channel_id | BIGINT | 否 | 账号渠道 |
| relationship | STRING | 是 | 角色与用户关系枚举，见下表 |
| health_tag_summary | STRING | 否 | 脱敏摘要，禁止默认放原文JSON |
| paid_order_cnt_30d | BIGINT | 是 | 近30日支付订单数 |
| gmv_30d | DECIMAL(18,2) | 是 | 近30日实付金额 |
| last_paid_date | DATE | 否 | 最近支付业务日 |
| last_active_date | DATE | 否 | 最近活跃业务日 |
| silence_days | INT | 是 | `pt`与`last_active_date`差 |
| service_stage | STRING | 是 | 服务阶段枚举，见下表 |
| risk_blacklist_flag | TINYINT | 是 | 0否1是 |
| risk_block_wework_flag | TINYINT | 是 | 0否1是 |

### 4.1 relationship（角色关系）

| 枚举值 | 说明 |
|--------|------|
| SELF | 本人 |
| PARENT | 父母 |
| CHILD | 子女 |
| SPOUSE | 配偶 |
| OTHER | 其他 |

### 4.2 service_stage（服务阶段，建议集）

| 枚举值 | 说明 |
|--------|------|
| NEW | 新进入私域，未完成关键问诊动作 |
| CONSULT | 问诊/病历推进中 |
| WAIT_SIGN | 待医生签字 |
| WAIT_PAY | 待支付 |
| PAID | 已支付 |
| FOLLOWUP | 随访期 |
| SILENT | 沉默（达到沉默阈值） |
| CHURN | 流失（达到流失阈值） |

---

## 5. 标签实例长表 `dwd_fact_tag_instance_di`（逻辑）

| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pt | STRING | 是 | 标签生效业务日 |
| role_id | BIGINT | 是 | 主粒度 |
| user_id | BIGINT | 是 | 冗余关联 |
| tag_id | BIGINT | 是 | 关联标签元数据 |
| tag_value | STRING | 是 | 枚举编码或数值字符串 |
| source | STRING | 是 | 标签来源枚举，见下表 |
| etl_time | TIMESTAMP | 是 | 写入时间 |

### 5.1 source（标签来源）

| 枚举值 | 说明 |
|--------|------|
| rule | 规则标签 |
| model | 模型标签 |
| crm_sync | CRM同步 |

---

## 6. 拉黑专题表 `ads_role_block_assistant_daily`（逻辑）

| 字段名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| pt | STRING | 是 | 统计业务日 |
| role_id | BIGINT | 是 | 服务对象 |
| user_id | BIGINT | 是 | 账号 |
| block_event_ts | TIMESTAMP | 否 | 事件发生时间 |
| block_source | STRING | 是 | 枚举：`WEWORK_CALLBACK`/`PLATFORM`/`OPS` |
| assistant_id_at_event | BIGINT | 否 | 事件关联医助 |
| channel_id | BIGINT | 否 | 渠道 |
| service_stage_at_event | STRING | 否 | 事件时点或前一日推断阶段 |

---

## 7. 修订记录

| 版本 | 日期 | 修订内容 | 修订人 |
|------|------|----------|--------|
| V1.0 | 2026-05-14 | 初版 | 产品 |
