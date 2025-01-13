## Milvus
If you wish to utilize the Milvus vector database within agentUniverse, you need to follow these steps:

1. Install the Milvus vector database
You can consult the [official Milvus installation documentation](https://milvus.io/docs/install_standalone-docker.md) for detailed instructions on installing and using Milvus. As a recommendation, you can start the Milvus container in Docker by executing the following commands:

``` shell
# Download the installation script
$ curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh

# Start the Docker container
$ bash standalone_embed.sh start
```
These commands will download the Milvus image and initiate a container, thereby offering database services on port 19530. For additional information and alternative installation methods, kindly refer to the official documentation.

2. Install the Milvus Python SDK
```
pip install pymilvus
```

### How to Configure Milvus Components
```yaml
name: 'milvus_store'
description: 'a store based on milvus'
connection_args:
  host: '127.0.0.1'
  port: '19530'
search_args:
  metric_type: "L2"
  params:
    nprobe: 10
index_params:
  metric_type: "L2"
  index_type: "HNSW"
  params:
    M: 8
    efConstruction: 32
embedding_model: 'dashscope_embedding'
similarity_top_k: 100
metadata:
  type: 'STORE'
  module: 'agentuniverse.agent.action.knowledge.store.milvus_store'
  class: 'MilvusStore'
```
- connection_args: Parameters required for connecting to the Milvus database, encompassing the host address (host) and port number (port).
- search_args: Search parameters, defining the type of distance metric (metric_type) utilized during searches, along with related parameters such as nprobe.
- index_params: Indexing parameters, specifying the index type (index_type), distance metric type (metric_type), and specific parameters pertinent to index construction, such as M and efConstruction.
- embedding_model: The model employed to generate embedding vectors, specified here as dashscope_embedding.
- similarity_top_k: The number of the most similar results returned in a similarity search.

### Usage
[Knowledge_Define_And_Use](../../../In-Depth_Guides/Tutorials/Knowledge/Knowledge_Define_And_Use.md)

