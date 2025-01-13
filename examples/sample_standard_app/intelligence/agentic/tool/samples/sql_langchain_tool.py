# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/7/9 20:04
# @Author  : weizjajj 
# @Email   : weizhongjie.wzj@antgroup.com
# @FileName: sql_langchain_tool.py

from typing import Type, Optional

from langchain_core.tools import BaseTool, Tool as LangchainTool

from agentuniverse.agent.action.tool.tool import ToolInput
from agentuniverse.database.sqldb_wrapper_manager import SQLDBWrapperManager
from examples.sample_standard_app.intelligence.agentic.tool.samples.langchain_tool import LangChainTool


class SqlLangchainTool(LangChainTool):
    db_wrapper_name: Optional[str] = ""
    clz: Type[BaseTool] = BaseTool

    def execute(self, tool_input: ToolInput):
        if self.tool is None:
            self.get_sql_database()
        return super().execute(tool_input)

    def get_sql_database(self):
        db_wrapper = SQLDBWrapperManager().get_instance_obj(self.db_wrapper_name)
        self.tool = self.clz(db=db_wrapper.sql_database)
        self.description = self.tool.description

    def as_langchain(self) -> LangchainTool:
        if self.tool is None:
            self.get_sql_database()
        return super().as_langchain()

    def get_langchain_tool(self, init_params: dict, clz: Type[BaseTool]):
        self.db_wrapper_name = init_params.get("db_wrapper")
        self.clz = clz
