# Legal Advice
## Case Description
This case demonstrates a simple legal consultation agent built utilizing `RagPlanner`. The agent provides legal advice by retrieving relevant provisions from the Civil Law and the Criminal Law, and integrating them with the case background.

The case leverages the embedding and reranking features of DashScope in conjunction with the Qwen llm. Before using this, you need to configure the `DASHSCOPE_API_KEY` in your environment variables.

## Components
### Legal Knowledge Base
The legal knowledge base is constructed using [Knowledge Components](../In-Depth_Guides/Tutorials/Knowledge/Knowledge_Related_Domain_Objects.md) from agentUniverse. By storing the original legal provisions in the both ChromaDB and Sqlite database, the knowledge base enables efficient retrieval and consultation for the agent.
Original legal documents
- [民法典.pdf](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/raw_knowledge_file/民法典.pdf)
- [刑法.pdf](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/raw_knowledge_file/刑法.pdf)

### [Knowledge Definition](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/law_knowledge.yaml)
```yaml
name: "law_knowledge"
description: "中国民法与刑法相关的知识库"
stores:
    - "civil_law_chroma_store"
    - "criminal_law_chroma_store"
    - "civil_law_sqlite_store"
    - "criminal_law_sqlite_store"
query_paraphrasers:
    - "custom_query_keyword_extractor"
insert_processors:
    - "recursive_character_text_splitter"
rag_router: "nlu_rag_router"
post_processors:
    - "dashscope_reranker"
readers:
    pdf: "default_pdf_reader"

metadata:
  type: 'KNOWLEDGE'
  module: 'sample_standard_app.intelligence.agentic.knowledge.law_knowledge'
  class: 'LawKnowledge'
```

### Reader Component
- [default_pdf_reader](../../../../agentuniverse/agent/action/knowledge/reader/file/pdf_reader.yaml)

### DocProcessor Component
- [custom_query_keyword_extractor](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/doc_processor/query_keyword_extractor.yaml)
- [recursive_character_text_splitter](../../../../agentuniverse/agent/action/knowledge/doc_processor/recursive_character_text_splitter.yaml)

### QueryParaphraser Component
- [custom_query_keyword_extractor](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/query_paraphraser/custom_query_keyword_extractor.yaml)

### RagRouter Component
- [nlu_rag_router](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/rag_router/nlu_rag_router.yaml)

### Store Component
- [civil_law_chroma_store](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/store/civil_law_chroma_store.yaml)
- [criminal_law_chroma_store](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/store/criminal_law_chroma_store.yaml)
- [civil_law_sqlite_store](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/store/civil_law_sqlite_store.yaml)
- [criminal_law_sqlite_store](../../../../examples/sample_apps/rag_app/intelligence/agentic/knowledge/store/criminal_law_sqlite_store.yaml)

For your convenience, we have placed the databases containing the relevant information in [this directory](../../../../examples/sample_apps/rag_app/db). If you want to build the knowledge base from scratch, you can run the following code:
```python
from agentuniverse.base.agentuniverse import AgentUniverse
from agentuniverse.agent.action.knowledge.knowledge_manager import KnowledgeManager


if __name__ == '__main__':
    AgentUniverse().start(config_path='../../config/config.toml', core_mode=True)
    civil_store_list = ["civil_law_sqlite_store", "civil_law_chroma_store"]
    criminal_store_list = ["criminal_law_sqlite_store", "criminal_law_chroma_store"]
    law_knowledge = KnowledgeManager().get_instance_obj("law_knowledge")
    law_knowledge.insert_knowledge(
        source_path="../resources/刑法.pdf",
        stores=criminal_store_list
    )
    law_knowledge.insert_knowledge(
        source_path="../resources/民法典.pdf",
        stores=civil_store_list
    )
```

### Law Agent
This agent involves the following file:
- [law_rag_agent.yaml](../../../../examples/sample_apps/rag_app/intelligence/agentic/agent/agent_instance/rag_agent_case/law_rag_agent.yaml): Defines the agent's related prompts


### Demonstration Code
[CodeLink](../../../../examples/sample_apps/rag_app/intelligence/test/legal_advice_rag_agent.py)

## Demonstration
![](../../_picture/law_agent_demo.png)
