# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/10/21 12:01
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: default_compliance_tool.py
from agentuniverse.agent.action.tool.tool import Tool, ToolInput


class DefaultComplianceTool(Tool):
    def execute(self, tool_input: ToolInput):
        input = tool_input.get_data("input")
        sensitive_words = ['习近平', '法轮功']
        for word in sensitive_words:
            if word in input:
                return False
        return True
