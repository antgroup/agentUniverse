# QueryParaphraser

The QueryParaphraser is responsible for processing and refining the original Query, including rewriting, splitting, and keyword extraction. This allows the Query to retrieve more accurate and richer content from the Store. The input and output of the QueryParaphraser are both in the form of a Query, enabling the Query to undergo multiple layers of paraphrasing.


The Query is defined as follows:
```python
from PIL.Image import Image
from typing import Optional, List, Set

from pydantic import BaseModel, Field


class Query(BaseModel):
    query_str: Optional[str] = None
    query_text_bundles: Optional[List[str]] = Field(default_factory=list)
    query_image_bundles: Optional[List[Image]] = Field(default_factory=list)
    keywords: Optional[Set[str]] = Field(default_factory=set)
    embeddings: List[List[float]] = Field(default_factory=list)
    ext_info: dict = {}
    similarity_top_k: Optional[int] = None
```
- query_str: An optional string field used to store the text content of the original query.
- query_text_bundles: An optional list of strings used to store multiple rewritten query text segments.
- query_image_bundles: An optional list of images used to store multiple query images.
- keywords: An optional set field used to store the keywords of the query.
- embeddings: A list of embedding vectors used to store the query's embedding representations for similarity matching.
- ext_info: A dictionary field used to store additional information related to the query, supporting arbitrary extensions.
- similarity_top_k: An optional integer field used to specify the number of most similar results to return in similarity searches.

The QueryParaphraser is defined as follows:
```python
from abc import abstractmethod
from typing import Optional

from agentuniverse.agent.action.knowledge.store.query import Query
from agentuniverse.base.component.component_base import ComponentEnum
from agentuniverse.base.component.component_base import ComponentBase


class QueryParaphraser(ComponentBase):

    component_type: ComponentEnum = ComponentEnum.QUERY_PARAPHRASER
    name: Optional[str] = None
    description: Optional[str] = None

    @abstractmethod
    def query_paraphrase(self, origin_query: Query) -> Query:
        """Paraphrase the origin query string to different style."""
```
When creating a custom subclass of QueryParaphraser, you need to override the query_paraphrase method, with both the input and output in the form of a Query.

After writing the corresponding code, you can refer to the following YAML configuration to register the QueryParaphraser as an aU component:
```yaml
name: 'query_keyword_extractor'
description: 'extract keywords from query origin str'
metadata:
  type: 'QUERY_PARAPHRASER'
  module: 'agentuniverse.agent.action.knowledge.query_paraphraser.query_keyword_extractor'
  class: 'QueryKeywordExtractor'
```
The type in the metadata must be QUERY_PARAPHRASER。
### Pay Attention to the Package Path of Your Custom QueryParaphrase:

In the config.toml file of the agentUniverse project, you need to configure the package path corresponding to your QueryParaphraser. Please double-check whether the path of the file you created is under the query_paraphraser path or its subdirectories in CORE_PACKAGE.

For example, the configuration in the sample project is as follows:
```yaml
[CORE_PACKAGE]
query_paraphraser = ['sample_standard_app.intelligence.agentic.knowledge.query_paraphraser']
```

## The following QueryParaphraser are built into agentUniverse:
### [query_keyword_extractor](../../../../../../agentuniverse/agent/action/knowledge/query_paraphraser/query_keyword_extractor.yaml)
This component extracts keywords from the original text in the Query and saves them into the keywords field of the Query.
The component definition file is as follows:
```yaml
name: 'query_keyword_extractor'
description: 'extract keywords from query origin str'
metadata:
  type: 'QUERY_PARAPHRASER'
  module: 'agentuniverse.agent.action.knowledge.query_paraphraser.query_keyword_extractor'
  class: 'QueryKeywordExtractor'
```