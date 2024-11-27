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

**agentUniverse is a multi-agent framework based on large language models.** agentUniverse provides you with the flexible and easily extensible capability to build single agents. At its core, agentUniverse features a rich set of multi-agent collaboration mode components (which can be viewed as a Collaboration Mode Factory, or Pattern Factory). These components allow agents to maximize their effectiveness by specializing in different domains to solve problems. agentUniverse also focuses on the integration of domain expertise, helping you seamlessly incorporate domain knowledge into the work of your agents.🎉🎉🎉

**🌈🌈🌈agentUniverse helps developers and enterprises to easily build powerful collaborative agents that perform at an expert level in their respective domains.**

![](docs/guidebook/_picture/agent_universe_framework_resize.jpg)

We encourage you to practice and share different domain Patterns within the community. The framework comes pre-loaded with several multi-agent collaboration mode components that have been validated in real-world industries and will continue to expand in the future. The components that will be available soon include:

* PEER Mode Component: This pattern uses agents with different responsibilities—Plan, Execute, Express, and Review—to break down complex problems into manageable steps, execute the steps in sequence, and iteratively improve based on feedback, enhancing the performance of reasoning and analysis tasks. Typical use cases: Event interpretation, industry analysis.
* DOE Mode Component: This pattern employs three agents—Data-fining, Opinion-inject, and Express—to improve the effectiveness of tasks that are data-intensive, require high computational precision, and incorporate expert opinions. Typical use cases: Financial report generation.

More patterns are coming soon...

****************************************
## Table of Contents
* [Quick Start](#Quick-Start)
* [Cases and Example Projects](#Cases-and-Example-Projects)
* [More](#More)
  * [Why Use agentUniverse](#Why-Use-agentUniverse)
  * [Core Features](#Core-Features)
  * [User Guide](#User-Guide)
  * [API Reference](#API-Reference)
  * [Support](#Support)
  * [Citation](#Citation)
  * [Acknowledgements](#Acknowledgements)
****************************************
## Quick Start
Using pip:
```shell
pip install agentUniverse
```

We will show you how to:

* Prepare the environment and application projects
* Build a simple agent
* Use mode components for multi-agent collaboration
* Test and tune the execution effectiveness of an agent
* Quickly deploy an agent as a service

For more details, please read the [Quick Start](./docs/guidebook/en/1_3_Quick_Start.md).

****************************************
## Using the Product Platform
agentUniverse provides a local product platform capability. Please follow the steps below for a quick start:

**Install via pip**
```shell
pip install magent-ui ruamel.yaml
```

**One-click Run**

Run the [product_application.py](sample_standard_app/boostrap/platform/product_application.py) file located in sample_standard_app/bootstrap for a one-click start.

For more details, refer to [Quick Start for Product Platform](./docs/guidebook/en/10_1_1_Product%20Platform%20Quick%20Start.md) and the [Advanced Guide](./docs/guidebook/en/10_1_2_Product_Platform_Advancement_Guide.md).

This feature is jointly launched by [difizen](https://github.com/difizen/magent) and agentUniverse.

****************************************

## Cases and Example Projects
### 🌟 Use Cases
[Legal Consultation Agent v2](./docs/guidebook/en/7_1_1_Legal_Consultation_Case.md)

[Python Code Generation and Execution Agent](./docs/guidebook/en/7_1_1_Python_Auto_Runner.md)

[Discussion Group Based on Multi-Turn Multi-Agent Mode](./docs/guidebook/en/6_2_1_Discussion_Group.md)

[Financial Event Analysis Based on PEER Multi-Agent Mode](./docs/guidebook/en/6_4_1_Financial_Event_Analysis_Case.md)

[Andrew Ng's Reflexive Workflow Translation Agent Replication](./docs/guidebook/en/7_1_1_Translation_Case.md)

#### 🚩 How to Quickly Build an RAG Agent
The RAG components have been fully upgraded. This tutorial provides a guide on how to quickly build an RAG agent in agentUniverse. You can refer to the documentation on [How to Build a RAG Agent](./docs/guidebook/en/2_2_4_How_To_Build_A_RAG_Agent.md). For more theoretical content, please check the documentation on [Introduction to RAG](./docs/guidebook/en/2_2_4_RAG.md).

#### 🚩 DataAgent - Data Autonomous Agent
agentUniverse has launched DataAgent (Minimum Viable Product Version). DataAgent aims to empower your agent with the capability of self-assessment and evolution through the use of intelligent agent abilities. For more details, please refer to the documentation. [DataAgent - Data Autonomous Agent](./docs/guidebook/en/8_1_1_data_autonomous_agent.md)

### 🌟 Example Projects
[agentUniverse Example Projects](sample_standard_app)

### 🌟 Product Cases Built with agentUniverse
['Zhi Xiao Zhu' AI Assistant for Financial Professionals](https://zhu.alipay.com/?from=au)

****************************************

**'Zhi Xiao Zhu' AI Assistant: Facilitate the implementation of large models in rigorous industries to enhance the efficiency of investment research experts**

'Zhi Xiao Zhu' AI Assistant is an efficient solution for the practical application of large models in rigorous industries. It is based on the Finix model, which focuses on precise applications, and the agentUniverse intelligent agent framework, which excels in professional customization. This solution targets a range of professional AI business assistants related to investment research, ESG (Environmental, Social, and Governance), finance, earnings reports, and other specialized areas. It has been extensively validated in large-scale scenarios at Ant Group, enhancing expert efficiency.


https://private-user-images.githubusercontent.com/39180831/355437700-192f712d-1b03-46a6-8422-1ca10aa94331.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5NDk4NTAsIm5iZiI6MTcyMjk0OTU1MCwicGF0aCI6Ii8zOTE4MDgzMS8zNTU0Mzc3MDAtMTkyZjcxMmQtMWIwMy00NmE2LTg0MjItMWNhMTBhYTk0MzMxLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA2VDEzMDU1MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU4NWMzNzVjOGZjZDNjMDMzMTE4YjQzOTk0ZWQwZGZkNWNmNWQxNWMzYWIzMTk4MzY1MjA5NWRhMjU2NGNiNzUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.q1vdSg_Ghxr-DHLXfmQ_fVVRVSFn7H8VMHMi-_2QrjA

****************************************
## More
### Why Use agentUniverse
💡 [Why Use agentUniverse?](./docs/guidebook/en/1_Why_Use_agentUniverse.md)

### Core Features

* **Rich Multi-Agent Collaboration Modes:** Provides industry-validated collaboration modes such as PEER (Plan/Execute/Express/Review) and DOE (Data-fining/Opinion-inject/Express). It also supports user-defined patterns for new modes, enabling organic collaboration among multiple agents.
* **Customizable Components:** All framework components, including LLM, knowledge, tools, and memory, are customizable, allowing users to enhance their dedicated agents.
* **Seamless Integration of Domain Expertise:** Offers capabilities for domain-specific prompts, knowledge construction, and management, and supports domain-level SOP orchestration and embedding, aligning agents to the expert level in their fields.

💡 For more features details, see the [Core Features of agentUniverse](./docs/guidebook/en/1_Core_Features.md).

### User Guide
💡 For more detailed information, please read the [User Guide](./docs/guidebook/en/0_index.md).

### API Reference
💡 Please read the [API Reference](https://agentuniverse.readthedocs.io/en/latest/).

### Support
#### Submit Questions via GitHub Issues
😊 We recommend submitting your queries using [GitHub Issues](https://github.com/alipay/agentUniverse/issues), we typically respond within 2 days.

#### Contact Us via Discord
😊 Join our [Discord Channel](https://discord.gg/DHFcdkWAhn) to interact with us.

#### Contact Us via Administrator Email
😊 Email: 
[jihan.hanji@antgroup.com](mailto:jihan.hanji@antgroup.com)
[jerry.zzw@antgroup.com](mailto:jerry.zzw@antgroup.com)
[jinshi.zjs@antgroup.com](mailto:jinshi.zjs@antgroup.com)

#### twitter
ID: [@agentuniverse_](https://x.com/agentuniverse_)

### Citation
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
Overview: This document provides a detailed introduction to the mechanisms and principles of the PEER multi-agent framework. In the experimental section, scores were assigned across seven dimensions: completeness, relevance, conciseness, factualness, logicality, structure, and comprehensiveness (each dimension has a maximum score of 5 points). The PEER model scored higher on average in each evaluation dimension compared to BabyAGI and demonstrated significant advantages in the dimensions of completeness, relevance, logicality, structure, and comprehensiveness. Additionally, the PEER model achieved a superior rate of 83% over BabyAGI using the GPT-3.5 Turbo (16k) model, and 81% using the GPT-4 model. For more details, please refer to the document.
https://arxiv.org/pdf/2407.06985

## Acknowledgements
This project is partially built on excellent open-source projects such as langchain, pydantic, gunicorn, flask, SQLAlchemy, chromadb, etc. (The detailed dependency list can be found in pyproject.toml). We would like to extend special thanks to the related projects and contributors. 🙏🙏🙏
