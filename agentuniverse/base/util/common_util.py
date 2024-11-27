# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/10/24 21:12
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: common_util.py
from queue import Queue


def stream_output(output_stream: Queue, data: dict):
    """Add data to the output stream.

    Args:
        output_stream (Queue): The output stream.
        data (dict): The data to be streamed.
    """
    if output_stream is None:
        return
    output_stream.put_nowait(data)
