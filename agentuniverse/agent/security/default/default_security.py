# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/10/18 17:40
# @Author  : jijiawei
# @Email   : jijiawei.jjw@antgroup.com
# @FileName: default_security.py


from agentuniverse.agent.security.security import Security


class DefaultSecurity(Security):
    def security_unpass_process(self):
        """Target security """
        return ['input']
