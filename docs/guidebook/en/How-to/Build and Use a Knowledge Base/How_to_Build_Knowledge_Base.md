# How to build knowledge base

The definition of a knowledge construction document is as follows:
```yaml
name: "law_knowledge"
description: "中国民法与刑法相关的知识库"
type: "building"
stores:
    - "civil_law_chroma_store"
    - "criminal_law_chroma_store"
    - "civil_law_sqlite_store"
    - "criminal_law_sqlite_store"
insert_processors:
    - "recursive_character_text_splitter"
readers:
    pdf: "default_pdf_reader"

metadata:
  type: 'KNOWLEDGE'
  module: 'sample_standard_app.intelligence.agentic.knowledge.law_knowledge'
  class: 'LawKnowledge'
```

## Build the knowledge index
legal books:
- [Civil_Law.pdf](../../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/raw_knowledge_file/民法典.pdf)
- [Criminal_Law.pdf](../../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/raw_knowledge_file/刑法.pdf)

### Extract text content from PDF
In this case, since the original document is in PDF format, we made the following configurations in Knowledge:
```yaml
readers:
    pdf: "default_pdf_reader"
```
You can extract text from a PDF. If you want to read files in more formats, you can refer to [Reader Component](../../In-Depth_Guides/Tutorials/Knowledge/Reader.md).

### Split The Text
The original document contains long text, so we need to split it into smaller segments. Here, we will use the `recursive_character_text_splitter` to accomplish this, with the following configuration.
```yaml
insert_processors:
    - "recursive_character_text_splitter"
```

This configuration item is in the form of a list and allows for the configuration of various document processing handlers. In this case, the specified handler, `recursive_character_text_splitter`, will recursively split the original document based on a specified delimiter until a designated length is met. For more details, please refer to [DocProcessor](../../In-Depth_Guides/Tutorials/Knowledge/DocProcessor.md). This document also includes other document processors that you can use directly or customize your own.

### Config Store Component
This case includes four stores: Civil Law and Criminal Law are stored in SQLite and ChromaDB respectively. We will take civil_law_chroma_store as an example, while the other stores are similar.

The configuration for civil_law_chroma_store is as follows:
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

The `persist_path` specifies the storage location for the local database file and designates dashscope_embedding as the component for vectorizing the text in the database. The `similarity_top_k` indicates the number of documents to be recalled. You can find more detailed information about `Store` component in [this document](../../In-Depth_Guides/Tutorials/Knowledge/Store.md).

### Execute Building Process
After completing the above configuration, we can execute the following code to build the knowledge base.
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
We specified the data to be inserted through the `source_path` in the `insert_knowledge` method and used the `stores` parameter to assign different Stores to different documents. The `stores` parameter is optional; if not specified, the data will be inserted into all Stores by default.