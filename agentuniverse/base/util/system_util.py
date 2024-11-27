# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/3/14 10:42
# @Author  : fanen.lhy
# @Email   : fanen.lhy@antgroup.com
# @FileName: system_util.py

from pathlib import Path
import importlib

PROJECT_ROOT_PATH = None


def get_project_root_path() -> Path:
    """Get the project root path."""
    global PROJECT_ROOT_PATH
    if PROJECT_ROOT_PATH:
        return PROJECT_ROOT_PATH
    current_work_directory = Path.cwd()
    root_path = current_work_directory.parents[1]
    PROJECT_ROOT_PATH = root_path
    return root_path


def parse_dynamic_str(param: str):
    """
    Translate a string, firstly attempting to parse it as a full path to a
    parameterless function. If it can be correctly imported, return the result
    of the function execution, otherwise return the original string.
    This is useful in scenarios where it's inconvenient to write the real
    value directly, such as with secret keys.
    """
    try:
        parts = param.rsplit('.', 1)
        if len(parts) == 2:
            module_path, func_name = parts
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
            if callable(func):
                return func()
            else:
                return param
        else:
            return param
    except (ImportError, AttributeError, Exception):
        return param