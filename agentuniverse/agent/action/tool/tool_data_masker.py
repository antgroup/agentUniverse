import re
from typing import Union, Dict, ClassVar

from agentuniverse.agent.action.tool.enum import ToolTypeEnum
from agentuniverse.agent.action.tool.tool import Tool, ToolInput


class DataMasker(Tool):
    """数据脱敏工具"""

    MASK_RULES: ClassVar[Dict[str, str]] = {
        'phone': r'(\d{3})\d{4}(\d{4})',
        'id_card': r'(\d{4})\d{10}(\w{4})',
        'name': r'([\u4e00-\u9fa5]{1})([\u4e00-\u9fa5]+)'
    }

    masking_strategies: Dict = {
        'phone': lambda m: f'{m.group(1)}****{m.group(2)}',
        'id_card': lambda m: f'{m.group(1)}**********{m.group(2)}',
        'name': lambda m: f'{m.group(1)}*{m.group(2)[-1] if len(m.group(2))>1 else "*"}'
    }

    def __init__(self):
        super().__init__()
        self.tool_type = ToolTypeEnum.FUNC
        self.name = "data_masker"
        self.description = "Mask sensitive information in text like phone numbers, ID cards and names"
        self.input_keys = ["text"]

    def mask(self, text: str, custom_rules: Dict[str, str] = None) -> str:
        """执行脱敏处理"""
        rules = {**self.MASK_RULES, **(custom_rules or {})}

        for pattern_name, pattern in rules.items():
            text = re.sub(
                pattern,
                self.masking_strategies.get(pattern_name, lambda m: '****'),
                text
            )
        return text

    def execute(self, tool_input: ToolInput) -> str:
        self.input_check(tool_input.to_dict())
        return self.mask(tool_input.get_data("text"))