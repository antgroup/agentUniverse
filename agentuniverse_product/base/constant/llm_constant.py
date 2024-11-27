# !/usr/bin/env python3
# -*- coding:utf-8 -*-

# @Time    : 2024/7/26 10:10
# @Author  : wangchongshi
# @Email   : wangchongshi.wcs@antgroup.com
# @FileName: llm.py
# llm model name list
LLM_MODEL_NAME = {
    'demo_llm': ['gpt-3.5-turbo', 'gpt-4o', 'gpt-4-turbo', 'gpt-4o-mini', 'gpt-4'],
    'default_openai_llm': ['gpt-3.5-turbo', 'gpt-4o', 'gpt-4-turbo', 'gpt-4o-mini', 'gpt-4'],
    'qwen_llm': ['qwen-max', 'qwen-long', 'qwen-turbo', 'qwen2-72b-instruct', 'qwen2-7b-instruct', 'qwen1.5-110b-chat',
                 'qwen1.5-72b-chat', 'qwen1.5-7b-chat', 'qwen2.5-72b-instruct', 'qwen-plus'],
    'default_qwen_llm': ['qwen-max', 'qwen-long', 'qwen-turbo', 'qwen2-72b-instruct', 'qwen2-7b-instruct',
                         'qwen1.5-110b-chat', 'qwen1.5-72b-chat', 'qwen1.5-7b-chat', 'qwen2.5-72b-instruct',
                         'qwen-plus'],
    'wenxin_llm': ['ERNIE-Speed-AppBuilder-8K-0516', 'ERNIE-Lite-8K-0725', 'ERNIE-Speed-128K', 'ERNIE-3.5-128K',
                   'ERNIE-3.5-8K-0701', 'ERNIE-4.0-8K-0613', 'ERNIE-4.0-8K-Preview', 'ERNIE-3.5-8K-Preview',
                   'ERNIE-Tiny-8K', 'ERNIE-4.0-8K-Latest', 'ERNIE-4.0-Turbo-8K'],
    'default_wenxin_llm': ['ERNIE-Speed-AppBuilder-8K-0516', 'ERNIE-Lite-8K-0725', 'ERNIE-Speed-128K', 'ERNIE-3.5-128K',
                           'ERNIE-3.5-8K-0701', 'ERNIE-4.0-8K-0613', 'ERNIE-4.0-8K-Preview', 'ERNIE-3.5-8K-Preview',
                           'ERNIE-Tiny-8K', 'ERNIE-4.0-8K-Latest', 'ERNIE-4.0-Turbo-8K'],
    'kimi_llm': ['moonshot-v1-8k', 'moonshot-v1-32k', 'moonshot-v1-128k'],
    'default_kimi_llm': ['moonshot-v1-8k', 'moonshot-v1-32k', 'moonshot-v1-128k'],
    'deep_seek_llm': ['deepseek-chat', 'deepseek-coder'],
    'default_deepseek_llm': ['deepseek-chat', 'deepseek-coder'],
    'baichuan_llm': ['Baichuan4', 'Baichuan3-Turbo', 'Baichuan3-Turbo-128k', 'Baichuan2-Turbo', 'Baichuan2-Turbo-192k'],
    'default_baichuan_llm': ['Baichuan4', 'Baichuan3-Turbo', 'Baichuan3-Turbo-128k', 'Baichuan2-Turbo',
                             'Baichuan2-Turbo-192k'],
}
