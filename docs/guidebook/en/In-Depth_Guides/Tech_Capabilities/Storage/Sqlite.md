## Sqlite

The SQLite component within the Store module is utilized to store the textual content of Documents and construct a corresponding inverted index based on the keyword extraction capability of Jieba. During the retrieval phase, relevant documents are retrieved using keywords, and the relevance score between the query and the retrieved texts is computed using the BM25 algorithm. Ultimately, the system returns the Top k most similar documents.

### How to Configure the SQLite Component

You can use ChromaDB to store and query knowledge in the [Knowledge Components](../../../In-Depth_Guides/Tutorials/Knowledge/Knowledge.md). You can create a storage component using SQLite with the following configuration:
```yaml
name: 'sqlite_store'
description: 'a store based on sqlite'
db_path: '../../DB/civil_law_sqlite.db'
k1: 1.5
b: 0.75
keyword_extractor: 'jieba_keyword_extractor'
similarity_top_k: 10
metadata:
  type: 'STORE'
  module: 'agentuniverse.agent.action.knowledge.store.sqlite_store'
  class: 'SQLiteStore'
```
- db_path: The path to the SQLite database file, utilized for storing and managing textual data.
- k1:  The k1 parameter in the BM25 algorithm, which regulates the impact of term frequency on the scoring.
- b: The b parameter in the BM25 algorithm, which modulates the influence of document length on the scoring.
- keyword_extractor: The tool designated for keyword extraction, specified here as jieba_keyword_extractor.
- similarity_top_k: Returns the top k most similar documents based on the BM25 score.

### Usage
[Knowledge_Define_And_Use](../../../In-Depth_Guides/Tutorials/Knowledge/Knowledge_Define_And_Use.md)