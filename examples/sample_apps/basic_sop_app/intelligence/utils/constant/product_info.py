# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/11/23 13:43
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: product_info.py
PRODUCT_ITEM_MAP = {"A": "投/被保险人", "B": "被保险宠物", "C": "投保份数", "D": "保险期限", "E": "保障责任",
                    "F": "缴费方式及金额", "G": "产品犹豫期",
                    "H": "产品合同解除（退保）规则", "I": "续保规则", "J": "增值服务", "K": "责任免除"}

PRODUCT_B = """
保险产品名称：宠物责任险
对应险种：宠物保险-宠物责任险
"""

PRODUCT_B_RECOMMENDATION = """
宠物责任险

- 总评：该产品不仅保障宠物对第三者造成的人身伤害，也保障自己及家人，并且包含行业首创的人宠传染病责任，适合养宠人士购买

- 优势点：性价比高，同等保障价格更低；保障对象更广，第三者、宠物主及家人均可赔。
"""

PRODUCT_C = """
保险产品名称：宠物医保大病医疗
对应险种：宠物保险-宠物医疗险
"""

PRODUCT_C_RECOMMENDATION = """
宠物医保-大病医疗

- 总评：本产品可报销猫或狗的疾病（包括小病门诊及大病手术）与意外（骨折、烧伤烫伤等）医疗费用，重疾单次最多可赔2万，性价比高，适合养宠人士投保

- 优势点：性价比高，保额高，定点宠物医院覆盖广；科技赋能，投保理赔更便捷；理赔时仅需在线提交资料，支持3日快赔；健康要求宽松，无疫苗接种要求。
"""

PRODUCT_NAME_MAP = {"B": PRODUCT_B, "C": PRODUCT_C}
PRODUCT_RECOMMENDATION_MAP = {"B": PRODUCT_B_RECOMMENDATION,
                              "C": PRODUCT_C_RECOMMENDATION}
