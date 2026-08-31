#!/usr/bin/env python3
"""根据投流词条分类规则，对 active.xlsx 搜索词进行一级/二级分类并统计。"""

import re
from pathlib import Path

import pandas as pd

ACTIVE_FILE = Path(
    "/Users/wuyuanyuan/Library/Containers/com.tencent.xinWeChat/Data/Documents/"
    "xwechat_files/wxid_h0v53ml58sbf21_dbf6/msg/file/2026-08/active.xlsx"
)
RULE_FILE = Path("/Users/wuyuanyuan/Desktop/投流词条分类.xlsx")
OUTPUT_FILE = Path("/Users/wuyuanyuan/Desktop/active_分类结果.xlsx")

# 规则按优先级从高到低排列，先匹配更具体的意图
RULES: list[tuple[str, str, re.Pattern]] = [
    # 购买决策
    ("购买决策", "价格费用评估", re.compile(r"多少钱|价格|费用|一盒|一盒多少|贵不贵|报销")),
    ("购买决策", "品牌厂家选择", re.compile(r"哪个牌子|什么牌子|品牌|厂家|制药|哪家好|好吗$|哪个好$|公司")),
    # 对比选择
    ("对比选择", "差异辨析", re.compile(r"区别|不同|差异|有啥不同|有什么区别|与.*的区别|还是|风寒还是风热|鉴别")),
    ("对比选择", "优选判断", re.compile(r"哪个效果好|哪个好|哪个更好|选哪个|哪家好")),
    # 用药指导
    ("用药指导", "用法用量咨询", re.compile(
        r"用量|剂量|一次吃|一次服|几粒|几包|几片|多少mg|多少克|成人用量|儿童用量|"
        r"一天几次|每日|每次|g=多少mg|=\s*多少|补多久|要补多久|保质期"
    )),
    ("用药指导", "适用禁忌人群", re.compile(
        r"不宜|禁忌|三种人|孕妇|哺乳期|能不能吃|可不可以吃|什么人不能|哪些人不能|"
        r"不适合|禁用|慎用|适合什么人|适合什么人群|什么人服|什么人群"
    )),
    ("用药指导", "副作用风险咨询", re.compile(r"副作用|危害|风险|不良反应|有毒|伤.*吗")),
    ("用药指导", "服药时机咨询", re.compile(
        r"饭前|饭后|餐前|餐后|最佳服用时间|什么时候吃|何时吃|早上吃|晚上吃|睡前"
    )),
    ("用药指导", "服用方法咨询", re.compile(
        r"怎么吃|怎么服|服用方法|用法|用水|温水|开水|吞服|嚼服|打粉|"
        r"正确吃法|正确用法|冲泡方法|正确冲泡|吃法是什么"
    )),
    ("用药指导", "联合用药安全", re.compile(
        r"一起吃|同服|可以一起|能否一起|联合|配伍.*吗|和.*一起.*吗|可一起"
    )),
    ("用药指导", "用药指导综合", re.compile(
        r"能常吃|长期吃|停药|吃多久|单独用药|可以单独|长期服|长期服用|需要吃多久"
    )),
    # 功效咨询
    ("功效咨询", "有效性评估", re.compile(
        r"有用吗|有效吗|有没有用|管用吗|能.*吗$|可以改善|是否有效|效果好吗|"
        r"影响.*吗|可以去.*吗|可是.*吗"
    )),
    # 治疗方案
    ("治疗方案", "选药方案咨询", re.compile(
        r"吃什么药|用什么药|什么药.*最好|哪种药|推荐.*药|有什么药|中药吃|"
        r"最好的.*药|最好的中成药|食补吃什么|贫血要吃什么|降血压的药"
    )),
    ("治疗方案", "根治可能性诉求", re.compile(r"能治愈|可以治愈|根治|能治好|可以治好|能好$|快速治愈|快速好")),
    ("治疗方案", "调理方案咨询", re.compile(r"怎么调理|如何调理|中医调理|怎么打通|调理.*吗|怎样调理|咋解决|咋办|怎办|怎样.*调理")),
    ("治疗方案", "治疗路径咨询", re.compile(r"怎么治|如何治疗|怎样治|治最有效|治疗方法|怎么医|针灸.*效果|快速.*治")),
    # 症状问题
    ("症状问题", "风险程度判断", re.compile(
        r"正常吗|严重吗|多严重|比较严重|会不会|要紧吗|危险吗|什么时候会好|多久会好"
    )),
    ("症状问题", "病因追问", re.compile(
        r"是什么原因|什么原因|怎么回事|为什么|咋回事|咋回事儿|什么造成的|什么引起|是啥原因"
    )),
    ("症状问题", "症状识别", re.compile(
        r"是什么症状|什么症状|的症状|什么病|是什么病|什么情况|什么表现|有哪些症状|"
        r"什么现象|什么感觉|.*种症状|表现.*症状|有.*拉不出来|时隐时现|一.*就"
    )),
    # 科普流量
    ("科普流量", "利弊评估", re.compile(
        r"好处和坏处|利弊|有什么好处|有什么坏处|好处与坏处|为何要尽量|为什么要少|"
        r"尽量不吃|为何.*少|复发率"
    )),
    ("科普流量", "机理解释", re.compile(r"原理|机制|为什么.*老是|为什么.*总是|怎么回事")),
    # 药品品类
    ("药品品类", "成分配方查询", re.compile(r"成分|配方|组成|配料|配方颗粒|一览表")),
    ("药品品类", "品类枚举检索", re.compile(r"有哪些|有什么|哪些.*好|什么.*食物|类别|种类")),
    ("药品品类", "药品类别检索", re.compile(r"什么药|哪种药|哪类药|药.*分类")),
    # 药品功效
    ("药品功效", "配伍功效查询", re.compile(
        r"一起.*功效|和.*一起.*(功效|作用|好处|效果)|配伍.*功效|.*与.*功效"
    )),
    ("药品功效", "疗效强度查询", re.compile(r"效果怎么样|效果怎样|疗效|效果好吗|效果好不好|治疗.*最好|.*效果好$|治疗效果")),
    ("药品功效", "主治范围查询", re.compile(
        r"主治|治什么|管什么|主要治|治疗什么|适用于|适合治疗|管什么用|药用价值"
    )),
    ("药品功效", "基础功效查询", re.compile(
        r"功效|作用|功能|功用|疗效|有什么效果|有什么作用"
    )),
    # 通用健康
    ("通用健康", "体重代谢管理", re.compile(r"减肥|瘦身|瘦|增重|代谢|降.*脂|降.*糖|控糖")),
    ("通用健康", "体质辨识与调理", re.compile(r"气虚|血虚|阴虚|阳虚|体质|湿热|寒湿|痰湿|血瘀")),
    ("通用健康", "生活方式调节", re.compile(
        r"失眠|怎么解决|最快最有效|上午好|下午好|几点|作息|运动|按摩|泡脚"
    )),
    ("通用健康", "饮食养生咨询", re.compile(
        r"可以喝|可以吃|能不能喝|能不能吃|一起喝|一起吃|养生|食疗|煲|炖|"
        r"泡水喝|煮.*水|吃什么好|能吃什么|食补|富含|正确吃法|祛湿.*吃法"
    )),
    ("通用健康", "通用健康咨询", re.compile(
        r"怎么.*好|如何.*好|怎么办|怎么改善|如何改善|健康|保养|护理|咋办|怎办|"
        r"身体素质|有.*吗$"
    )),
]


def classify_term(term: str) -> tuple[str, str]:
    if not isinstance(term, str) or not term.strip():
        return "未分类", "未分类"
    text = term.strip()
    for level1, level2, pattern in RULES:
        if pattern.search(text):
            return level1, level2
    return "未分类", "未分类"


def main() -> None:
    print("读取分类规则...")
    rules_df = pd.read_excel(RULE_FILE)
    print(f"分类标签数: {len(rules_df)}")

    print("读取 active 词条...")
    active_df = pd.read_excel(ACTIVE_FILE)
    col = active_df.columns[0]
    total = len(active_df)
    print(f"词条总数: {total:,}")

    print("开始分类...")
    results = active_df[col].map(classify_term)
    active_df["一级分类"] = results.map(lambda x: x[0])
    active_df["二级分类"] = results.map(lambda x: x[1])

    # 统计
    level1_stats = (
        active_df["一级分类"]
        .value_counts()
        .reset_index(name="数量")
    )
    level1_stats.columns = ["一级分类", "数量"]
    level1_stats["占比"] = (level1_stats["数量"] / total * 100).round(2).astype(str) + "%"

    level2_stats = (
        active_df.groupby(["一级分类", "二级分类"])
        .size()
        .reset_index(name="数量")
        .sort_values(["一级分类", "数量"], ascending=[True, False])
    )
    level2_stats["占比"] = (level2_stats["数量"] / total * 100).round(2).astype(str) + "%"

    unclassified = (active_df["一级分类"] == "未分类").sum()
    print(f"\n分类完成。未分类: {unclassified:,} ({unclassified/total*100:.2f}%)")

    print("\n=== 一级分类统计 ===")
    print(level1_stats.to_string(index=False))

    print("\n=== 二级分类统计（前30） ===")
    print(level2_stats.head(30).to_string(index=False))

    print(f"\n写入结果: {OUTPUT_FILE}")
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        active_df.to_excel(writer, sheet_name="分类明细", index=False)
        level1_stats.to_excel(writer, sheet_name="一级分类统计", index=False)
        level2_stats.to_excel(writer, sheet_name="二级分类统计", index=False)
        rules_df.to_excel(writer, sheet_name="分类规则参考", index=False)

    print("完成!")


if __name__ == "__main__":
    main()
