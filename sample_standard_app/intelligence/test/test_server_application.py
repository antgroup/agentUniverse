# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/4/9 16:57
# @Author  : jerry.zzw 
# @Email   : jerry.zzw@antgroup.com
# @FileName: server_application.py

from sample_standard_app.boostrap.intelligence.server_application import ServerApplication


def test_app_start():
    ServerApplication.start()
