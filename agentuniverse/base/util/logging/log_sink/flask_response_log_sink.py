# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/12/9 18:01
# @Author  : fanen.lhy
# @Email   : fanen.lhy@antgroup.com
# @FileName: base_log_sink.py

from agentuniverse.base.util.logging.log_sink.base_file_log_sink import BaseFileLogSink
from agentuniverse.base.util.logging.log_type_enum import LogTypeEnum


class FlaskResponseLogSink(BaseFileLogSink):
    log_type: LogTypeEnum = LogTypeEnum.flask_response

    def filter(self, record):
        if not record['extra'].get('log_type') == self.log_type:
            return False
        self.process_record(record)
        return True

    def process_record(self, record):
        record["message"] = self.generate_log(
            flask_response=record['extra'].get('flask_response'),
            elapsed_time=record['extra']['elapsed_time']
        )
        record['extra'].pop('flask_response', None)

    def generate_log(self, flask_response, elapsed_time) -> str:
        pass
