# How to Build a RAG Agent

This tutorial provides a quick guide to building a RAG (Retrieval-Augmented Generation) agent within agentUniverse. The full structure and content of the case can be found in [this document](7_1_1_Legal_Consultation_Case.md). This document focuses on the construction process, so some non-essential content has been omitted.

## Case Description
This case is based on RagPlanner and sets up a simple legal consultation agent that provides relevant legal advice by retrieving applicable articles from the Civil Code and Criminal Code and considering the case background.
The case uses the Qianwen large model and DashScope's embedding and rerank functionalities. Before using it, you need to configure the `DASHSCOPE_API_KEY` in your environment variables.

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
- [民法典.pdf](../../../sample_standard_app/intelligence/agentic/knowledge/raw_knowledge_file/民法典.pdf)
- [刑法.pdf](../../../sample_standard_app/intelligence/agentic/knowledge/raw_knowledge_file/刑法.pdf)

### Extracting Text from PDFs
Since the original documents in this case are in PDF format, we configured the Knowledge component as follows:
```yaml
readers:
    pdf: "default_pdf_reader"
```
This allows the extraction of text from the PDF. If you want to read more file formats, you can refer to the [Reader component](2_2_4_Reader.md).

### Splitting Long Text
Since the text content in the original documents is very long, we need to split it into smaller chunks. Here we use `recursive_character_text_splitter` for splitting, configured as follows:：
```yaml
insert_processors:
    - "recursive_character_text_splitter"
```
This configuration is a list format, allowing multiple document processors to be configured. The only specified processor in this case, recursive_character_text_splitter, recursively splits the original document according to a specified delimiter until it meets the required length. For more details, refer to [DocProcessor](2_2_4_DocProcessor.md). This document also includes other document processors that you can use or customize.

### Configuring the Store
This case includes four Stores: the Civil Law and Criminal Law are stored separately in SQLite and ChromaDB. We will take `civil_law_chroma_store` as an example, with other Stores being similar.
```yaml
name: 'civil_law_chroma_store'
description: '保存了中国民法典的所有内容，以文本向量形式存储'
persist_path: '../../db/civil_law.db'
embedding_model: 'dashscope_embedding'
similarity_top_k: 100
metadata:
  type: 'STORE'
  module: 'agentuniverse.agent.action.knowledge.store.chroma_store'
  class: 'ChromaStore'
```

The `persist_path` specifies the local storage location of the database file and designates `dashscope_embedding` as the component for vectorizing the text in the database. `similarity_top_k` indicates the number of documents to be retrieved. For more details on Store, refer to [this document](2_2_4_Store.md).

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
We specify the data to be inserted using the `source_path` parameter in the `insert_knowledge` method and designate different Stores for different documents using the `stores` parameter. The `stores` parameter is optional; if not specified, the data is inserted into all stores by default.


## Building the Retrieval Process

### Re-ranking
We configured the post-processing flow of the knowledge as follows:
```yaml
post_processors:
    - "dashscope_reranker"
```
This indicates that we will use Dashscope’s re-ranking service to re-rank the documents. You can also add other post-processing flows here.

## Using RAG in the Agent

```yaml
info:
  name: 'law_rag_agent'
  description: '一个法律顾问，可以根据给出的事件，以及提供的背景知识做出客观的司法判断'
action:
  knowledge:
    - 'law_knowledge'
```
We configure the knowledge like this in the YAML file of the Agent.

For the complete case and how to invoke it, please refer to [this document](7_1_1_Legal_Consultation_Case.md).