# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/12/5 16:22
# @Author  : fanen.lhy
# @Email   : fanen.lhy@antgroup.com
# @FileName: log_type_const.py
from enum import Enum


class LogTypeEnum(str, Enum):
    default = 'default'
    llm_trace = 'llm_trace'
    flask_request = 'flask_request'
    flask_response = 'flask_response'
