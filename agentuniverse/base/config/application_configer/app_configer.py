# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/3/12 16:17
# @Author  : jerry.zzw 
# @Email   : jerry.zzw@antgroup.com
# @FileName: app_configer.py
from typing import Optional
from agentuniverse.base.config.configer import Configer


class AppConfiger(object):
    """The AppConfiger class, which is used to load and manage the application configuration."""

    def __init__(self):
        """Initialize the AppConfiger."""
        self.__configer: Optional[Configer] = None
        self.__base_info_appname: Optional[str] = None
        self.__core_default_package_list: Optional[list[str]] = None
        self.__core_agent_package_list: Optional[list[str]] = None
        self.__core_knowledge_package_list: Optional[list[str]] = None
        self.__core_llm_package_list: Optional[list[str]] = None
        self.__core_planner_package_list: Optional[list[str]] = None
        self.__core_tool_package_list: Optional[list[str]] = None
        self.__core_memory_package_list: Optional[list[str]] = None
        self.__core_service_package_list: Optional[list[str]] = None
        self.__core_sqldb_wrapper_package_list: Optional[list[str]] = None
        self.__core_prompt_package_list: Optional[list[str]] = None
        self.__core_product_package_list: Optional[list[str]] = None
        self.__core_workflow_package_list: Optional[list[str]] = None
        self.__core_embedding_package_list: Optional[list[str]] = None
        self.__core_doc_processor_package_list: Optional[list[str]] = None
        self.__core_reader_package_list: Optional[list[str]] = None
        self.__core_store_package_list: Optional[list[str]] = None
        self.__core_rag_router_package_list: Optional[list[str]] = None
        self.__core_query_paraphraser_package_list: Optional[list[str]] = None
        self.__core_memory_compressor_package_list: Optional[list[str]] = None
        self.__core_memory_storage_package_list: Optional[list[str]] = None
        self.__core_work_pattern_package_list: Optional[list[str]] = None
        self.__core_log_sink_package_list: Optional[list[str]] = None
        self.__conversation_memory_configer: Optional[dict] = None

    @property
    def base_info_appname(self) -> Optional[str]:
        """Return the appname of the application."""
        return self.__base_info_appname

    @property
    def core_default_package_list(self) -> Optional[list[str]]:
        """Return the default package list of the core."""
        return self.__core_default_package_list

    @property
    def core_agent_package_list(self) -> Optional[list[str]]:
        """Return the agent package list of the core."""
        return self.__core_agent_package_list

    @property
    def core_knowledge_package_list(self) -> Optional[list[str]]:
        """Return the knowledge package list of the core."""
        return self.__core_knowledge_package_list

    @property
    def core_llm_package_list(self) -> Optional[list[str]]:
        """Return the llm package list of the core."""
        return self.__core_llm_package_list

    @property
    def core_planner_package_list(self) -> Optional[list[str]]:
        """Return the planner package list of the core."""
        return self.__core_planner_package_list

    @property
    def core_tool_package_list(self) -> Optional[list[str]]:
        """Return the tool package list of the core."""
        return self.__core_tool_package_list

    @property
    def core_memory_package_list(self) -> Optional[list[str]]:
        """Return the memory package list of the core."""
        return self.__core_memory_package_list

    @property
    def core_service_package_list(self) -> Optional[list[str]]:
        """Return the service package list of the core."""
        return self.__core_service_package_list

    @property
    def core_sqldb_wrapper_package_list(self) -> Optional[list[str]]:
        """Return the sql db wrapper package list of the core."""
        return self.__core_sqldb_wrapper_package_list

    @property
    def core_prompt_package_list(self) -> Optional[list[str]]:
        return self.__core_prompt_package_list

    @property
    def core_product_package_list(self) -> Optional[list[str]]:
        return self.__core_product_package_list

    @property
    def core_workflow_package_list(self) -> Optional[list[str]]:
        return self.__core_workflow_package_list

    @property
    def core_embedding_package_list(self) -> Optional[list[str]]:
        """Return the embedding package list of the core."""
        return self.__core_embedding_package_list

    @property
    def core_doc_processor_package_list(self) -> Optional[list[str]]:
        """Return the document processor package list of the core."""
        return self.__core_doc_processor_package_list

    @property
    def core_reader_package_list(self) -> Optional[list[str]]:
        """Return the reader package list of the core."""
        return self.__core_reader_package_list

    @property
    def core_store_package_list(self) -> Optional[list[str]]:
        """Return the store package list of the core."""
        return self.__core_store_package_list

    @property
    def core_rag_router_package_list(self) -> Optional[list[str]]:
        """Return the RAG router package list of the core."""
        return self.__core_rag_router_package_list

    @property
    def core_query_paraphraser_package_list(self) -> Optional[list[str]]:
        """Return the query paraphraser package list of the core."""
        return self.__core_query_paraphraser_package_list

    @property
    def core_memory_compressor_package_list(self) -> Optional[list[str]]:
        """Return the memory compressor package list of the core."""
        return self.__core_memory_compressor_package_list

    @property
    def core_memory_storage_package_list(self) -> Optional[list[str]]:
        """Return the memory storage package list of the core."""
        return self.__core_memory_storage_package_list

    @property
    def core_work_pattern_package_list(self) -> Optional[list[str]]:
        """Return the work pattern package list of the core."""
        return self.__core_work_pattern_package_list

    @property
    def core_log_sink_package_list(self) -> Optional[list[str]]:
        """Return the work pattern package list of the core."""
        return self.__core_log_sink_package_list

    @property
    def conversation_memory_configer(self) -> dict:
        return self.__conversation_memory_configer

    def load_by_configer(self, configer: Configer) -> 'AppConfiger':
        """Load the AppConfiger by the given Configer.

        Args:
            configer(Configer): the Configer object
        Returns:
            AppConfiger: the AppConfiger object
        """
        self.__configer = configer
        self.__base_info_appname = configer.value.get('BASE_INFO', {}).get('appname')
        self.__core_default_package_list = configer.value.get('CORE_PACKAGE', {}).get('default')
        self.__core_agent_package_list = configer.value.get('CORE_PACKAGE', {}).get('agent')
        self.__core_knowledge_package_list = configer.value.get('CORE_PACKAGE', {}).get('knowledge')
        self.__core_llm_package_list = configer.value.get('CORE_PACKAGE', {}).get('llm')
        self.__core_planner_package_list = configer.value.get('CORE_PACKAGE', {}).get('planner')
        self.__core_tool_package_list = configer.value.get('CORE_PACKAGE', {}).get('tool')
        self.__core_memory_package_list = configer.value.get('CORE_PACKAGE', {}).get('memory')
        self.__core_service_package_list = configer.value.get('CORE_PACKAGE', {}).get('service')
        self.__core_sqldb_wrapper_package_list = configer.value.get('CORE_PACKAGE', {}).get('sqldb_wrapper')
        self.__core_prompt_package_list = configer.value.get('CORE_PACKAGE', {}).get('prompt')
        self.__core_product_package_list = configer.value.get('CORE_PACKAGE', {}).get('product')
        self.__core_workflow_package_list = configer.value.get('CORE_PACKAGE', {}).get('workflow')
        self.__core_embedding_package_list = configer.value.get('CORE_PACKAGE', {}).get('embedding')
        self.__core_doc_processor_package_list = configer.value.get('CORE_PACKAGE', {}).get('doc_processor')
        self.__core_reader_package_list = configer.value.get('CORE_PACKAGE', {}).get('reader')
        self.__core_store_package_list = configer.value.get('CORE_PACKAGE', {}).get('store')
        self.__core_rag_router_package_list = configer.value.get('CORE_PACKAGE', {}).get('rag_router')
        self.__core_query_paraphraser_package_list = configer.value.get('CORE_PACKAGE', {}).get('query_paraphraser')
        self.__core_memory_compressor_package_list = configer.value.get('CORE_PACKAGE', {}).get('memory_compressor')
        self.__core_memory_storage_package_list = configer.value.get('CORE_PACKAGE', {}).get('memory_storage')
        self.__core_work_pattern_package_list = configer.value.get('CORE_PACKAGE', {}).get('work_pattern')
        self.__core_log_sink_package_list = configer.value.get('CORE_PACKAGE', {}).get('log_sink')
        self.__conversation_memory_configer = configer.value.get('CONVERSATION_MEMORY')
        return self
