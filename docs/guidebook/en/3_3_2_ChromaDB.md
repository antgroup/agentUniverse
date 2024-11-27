## ChromaDB

The agentUniverse already integrates ChromaDB-related dependencies, so you do not need to install additional packages to use ChromaDB's features.
If you want to learn about the underlying principles of ChromaDB, you can visit the [official ChromaDB website](https://www.trychroma.com/).

### How to Configure ChromaDB Components
```yaml
name: 'chroma_store'
description: 'store based on chroma db'
persist_path: '../../DB/criminal_law.db'
embedding_model: 'dashscope_embedding'
similarity_top_k: 100
metadata:
  type: 'STORE'
  module: 'agentuniverse.agent.action.knowledge.store.chroma_store'
  class: 'ChromaStore'
```
- persist_path: The persistence storage path for the database, used for storing and loading vector data.
- embedding_model: The model used to generate embedding vectors, specified here as dashscope_embedding.
- similarity_top_k: The number of most similar results returned in similarity search.

### [ChromaHierarchicalStore](../../../agentuniverse/agent/action/knowledge/store/chroma_hierarchical_store.py)
ChromaHierarchicalStore is a subclass of ChromaStore, used to store document content that includes hierarchical information.   
Here is an example of a definition file for ChromaHierarchicalStore:
```yaml
name: 'chroma_hierarchical_store'
description: 'sample chroma hierarchical store'
persist_path: '../../DB/civil_law_hierarchical.db'
embedding_model: 'dashscope_embedding'
search_depth: 2
similarity_top_k_list:
  - 2
  - 10
metadata:
  type: 'STORE'
  module: 'agentuniverse.agent.action.knowledge.store.chroma_hierarchical_store'
  class: 'ChromaHierarchicalStore'
```
- search_depth: Indicates the depth of the search. The search begins at the top level of the document and proceeds through each level.
- similarity_top_k_list: Specifies the number of documents returned at each search depth. Note that if the first level is set to return 2 documents and the second level is set to return 10, the final result will contain 2 * 10 = 20 documents.

### Usage
[Knowledge_Define_And_Use](2_2_4_Knowledge_Define_And_Use.md)