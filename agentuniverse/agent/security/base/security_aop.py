# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2025/1/13 18:15
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: security_aop.py
from functools import wraps

from agentuniverse.agent.security.security_manager import SecurityManager


def security_process(security_name):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            # 调用原函数
            res = func(self, *args, **kwargs)
            security = SecurityManager().get_instance_obj(security_name)
            security_res = security.content_process({'input': res})
            return security_res

        return wrapper

    return decorator
