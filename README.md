# agentUniverse
****************************************
Language version: [English](./README.md) | [中文](./README_zh.md) | [日本語](./README_jp.md)

![](https://img.shields.io/badge/framework-agentUniverse-pink)
![](https://img.shields.io/badge/python-3.10%2B-blue?logo=Python)
[![](https://img.shields.io/badge/%20license-Apache--2.0-yellow)](LICENSE)
[![Static Badge](https://img.shields.io/badge/pypi-v0.0.13-blue?logo=pypi)](https://pypi.org/project/agentUniverse/)

![](docs/guidebook/_picture/logo_bar.jpg)
****************************************

## What is agentUniverse?

**agentUniverse is a multi-agent framework based on large language models. It provides flexible and easily extensible capabilities for building individual agents. The core of agentUniverse is a rich set of multi-agent collaborative pattern components (serving as a collaborative pattern factory), which allows agents to perform their respective duties and maximize their capabilities when solving problems in different fields; at the same time, agentUniverse focuses on the integration of domain experience, helping you smoothly integrate domain experience into the work of intelligent agents.🎉🎉🎉

**🌈🌈🌈agentUniverse helps developers and enterprises easily build powerful agents at the domain expert level to work collaboratively for you.**

![](docs/guidebook/_picture/agent_universe_framework_resize.jpg)

We look forward to your practice and communication and sharing of Patterns in different fields through the community. This framework has already placed many useful components that have been tested in real business scenarios in terms of multi-agent cooperation, and will continue to be enriched in the future.
The pattern components that are currently open for use include:

* PEER pattern component: This pattern uses agents with different responsibilities—Plan, Execute, Express, and Review—to break down complex problems into manageable steps, execute the steps in sequence, and iteratively improve based on feedback, enhancing the performance of reasoning and analysis tasks. Typical use cases: Event interpretation, industry analysis.
* DOE pattern component: This pattern employs three agents—Data-fining, Opinion-inject, and Express—to improve the effectiveness of tasks that are data-intensive, require high computational precision, and incorporate expert opinions. Typical use cases: Financial report generation.

More patterns are coming soon...

****************************************

## Citation

The agentUniverse project is supported by the following research achievements.

BibTeX formatted
```text
@misc{wang2024peerexpertizingdomainspecifictasks,
      title={PEER: Expertizing Domain-Specific Tasks with a Multi-Agent Framework and Tuning Methods}, 
      author={Yiying Wang and Xiaojing Li and Binzhu Wang and Yueyang Zhou and Han Ji and Hong Chen and Jinshi Zhang and Fei Yu and Zewei Zhao and Song Jin and Renji Gong and Wanqing Xu},
      year={2024},
      eprint={2407.06985},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2407.06985}, 
}
```
Overview: This document introduces in detailed the mechanisms and principles underlying the PEER multi-agent framework. The experimental section assigned scores across seven dimensions: completeness, relevance, conciseness, factualness, logicality, structure, and comprehensiveness, with a maximum score of 5 points for each dimension. On average, the PEER model scored higher in each evaluation dimension compared to BabyAGI, and show notable advantages particularly in completeness, relevance, logicality, structure, and comprehensiveness. Furthermore, when tested with the GPT-3.5 Turbo (16k) model, the PEER model achieved a superior accuracy rate of 83% compared to BabyAGI, and with the GPT-4 model, it achieved an accuracy rate of 81%. For more details, please refer to the document. 
🔗https://arxiv.org/pdf/2407.06985

****************************************

## Table of Contents

* [Quick Start](#Quick-Start)  
* [How to build an agent application](#How-to-build-an-agent-application)
* [Setup the visual agentic workflow platform](#Setup-the-visual-agentic-workflow-platform)
* [Why use agentUniverse](#Why-use-agentUniverse)  
* [Sample Projects](#Sample-Projects)  
* [Documents](#Documents)  
* [Support](#Support)

****************************************
## Quick Start

### Installation
Using pip:
```shell
pip install agentUniverse
```
### Run the first example
Run your first example, and you can quickly experience the performance of the agents (or agent groups) built by agentUniverse through the tutorial.

Please refer to the document for detail steps: [Run the first example](docs/guidebook/en/Get_Start/Quick_Start.md) 。

****************************************

## How to build an agent application

### Standard Project Scaffolding
Setup the standard project: [agentUniverse Standard Project](examples/sample_standard_app)

### Create and use agents
You can learn about the important components of agents through the [Introduction to Agents](docs/guidebook/en/In-Depth_Guides/Tutorials/Agent/Agent.md). For detailed information on creating agents, refer to [Creating and Using Agents](docs/guidebook/en/In-Depth_Guides/Tutorials/Agent/Agent_Create_And_Use.md). You can also deepen your understanding of the creation and usage of agents by exploring official examples, such as the [Python Code Generation and Execution Agent](docs/guidebook/en/Examples/Python_Auto_Runner.md).

### Setting and use knowledgeBase
In the development of intelligent agent applications, knowledge base construction and recall are indispensable. The agentUniverse framework, based on RAG technology, offers an efficient standard operating procedure for knowledge base construction and managing the retrieval and recall process of RAG. You can learn about its usage through the [Knowledge Introduction](docs/guidebook/en/In-Depth_Guides/Tutorials/Knowledge/Knowledge.md) and [Knowledge Definition and Usage](docs/guidebook/en/In-Depth_Guides/Tutorials/Knowledge/Knowledge_Define_And_Use.md), and further hone your skills in quickly building a knowledge base and creating an agent capable of retrieval and recall through [How to Build RAG Agents](docs/guidebook/en/How-to/How_To_Build_A_RAG_Agent.md).

### Create and use Tools
In the development of agent applications, agents need to connect to a variety of tools. You should specify a range of tools that they can utilize. You can integrate various proprietary APIs and services as tool plugins through [Tool Creation and Usage](docs/guidebook/en/In-Depth_Guides/Tutorials/Tool/Tool_Create_And_Use.md). The framework has already integrated LangChain as well as several third-party toolkits. For detailed instructions on how to use thses tools, you can refer to [Integrating LangChain Tools](docs/guidebook/en/In-Depth_Guides/Components/Tools/Integrated_LangChain_Tools.md) and [Existing Integrated Tools](docs/guidebook/en/In-Depth_Guides/Components/Tools/Integrated_Tools.md).

### Effectiveness evaluation
The effectiveness evaluation of agents can be conducted through expert assessments, on the one hand, and by leveraging the evaluation capabilities of the agents themselves, on the other hand. The agentUniverse framework has launched DataAgent (Minimum Viable Product version), which aims to empower your agents with self-evaluation and evolution capabilities utilizing agent intelligence. You can also customize the evaluation criteria within it. For more details, please refer to the documentation:  [DataAgent - Autonomous Data Agents](docs/guidebook/en/In-Depth_Guides/Tutorials/Data_Autonomous_Agent.md).

### agentServe
agentUniverse provides multiple standard web server capabilities, as well as standard HTTP and RPC protocols. You can further explore the documentation on [Service Registration and Usage](docs/guidebook/en/In-Depth_Guides/Tech_Capabilities/Service/Service_Registration_and_Usage.md) and the [Web Server](docs/guidebook/en/In-Depth_Guides/Tech_Capabilities/Service/Web_Server.md) sections.

****************************************

## Setup the visual agentic workflow platform

agentUniverse provides a visual canvas platform for creating agentic workflow. Follow these steps for a quick start:

**Using pip**
```shell
pip install magent-ui ruamel.yaml
```

**One-click Run**

Run [product_application.py](examples/sample_standard_app/boostrap/platform/product_application.py) in sample_standard_app/boostrap/platform for quick startup.

For more details, refer to [Quick Start for Product Platform](docs/guidebook/en/How-to/Product_Platform_Quick_Start.md) and the [Advanced Guide](docs/guidebook/en/How-to/Product_Platform_Advancement_Guide.md).

This feature is jointly developed by [difizen](https://github.com/difizen/magent) and agentUniverse.

****************************************

## Why use agentUniverse

### Concept
![](docs/guidebook/_picture/agentuniverse_structure.png)

The core of agentUniverse provides all the essential components needed to build a single intelligent agent, the collaboration mechanisms between multiple agents, and allows for the injection of expert knowledge. The enables developers to effortlessly create intelligent applications equipped with professional know-how.

### Multi Agent Collaboration
AgentUniverse offers several multi-agent collaboration model components that have been validated in real-world industries. Among these, the "PEER" model stands out as one of the most distinctive.

The PEER model utilizes agents with four distinct responsibilities: Planning, Executing, Expressing, and Reviewing. This structure allows for the decomposition and step-by-step execution of complex problems and enables autonomous iteration based on evaluation feedback, ultimately enhancing performance in reasoning and analytical tasks. This model is particularly effective in scenarios that require multi-step decomposition and in-depth analysis, such as event interpretation, macroeconomic analysis, and the feasibility analysis of business proposals.

The PEER model has achieved impressive results, and the latest research findings and experimental data can be found in the following literature.

### Key Features
Based on the above introduction, we summarize the main features of agentUniverse as follow:

Flexible and Extensible Agent Construction Capability: It provides all the essential components necessary for building agents, all of which support customization to tailor user-specific agents.

Rich and Effective Multi-Agent Collaboration Models: It offers collaborative models such as PEER (Plan/Execute/Express/Review) and DOE (Data-finding/Opinion-inject/Express), which have been validated in the industry. Users can also customize and orchestrate new models to facilitate organic collaboration among multiple agents.

Easy Integration of Domain Expertise: It offers capabilities for domain prompts, knowledge construction, and management, enabling the orchestration and injection of domain-level SOPs, aligning agents with expert-level domain knowledge.

💡 For additional features:
see the section on [key features of agentUniverse](docs/guidebook/en/Concepts/Core_Features.md) for more details.

****************************************

## Sample Projects

🚩 [Legal Advice Agent v2](docs/guidebook/en/Examples/Legal_Advice.md)

🚩 [Python Code Generation and Execution Agent](docs/guidebook/en/Examples/Python_Auto_Runner.md)

🚩 [Discussion Group Based on Multi-Turn Multi-Agent Mode](docs/guidebook/en/Examples/Discussion_Group.md)

🚩 [Financial Event Analysis Based on PEER Multi-Agent Mode](docs/guidebook/en/Examples/Financial_Event_Analysis.md)

🚩 [Andrew Ng's Reflexive Workflow Translation Agent Replication](docs/guidebook/en/Examples/Translation_Assistant.md)

****************************************

## Commercial Product base on agentUniverse

🔗 [_Zhi Xiao Zhu_-AI Assistant for Financial Professionals](https://zhu.alipay.com/?from=au)

**_Zhi Xiao Zhu_ AI Assistant: Designed to facilitate the development of large models in rigorous industries to enhance the productively of investment research experts**

_Zhi Xiao Zhu_ AI Assistant an efficient solution for the practical application of large models in rigorous industries. It is built upon the Finix model, which emphasizes precise applications, and leverages the agentUniverse intelligent agent framework, known for its professional customization capabilities. This solution targets a range of professional AI business assistants related to investment research, ESG (environmental, social, and governance), finance, earnings reports, and other specialized domains. It has been extensively validated in large-scale scenarios at Ant Group, significantly improving expert efficiency.

https://private-user-images.githubusercontent.com/39180831/355437700-192f712d-1b03-46a6-8422-1ca10aa94331.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5NDk4NTAsIm5iZiI6MTcyMjk0OTU1MCwicGF0aCI6Ii8zOTE4MDgzMS8zNTU0Mzc3MDAtMTkyZjcxMmQtMWIwMy00NmE2LTg0MjItMWNhMTBhYTk0MzMxLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA2VDEzMDU1MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU4NWMzNzVjOGZjZDNjMDMzMTE4YjQzOTk0ZWQwZGZkNWNmNWQxNWMzYWIzMTk4MzY1MjA5NWRhMjU2NGNiNzUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.q1vdSg_Ghxr-DHLXfmQ_fVVRVSFn7H8VMHMi-_2QrjA

****************************************

## Documents

### User Guide
💡 For more detailed information, please refer to the [User Guide](./docs/guidebook/en/Contents.md).

### API Reference
💡 Please consult the [API Reference](https://agentuniverse.readthedocs.io/en/latest/) for technical details.

****************************************

## Support

### Submit Questions via GitHub Issues
😊 We recommend submitting your queries using [GitHub Issues](https://github.com/antgroup/agentUniverse/issues), we typically respond within 2 business days.

### Contact Us via Discord
😊 Join our [Discord Channel](https://discord.gg/DHFcdkWAhn) to interact with us.

### Contact Us via Administrator Email
😊 Email: 
* [jihan.hanji@antgroup.com](mailto:jihan.hanji@antgroup.com)
* [jerry.zzw@antgroup.com](mailto:jerry.zzw@antgroup.com)
* [jinshi.zjs@antgroup.com](mailto:jinshi.zjs@antgroup.com)

### twitter
ID: [@agentuniverse_](https://x.com/agentuniverse_)

### Acknowledgements

This project is partially built upon excellent open-source projects such as Langchain, Pydantic, Gunicorn, Flask, SQLAlchemy, chromadb, etc. (The detailed dependency list can be found in pyproject.toml). We would like to express our heartfelt gratitude to the related projects and their contributors. 🙏🙏🙏
