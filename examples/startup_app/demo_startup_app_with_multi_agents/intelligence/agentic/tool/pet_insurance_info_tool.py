# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/11/28 17:17
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: pet_insurance_tool.py
from agentuniverse.agent.action.tool.tool import Tool, ToolInput

from examples.startup_app.demo_startup_app_with_multi_agents.intelligence.utils.constant.prod_description import \
    PROD_A_DESCRIPTION, PROD_B_DESCRIPTION


class PetInsuranceInfoTool(Tool):
    def execute(self, tool_input: ToolInput):
        ins_name = tool_input.get_data('ins_name')
        if ins_name == '宠物医保（体验版）':
            return PROD_A_DESCRIPTION
        if ins_name == '宠物医保':
            return PROD_B_DESCRIPTION
        return PROD_B_DESCRIPTION
