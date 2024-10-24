# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/10/21 16:35
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: default_mask_tool.py


import re

from agentuniverse.agent.action.tool.tool import Tool, ToolInput


class DefaultMaskTool(Tool):
    def execute(self, tool_input: ToolInput):
        input_text = tool_input.get_data("input")
        print(input_text)
        text = re.sub(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', lambda x: self.mask_email(x.group()),
                      input_text)
        text = re.sub(r'\b\d{3}[-. ]?\d{3}[-. ]?\d{4}\b', lambda x: self.mask_phone(x.group()), text)
        text = re.sub(r'\b\d{17}|\d{15}\b', lambda x: self.mask_id_card(x.group()), text)
        return text

    @staticmethod
    def mask_email(email: str):
        """mask email data"""
        masked_email = re.sub(r'(?<=.).(?=.*@)', '*', email)
        return masked_email

    @staticmethod
    def mask_phone(phone: str):
        """mask phone data"""
        masked_phone = re.sub(r'\d(?=\d{4})', '*', phone)
        return masked_phone

    @staticmethod
    def mask_id_card(id_card):
        """mask id data"""
        masked_id_card = re.sub(r'(?<=\d{3})\d(?=\d{2})', '*', id_card)
        return masked_id_card
