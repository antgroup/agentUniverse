# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/10/14 14:59
# @Author  : weizjajj
# @Email   : weizhongjie.wzj@antgroup.com
# @FileName: opinions_verify_tool.py

from agentuniverse.agent.action.tool.tool import Tool, ToolInput
import pandas as pd


class LoadOpinionTool(Tool):
    def execute(self, tool_input: ToolInput):
        opinions_path = tool_input.get_data("opinions_path")

        # 从csv文件中读取信息
        df = pd.read_csv(opinions_path,header=None)
        values = df.values.tolist()
        keys = values[0]
        opinions = []
        for index,row in enumerate(values[1:]):

            temp = {
                keys[i]:row[i] for i in range(len(row))
            }
            temp['opinion_id'] = index
            opinions.append(temp)

        return {"opinions": opinions}


class OpinionMatchingTool(Tool):
    def execute(self, tool_input: ToolInput):
        matched_opinions =[]
        opinions = tool_input.get_data("opinions")
        data = tool_input.get_data("data_fining_result")
        for opinion in opinions:
            matching_conditions = opinion["rule"]
            if eval(matching_conditions,data):
                matched_opinions.append(opinion)
        return {
            "matched_opinions": matched_opinions
        }