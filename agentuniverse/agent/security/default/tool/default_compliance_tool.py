# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/10/21 12:01
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: default_compliance_tool.py
from typing import Optional

from agentuniverse.base.util.logging.logging_util import LOGGER

from agentuniverse.base.config.component_configer.configers.tool_configer import ToolConfiger

from agentuniverse.agent.action.tool.tool import Tool, ToolInput
import os
import glob


class DefaultComplianceTool(Tool):
    sensitive_single_vocabulary: Optional[list] = []
    sensitive_pair_vocabulary: Optional[list] = []

    def execute(self, tool_input: ToolInput):
        input_text = tool_input.get_data("input")
        for word in self.sensitive_single_vocabulary:
            if word in input_text:
                LOGGER.info(f'Target sensitive word: {word}')
                return False
        for pair in self.sensitive_pair_vocabulary:
            miss_flag = False
            for word in pair:
                if word not in input_text:
                    miss_flag = True
                    break
            if not miss_flag:
                LOGGER.info(f'Target sensitive pair: {pair}')
                return False
        return True

    @staticmethod
    def load_default_vocabulary():
        # 获取当前文件的绝对路径
        current_path = os.path.abspath(__file__)
        vocabulary_path = os.path.dirname(os.path.dirname(current_path)) + '/vocabulary'
        txt_files = glob.glob(os.path.join(vocabulary_path, '*.txt'))
        sensitive_single_collection = []
        sensitive_pair_collection = []
        for file_path in txt_files:
            with open(file_path, 'r', encoding='utf-8') as file:
                # from https://chinadigitaltimes.net/space/GFW%E6%95%8F%E6%84%9F%E8%AF%8D
                content = file.read()
                file_name = os.path.basename(file.name)
                if file_name == 'GFW补充词库.txt':
                    for line in content.split(','):
                        if not line:
                            continue
                        else:
                            sensitive_single_collection.append(line.strip())
                    continue

                for line in content.split('\n'):
                    if not line:
                        continue
                    if '+' in line:
                        sensitive_pair_collection.append(line.strip().split('+'))
                    else:
                        sensitive_single_collection.append(line.strip())
        return sensitive_single_collection, sensitive_pair_collection

    def initialize_by_component_configer(self, component_configer: ToolConfiger) -> 'DefaultComplianceTool':
        super().initialize_by_component_configer(component_configer)
        self.sensitive_single_vocabulary, self.sensitive_pair_vocabulary = self.load_default_vocabulary()
        return self
