# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/10/18 17:23
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: security_manager.py


from agentuniverse.base.annotation.singleton import singleton
from agentuniverse.base.component.component_enum import ComponentEnum
from agentuniverse.base.component.component_manager_base import ComponentManagerBase


@singleton
class SecurityManager(ComponentManagerBase):
    """The SecurityManager class, which is used to manage security component."""

    def __init__(self):
        """Initialize the SecurityManager."""
        super().__init__(ComponentEnum.SECURITY)
