# How to Build a RAG Agent

This tutorial offers a quick guide to constructing a RAG (Retrieval-Augmented Generation) agent within the agentUniverse framework. The comprehensive structure and detailed content of the case can be found in [this document](../Examples/Legal_Advice.md). However, this document specifically focuses on the construction process, so some non-essential details have been omitted for brevity.

## Case Description
This case is based on RagPlanner and sets up a simple legal consultation agent. This agent provides relevant legal advice by retrieving applicable articles from the Civil Code and Criminal Code, while also considering the case background. The case utilizes the Qianwen large model and DashScope's embedding and reranking functionalities. Before using it, you need to configure the  `DASHSCOPE_API_KEY` in your environment variables.
The knowledge file is defined as follows:
```yaml
name: "law_knowledge"
description: "中国民法与刑法相关的知识库"
stores:
    - "civil_law_chroma_store"
    - "criminal_law_chroma_store"
    - "civil_law_sqlite_store"
    - "criminal_law_sqlite_store"
insert_processors:
    - "recursive_character_text_splitter"
post_processors:
    - "dashscope_reranker"
readers:
    pdf: "default_pdf_reader"

metadata:
  type: 'KNOWLEDGE'
  module: 'sample_standard_app.intelligence.agentic.knowledge.law_knowledge'
  class: 'LawKnowledge'
```

## Building the Knowledge Index

Origin docs：
- [民法典.pdf](../../../../examples/sample_standard_app/intelligence/agentic/knowledge/raw_knowledge_file/民法典.pdf)
- [刑法.pdf](../../../../examples/sample_standard_app/intelligence/agentic/knowledge/raw_knowledge_file/刑法.pdf)

### Extracting Text from PDFs
Since the original documents in this case are in PDF format, we configured the Knowledge component as follows:
```yaml
readers:
    pdf: "default_pdf_reader"
```
This allows the extraction of text from the PDF. If you want to read more file formats, you can refer to the [Reader component](../In-Depth_Guides/Tutorials/Knowledge/Reader.md).

### Splitting Long Text
Since the text content in the original documents is very long, we need to split it into smaller chunks. Here, we use the `recursive_character_text_splitter` ffor splitting, configured as follows:
```yaml
insert_processors:
    - "recursive_character_text_splitter"
```
This configuration is in list format, allowing multiple document processors to be specified. In this case, the only processor specified is recursive_character_text_splitter, which recursively splits the original document according to a specified delimiter until the required length is met. For more details, refer to the  [DocProcessor](../In-Depth_Guides/Tutorials/Knowledge/DocProcessor.md)documentation. Additionally, this framework (agentUniverse) includes other document processors that you can use or customize.

### Configuring the Store
This case includes four Stores: the Civil Law and Criminal Law are stored separately in SQLite and ChromaDB. We will use the `civil_law_chroma_store` as an example, with the other Stores being similar.
```yaml
name: 'civil_law_chroma_store'
description: '保存了中国民法典的所有内容，以文本向量形式存储'
persist_path: '../../DB/civil_law.db'
embedding_model: 'dashscope_embedding'
similarity_top_k: 100
metadata:
  type: 'STORE'
  module: 'agentuniverse.agent.action.knowledge.store.chroma_store'
  class: 'ChromaStore'
```

The `persist_path` specifies the local storage location of the database file and designates `dashscope_embedding` as the component responsible for vectorizing the text within the database. The `similarity_top_k` parameter indicates the number of documents to be retrieved. For more details on Stores, refer to [this document](../In-Depth_Guides/Tutorials/Knowledge/Store.md) or the agentuniverse framework documentation..

### Executing the Insertion Process

After completing the above configurations, you can execute the following code to build the knowledge base:
```python
from agentuniverse.base.agentuniverse import AgentUniverse
from agentuniverse.agent.action.knowledge.knowledge_manager import KnowledgeManager


if __name__ == '__main__':
    AgentUniverse().start(config_path='../../config/config.toml', core_mode=True)
    law_knowledge = KnowledgeManager().get_instance_obj("law_knowledge")
    law_knowledge.insert_knowledge(
        source_path="../resources/刑法.pdf",
        stores=["civil_law_sqlite_store"]
    )
```
We specify the data to be inserted using the `source_path` parameter in the `insert_knowledge` method, and we designate different Stores for different documents by using the  `stores` parameter. The `stores` parameter is optional; if it is not specified, the data will be inserted into all stores by default.

## Building the Retrieval Process

### Re-ranking
We have configured the post-processing flow for the knowledge within the agentuniverse as follows:
```yaml
post_processors:
    - "dashscope_reranker"
```
This configuration indicates that we will utilize Dashscope's re-ranking service to reorder the documents based on relevance. Additionally, you have the option to incorporate other post-processing steps here as needed.

## Using RAG in the Agent

```yaml
info:
  name: 'law_rag_agent'
  description: '一个法律顾问，可以根据给出的事件，以及提供的背景知识做出客观的司法判断'
action:
  knowledge:
    - 'law_knowledge'
```
The specific configuration for the knowledge, as outlined, is defined in the YAML file of the Agent within the agentunivers.
For the complete case and how to invoke it, please refer to  [this document](../Examples/Legal_Advice.md).