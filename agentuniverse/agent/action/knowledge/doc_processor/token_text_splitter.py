# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/8/5 15:37
# @Author  : fanen.lhy
# @Email   : fanen.lhy@antgroup.com
# @FileName: token_text_splitter.py
from typing import List, Optional
from langchain.text_splitter import TokenTextSplitter as Splitter

from agentuniverse.agent.action.knowledge.doc_processor.doc_processor import \
    DocProcessor
from agentuniverse.agent.action.knowledge.store.document import Document
from agentuniverse.agent.action.knowledge.store.query import Query
from agentuniverse.base.config.component_configer.component_configer import \
    ComponentConfiger


class TokenTextSplitter(DocProcessor):
    chunk_size: int = 200
    chunk_overlap: int = 20
    encoding_name: str = 'gpt2'
    model_name: Optional[str] = None
    splitter: Optional[Splitter] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.splitter = Splitter(
            encoding_name=self.encoding_name,
            model_name=self.model_name,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def _process_docs(self, origin_docs: List[Document], query: Query = None) -> \
            List[Document]:
        lc_doc_list = self.splitter.split_documents(Document.as_langchain_list(
            origin_docs
        ))
        return Document.from_langchain_list(lc_doc_list)

    def _initialize_by_component_configer(self,
                                         doc_processor_configer: ComponentConfiger) -> 'DocProcessor':
        super()._initialize_by_component_configer(doc_processor_configer)
        if hasattr(doc_processor_configer, "chunk_size"):
            self.chunk_size = doc_processor_configer.chunk_size
        if hasattr(doc_processor_configer, "chunk_overlap"):
            self.chunk_overlap = doc_processor_configer.chunk_overlap
        if hasattr(doc_processor_configer, "encoding_name"):
            self.encoding_name = doc_processor_configer.encoding_name
        if hasattr(doc_processor_configer, "model_name"):
            self.model_name = doc_processor_configer.model_name
        self.splitter = Splitter(
            encoding_name=self.encoding_name,
            model_name=self.model_name,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )
        return self