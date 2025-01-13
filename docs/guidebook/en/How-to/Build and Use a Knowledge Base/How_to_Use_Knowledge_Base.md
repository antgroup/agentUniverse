# How to use knowledge base

The config of knowledge utilization is as follows.
```yaml
name: "law_knowledge"
description: "中国民法与刑法相关的知识库"
type: 'using'
stores:
    - "civil_law_chroma_store"
    - "criminal_law_chroma_store"
    - "civil_law_sqlite_store"
    - "criminal_law_sqlite_store"
post_processors:
    - "dashscope_reranker"
metadata:
  type: 'KNOWLEDGE'
  module: 'sample_standard_app.intelligence.agentic.knowledge.law_knowledge'
  class: 'LawKnowledge'
```

## Using Knowledge Base
### Reranker
We have configured the following post-processing component for knowledge.
```yaml
post_processors:
    - "dashscope_reranker"
```
We use rerank service which supported by Dashscope to process the documents. You can also add other post-processing component here.

## Using Knowledge in Agents

```yaml
info:
  name: 'law_rag_agent'
  description: '一个法律顾问，可以根据给出的事件，以及提供的背景知识做出客观的司法判断'
action:
  knowledge:
    - 'law_knowledge'
```
We can configure the knowledge in the Agent's YAML like this.

For more details, please refer to the [documentation](../../Examples/Legal_Advice.md).