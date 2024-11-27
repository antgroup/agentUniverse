# agentUniverse
****************************************
语言版本: [English](./README.md) | [中文](./README_zh.md) | [日本語](./README_jp.md)

![](https://img.shields.io/badge/framework-agentUniverse-pink)
![](https://img.shields.io/badge/python-3.10%2B-blue?logo=Python)
[![](https://img.shields.io/badge/%20license-Apache--2.0-yellow)](LICENSE)
[![Static Badge](https://img.shields.io/badge/pypi-v0.0.13-blue?logo=pypi)](https://pypi.org/project/agentUniverse/)

![](docs/guidebook/_picture/logo_bar.jpg)
****************************************

## agentUniverse是什么？

**agentUniverse 是一个基于大型语言模型的多智能体框架。** agentUniverse为您提供灵活易拓展的单智能体构建能力；agentUniverse核心拥有丰富的多智能体协同模式组件（可视为一个协同模式工厂Pattern Factory），它能让智能体们各司其职在解决不同领域问题时发挥最大的能力；同时agentUniverse专注于领域经验的融合，帮助您轻松将领域经验融入到智能体的工作中。🎉🎉🎉

**🌈🌈🌈agentUniverse帮助开发者、企业轻松构建出领域专家级别的强大智能体协同为您工作。**

![](docs/guidebook/_picture/agent_universe_framework_resize.jpg)

我们期待您通过社区对不同领域的Pattern进行实践与交流共享，框架也预置有若干已在真实产业中验证有效的多智能体协作模式组件，并在未来持续丰富。目前即将开放的模式组件包括：
* PEER 模式组件： 该pattern通过计划（Plan）、执行（Execute）、表达（Express）、评价（Review）四个不同职责的智能体，实现对复杂问题的多步拆解、分步执行，并基于评价反馈进行自主迭代，最终提升推理分析类任务表现。典型适用场景：事件解读、行业分析
* DOE 模式组件： 该pattern通过数据精制（Data-fining）、观点注入（Opinion-inject）、表达（Express）三个智能体，实现对数据密集、高计算精度、融合专家观点的生成任务的效果提升。典型适用场景：财报生成

更多模式组件持续推出中...

****************************************
## 目录
* [快速开始](#快速开始)
* [案例与样例工程](#案例与样例工程)
* [更多](#更多)
  * [为什么使用agentUniverse](#为什么使用agentUniverse)
  * [核心特性](#核心特性)
  * [用户指南](#用户指南)
  * [API参考](#API参考)
  * [支持](#支持)
  * [文献](#文献)
  * [鸣谢](#鸣谢)
****************************************
## 快速开始
使用pip：
```shell
pip install agentUniverse
```

我们将向您展示如何：
* 进行环境与应用工程准备
* 构建一个简单的agent
* 使用模式组件完成多agent协同
* 对agent执行效果进行测试调优
* 对agent进行快速服务化

详情请阅读[快速开始](docs/guidebook/zh/1_3_%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.md) 。
****************************************
## 产品化平台使用
agentUniverse提供基于本地的产品化平台能力，请按照如下步骤快速启动

**通过pip安装**
```shell
pip install magent-ui ruamel.yaml
```

**一键运行**

运行sample_standard_app/boostrap下的[product_application.py](sample_standard_app/boostrap/platform/product_application.py)文件，一键启动。

更多详情参考 [产品化平台快速开始](./docs/guidebook/zh/10_1_1_产品化平台快速开始.md)
与 [产品化平台进阶指南](./10_1_2_产品化平台进阶指南.md) 。

本功能由 [difizen](https://github.com/difizen/magent) X agentUniverse联合推出。

****************************************
## 案例与样例工程
### 🌟 使用案例
[法律咨询Agent_v2](./docs/guidebook/zh/7_1_1_法律咨询案例.md)

[Python代码生成与执行Agent](./docs/guidebook/zh/7_1_1_Python自动执行案例.md)

[基于多轮多Agent的讨论小组](./docs/guidebook/zh/6_2_1_讨论组.md)

[基于PEER协同模式的金融事件分析](./docs/guidebook/zh/6_4_1_金融事件分析案例.md)

[吴恩达反思工作流翻译智能体复刻](./docs/guidebook/zh/7_1_1_翻译案例.md)

#### 🚩 如何快速构建RAG智能体
RAG组件全面升级，教程提供一个在agentUniverse中快速构建一个RAG智能体，可查看文档[如何构建RAG智能体](./docs/guidebook/zh/2_2_4_如何构建RAG智能体.md)，更多原理性内容可查看文档[RAG介绍](./docs/guidebook/zh/2_2_4_RAG.md)。

#### 🚩 DataAgent - 数据自治智能体
agentUniverse推出了DataAgent（Minimum Viable Product版本）, DataAgent旨在使用智能体能力让您的Agent拥有自我评价与演进的能力。详情见文档: [DataAgent - 数据自治智能体](./docs/guidebook/zh/8_1_1_数据自治智能体.md)

### 🌟 示例项目
[agentUniverse 示例项目](sample_standard_app)

### 🌟 使用aU构建的产品案例
[支小助 金融从业专家AI助手](https://zhu.alipay.com/?from=au)

****************************************

**投研支小助：助推大模型落地严谨产业，提升投研专家效率**

投研支小助是大模型落地严谨产业的高效解决方案，基于专注严谨应用的凤凰大模型和善于专业定制的agentUniverse智能体框架，主要面向投研、ESG、财经、财报等投研相关细分领域的一系列专业AI业务助手，已在蚂蚁大规模场景充分验证，提升专家效率。


https://private-user-images.githubusercontent.com/39180831/355437700-192f712d-1b03-46a6-8422-1ca10aa94331.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjI5NDk4NTAsIm5iZiI6MTcyMjk0OTU1MCwicGF0aCI6Ii8zOTE4MDgzMS8zNTU0Mzc3MDAtMTkyZjcxMmQtMWIwMy00NmE2LTg0MjItMWNhMTBhYTk0MzMxLm1wND9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA4MDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwODA2VDEzMDU1MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTU4NWMzNzVjOGZjZDNjMDMzMTE4YjQzOTk0ZWQwZGZkNWNmNWQxNWMzYWIzMTk4MzY1MjA5NWRhMjU2NGNiNzUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.q1vdSg_Ghxr-DHLXfmQ_fVVRVSFn7H8VMHMi-_2QrjA


****************************************
## 更多
### 为什么使用agentUniverse
💡 [为什么使用agentUniverse?](./docs/guidebook/zh/1_为什么选择agentUniverse.md)

### 核心特性

* **丰富的多智能体协同模式：** 提供PEER（Plan/Execute/Express/Review）、DOE（Data-fining/Opinion-inject/Express）等产业中验证有效的协同模式，同时支持用户自定义编排新模式，让多个智能体有机合作；

* **所有组件均可定制：** LLM、知识、工具、记忆等所有框架组件均提供自定义能力，供用户来增强专属智能体；

* **轻松融入领域经验：** 提供领域prompt、知识构建与管理的能力，同时支持领域级SOP编排与注入，将智能体对齐至领域专家级别；

💡 更多特点见[agentUniverse核心特性](docs/guidebook/zh/1_核心特性.md)部分。

### 用户指南
💡 更多详细信息，请阅读[用户指南](docs/guidebook/zh/0_%E7%9B%AE%E5%BD%95.md) 。

### API参考
💡 请阅读[readthedocs](https://agentuniverse.readthedocs.io/en/latest/) 。

### 支持
#### 通过github issue提交疑问
😊 我们建议您使用[github issue](https://github.com/alipay/agentUniverse/issues) 提交您的疑问, 我们通常会在2日内回复。

#### 通过Discord联系我们
😊 加入我们的 [Discord频道](https://discord.gg/DHFcdkWAhn) 与我们进行交流。

#### 通过钉钉群联系我们
😊 加入我们的钉钉答疑群与我们联系。
![](./docs/guidebook/_picture/dingtalk_util20250429.png)

#### 通过管理员Email联系我们
😊 Email: [jerry.zzw@antgroup.com](mailto:jerry.zzw@antgroup.com)

#### 微信公众号

😊 公众号ID：**agentUniverse智多星**

![](./docs/guidebook/_picture/wechat_official.png)

更多相关的文章与资讯你可以在微信公众号中获取。

#### twitter
ID: [@agentuniverse_](https://x.com/agentuniverse_)

### 文献
agentUniverse项目基于以下的研究成果支撑。

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
文献简介：该文献详细介绍了介绍了PEER多智能体框架的机制原理，同时在实验部分分别从**完整性、相关性、紧凑性、事实性、逻辑性、结构性和全面性七个维度进行打分（各纬度满分为5分）**，PEER模式在每个测评维度的平均分数均高于BabyAGI，且在**完整性、相关性、逻辑性、结构性和全面性五个纬度有显著优势**；同时PEER模式在 GPT-3.5 turbo (16k) 模型下相较于 BabyAGI 的择优胜率达到 83%，在 GPT-4o 模型下择优胜率达到 81%，更多详情请阅读文献。
https://arxiv.org/pdf/2407.06985

## 鸣谢
本项目部分基于langchain、pydantic、gunicorn、flask、SQLAlchemy、chromadb等（详细依赖列表可见pyproject.toml）优秀开源项目实现，在此特别感谢相关项目与关联方。 🙏🙏🙏
