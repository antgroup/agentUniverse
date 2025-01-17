# Data Autonomous Agent
## Introduction
The comprehensive view of the Data Autonomous Agent: By **automated batch execution of multiple rounds of agent invocation**, **offline adaptive data collection**, **production of evaluation datasets**, **production of fine-tuning datasets**, **model inference training**, and **automatic multidimensional assessment of datasets**, a complete workflow is established to enhance the data autonomy process of large language models and Agents.

The current agentUniverse has released the **Data Autonomous MVP (Minimum Viable Product) version**.  This version, based on the **query sets** specified by the user, performs **automated batch execution of multiple rounds of agent invocation**, **produces evaluation datasets**, **automatically assesses datasets in multiple dimensions**, and **generates evaluation reports**. It introduces the concept of data autonomy to the open-source community, and will gradually unlock the full capabilities of the data autonomous workflow in the future.

## Background
Currently, the evaluation of agent performance within the industry often relies heavily on the expertise of specialists in specific fields, who conduct extensive manual review and annotation to ensure the high quality and accuracy of assessment results.

The dataAgent, within the agentUniverse framework, aims to leverage the agent's own capabilities for **self-collect**, **self-manage**, and **intelligently evaluate the data of the Agent**.

In the MVP version of agentUniverse, the  `dataset_build_agent` can be utilized to make multiple rounds of batch invocation on the query sets that need to be evaluated, thereby producing evaluation datasets. Subsequently,  the  `dataset_eval_agent` applies the **Fin-Eva** data evaluation standards published by Ant Group, which encompass seven dimensions (relevance, factuality, rationality, timeliness, structure, integrity, and comprehensiveness), to conduct intelligent data assessment and annotation. The results from multiple rounds of evaluation undergo comprehensive statistical analysis,  providing users with a more intuitive understanding of the Agent's capabilities changes.

By harnessing the complete set of data autonomy capabilities within agentUniverse, users can effortlessly ascertain their Agent's current performance level through intelligently generated evaluation reports.
It is particularly important to note that the scores in the entire evaluation report serve as reference values. In an actual production environment, a comprehensive comparison of scores from multiple rounds will be conducted to accurately assess the Agent's effectiveness.

## DataAgent Flowchart
![data_agent_flowchart](../../../_picture/data_agent_flowchart.jpg)
- data_agent consists of two parts. **dataset_build_agent** iis responsible for automating batch execution of multiple rounds of agent invocation and producing evaluation datasets.
- **dataset_eval_agent** is responsible for automating the multidimensional evaluation of the dataset and generating evaluation report.

## DataAgent Execution Steps
### Step1 Establish Agent Queryset
In the DataAgent framework, the initial step involves constructing an agent queryset in the JSONL (JSON Lines) file format. Each line within this file represents a complete input for an individual agent invocation. 

To illustrate, consider establishing a queryset that contains 3 items. Each item should include an "input" field, which corresponds to the query information specifically for the agent. Here's how it might look:
```jsonl
{"input": "Help me predict the 2024 European Cup championship"}
{"input": "Can Tesla's stock still be bought?"}
{"input": "What's the weather in New York today?"}
```

### Step2 Configure DataAgent
CWhen configuring the DataAgent within the AgentUniverse framework, the configuration file, in addition to the basic agent settings, primarily includes two crucial items:  `dataset_builder` , which corresponds to the name of the agent responsible for generating the evaluation dataset, and `dataset_evaluator`, which corresponds to the name of the agent tasked with dataset evaluation and annotation.
```yaml
info:
  name: 'data_agent'
  description: 'data agent'
profile:
  dataset_builder: 'dataset_build_agent'
  dataset_evaluator: 'dataset_eval_agent'
metadata:
  type: 'AGENT'
  module: 'data_agent_app.intelligence.agentic.agent.agent_instance.data_agent_case.data_agent'
  class: 'DataAgent'
```
[data_agent sample configuration file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/data_agent.yaml)

[data_agent sample python file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/data_agent.py)

### Step3 Configure the agent for producing the evaluation dataset.
Utilize the **dataset_build_agent** configured in the `dataset_builder`step of step 2 within the agentuniverse framework. Below is the configuration file for the dataset_build_agent. In addition to the basic agent configuration,  the configuration file primarily comprises two key items: 
1. `candidate` , which specifies the name of the agent to be evaluated (for instance, to assess the effectiveness of demo_rag_agent, candidate should be set to demo_rag_agent).
2. `concurrency_level` ,  which configures the concurrency level during batch agent invocation (for example, setting it to 5 means that the candidate agent will be invoked concurrently with 5 instances).
```yaml
info:
  name: 'dataset_build_agent'
  description: 'dataset build agent'
profile:
  concurrency_level: 1
  candidate: 'demo_rag_agent'
metadata:
  type: 'AGENT'
  module: 'data_agent_app.intelligence.agentic.agent.agent_instance.data_agent_case.dataset_build_agent'
  class: 'DatasetBuildAgent'
```
[dataset_build_agent sample configuration file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/dataset_build_agent.yaml)

[dataset_build_agent sample python file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/dataset_build_agent.py)

### Step4 Configure the agent for dataset evaluation and annotation
Utilize the **dataset_eval_agent** configured in the `dataset_evaluator`step of step 2 within the AgentUniverse framework. Below is the configuration file for the dataset_eval_agent. In addition to the basic agent configuration, the configuration file primarily contains two key items:
1. `llm_model` , which configures the agent's model.
2. `max_eval_lines` , which specifies the maximum number of evaluation data lines (for instance, setting it to 10 means that only the first 10 rows of data will be evaluated, to avoid a full-scale evaluation and the consumption of a large number of tokens).
```yaml
info:
  name: 'dataset_eval_agent'
  description: 'dataset eval agent'
profile:
  prompt_version: dataset_eval_agent.cn
  max_eval_lines: 10
  llm_model:
    name: 'qwen_llm'
    model_name: 'qwen2-72b-instruct'
    temperature: 0.1
metadata:
  type: 'AGENT'
  module: 'data_agent_app.intelligence.agentic.agent.agent_instance.data_agent_case.dataset_eval_agent'
  class: 'DatasetEvalAgent'
```
[dataset_eval_agent sample configuration file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/dataset_eval_agent.yaml)

[dataset_eval_agent sample python file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/dataset_eval_agent.py)

### step5 Run DataAgent
Using the [dataAgent code entry](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/data_agent.py), configure two parameters:
1. `queryset_path`, which representing the path to the queryset.
2. `turn`, which specifies the total number of rounds for the queryset execution. With these configurations, you can start the dataAgent with a single click.

Tips: please configure the queryset and specific the evaluation rows reasonably to avoid excessive computational and token consumption.

## DataAgent Example Usage
Please refer to the **DataAgent Execution Steps** mentioned previously, and follow these five steps to start the configured dataAgent.

### Evaluation Dataset
First, you need to generate the evaluation dataset. This dataset should store the agent's Q&A pairs in the JSONL file format. Each line in the file will represent a single Q&A pair, formatted as follows:
- query: agent question 
- answer: agent answer

![data_agent_dataset](../../../_picture/data_agent_dataset_en.png)

[dataAgent sample evaluation dataset](../../../../../examples/sample_apps/data_agent_app/intelligence/test/data/dataset_turn_1_2024-07-10-15-06-24.jsonl)


### Complete Evaluation Results
After generating the evaluation dataset, the dataagent begins multidimensional data assessment and annotation, producing complete evaluation results. (If multiple rounds of dataAgent batch tasks are executed, multiple set of complete evaluation results will be generated.)

As illustrated in the figure below:
- Line Number: Indicates the line number of the current evaluation data within the dataset.
- Overall Score:  A comprehensive score calculated as the total of assessment scores from multiple dimensions divided by the number of assessment dimensions (with a full score of 5 and a score range of 0-5).
- Query: The question posed to the agent.
- Answer: The agent's response to the question.
- Relevance Score: Represents the relevance of the agent's answer to the question. A higher score indicates greater relevance (with a full score of 5 and a score range of 0-5).
- Relevance Suggestion: Provides issues and suggestions for improvement in the relevance dimension.
- Additional Dimension Scores/Suggestions: Similar to the Relevance dimension, but for other assessment dimensions.
![data_agent_eval_result](../../../_picture/data_agent_eval_result_en.png)

[dataAgent sample eval result](../../../../../examples/sample_apps/data_agent_app/intelligence/test/data/eval_result_turn_1_2024-07-10-15-06-24.xlsx)



### Comprehensive Evaluation Report
Generate a comprehensive evaluation report based on multiple sets of complete evaluation results.

As illustrated in the figure below:
- Line Name: Includes two types of entries. One is `Queryset Turn x`, representing the evaluation dataset generated in the x-th round based on the queryset. The other is `Turn Avg Score`,which represents the average score across multiple rounds and dimensions.
- Overall Avg Score: This is calculated as the sum of the overall scores of all data entries in a single round of the dataset divided by the total number of data entries in that dataset (with a full score of 5 and a score range of 0-5).
- Relevance Avg Score: This is calculated as the sum of the relevance scores of all data entries in a single round of the dataset divided by the total number of data entries in that dataset (with a full score of 5 and a score range of 0-5).
- Additional Dimension Avg Scores: These are similar to the Relevance Avg Score but pertain to other assessment dimensions.

![data_agent_eval_report](../../../_picture/data_agent_eval_report_en.png)

[dataAgent sample evaluation report](../../../../../examples/sample_apps/data_agent_app/intelligence/test/data/eval_report_2024-07-10-15-06-24.xlsx)

### Comparative Experiment
Adjust the LLM model in the demo_rag_agent within agentUniverse from the previous `qwen1.5-72b-chat` to `qwen1.5-7b-chat`, and after evaluation by dataAgent, the comprehensive evaluation reports are as follows:

The following figure presents the comprehensive evaluation report generated by the data autonomous agent when the model is qwen1.5-7b-chat:

![data_agent_eval_report](../../../_picture/data_agent_eval_report_en_qwen7b.png)

The subsequent figure displays the comprehensive evaluation report produced by the data autonomous agent when the model is 
![data_agent_eval_report](../../../_picture/data_agent_eval_report_en.png)
Upon comparing the two comprehensive evaluation reports, it is evident that after switching the agent's LLM model from qwen1.5-7b-chat to qwen1.5-72b-chat, there was a notable increase in scores across all dimensions and in multiple rounds. This approach allows for a swift distinction in agent performance following changes to the agent configuration.

## DataAgent Detailed Description
### data_agent
- [configuration file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/data_agent.yaml)
- [agent file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/data_agent.py)

### dataset_build_agent
- [configuration file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/dataset_build_agent.yaml)
- [agent file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/dataset_build_agent.py)
- The evaluation data produced by dataset_build_agent is stored locally in jsonl format (the jsonl file name is dataset_turn_{i}_{date}, i represents the round, and `date` represents the generation time)

### dataset_eval_agent
- [configuration file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/dataset_eval_agent.yaml)
- [agent file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/agent/agent_instance/data_agent_case/dataset_eval_agent.py)
- [prompt file](../../../../../examples/sample_apps/data_agent_app/intelligence/agentic/prompt/dataset_eval_agent_en.yaml)：agentUniverse currently offers six agent evaluation dimensions that are industry-validated (note that the MVP version does not include the **comprehensive dimension**. The current comprehensive evaluation standard is tailored towards the financial field, and therefore, it is not discussed in the open source community).
- The complete **evaluation results** generated by **dataset_eval_agent** are stored locally in Excel format. The file naming convention is **eval_result_turn_{i}_{date}**, where  `i` represents the evaluation round and `date` represents the generation timestamp.
- The comprehensive **evaluation report** produced by **dataset_eval_a_agent** (assuming it's a typo and should be dataset_eval_agent or a specific variant) is also stored locally in Excel format. The file naming convention for the report is **eval_report_{date}**, where **{date}** represents the generation timestamp.