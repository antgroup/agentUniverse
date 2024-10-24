# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/10/21 10:52
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: compliance_base.py
from typing import Optional

from agentuniverse.agent.input_object import InputObject

from agentuniverse.base.component.component_configer_util import ComponentConfigerUtil

from agentuniverse.base.component.component_enum import ComponentEnum
from agentuniverse.base.util.logging.logging_util import LOGGER

from agentuniverse.base.component.component_base import ComponentBase
from pydantic import BaseModel


class ComplianceWorker(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    executor: Optional[ComponentBase] = None
    stream_step: Optional[int] = 10
    default_output: Optional[str] = '输出内容不合规'
    input_key: Optional[str] = 'input'

    def __init__(self, config: dict):
        component_manager_clz = ComponentConfigerUtil.get_component_manager_clz_by_type(
            ComponentEnum.from_value(self.type))
        executor = component_manager_clz().get_instance_obj(self.name)
        stream_step = config.get('stream_step') or self.stream_step
        default_output = config.get('default_output') or self.default_output
        input_key = config.get('input_key') or self.input_key
        data = {'name': config['name'], 'type': config['type'], 'executor': executor, 'stream_step': stream_step,
                'default_output': default_output, 'input_key': input_key}
        super().__init__(**data)

    def initialize_by_config(self, config: dict):
        self.type = config['type']
        self.name = config['name']
        component_manager_clz = ComponentConfigerUtil.get_component_manager_clz_by_type(
            ComponentEnum.from_value(self.type))
        self.executor = component_manager_clz().get_instance_obj(self.name)
        self.stream_step = config.get('stream_step') or self.stream_step
        self.default_output = config.get('default_output') or self.default_output
        self.input_key = config.get('input_key') or self.input_key

    def execute(self, input_text: str):
        input_param = {self.input_key: input_text}
        if self.type == ComponentEnum.TOOL.value:
            check_result = self.executor.run(**input_param)
        elif self.type == ComponentEnum.AGENT.value:
            check_result = self.executor.run(InputObject(input_param))
        else:
            LOGGER.error(f'Type {self.type} not support for compliance!')
            return
        if not check_result:
            raise Exception(self.default_output)
