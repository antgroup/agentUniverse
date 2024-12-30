# agentUniverse
****************************************
言語バージョン: [英語](./README.md) | [中国語](./README_zh.md) | [日本語](./README_jp.md)

![](https://img.shields.io/badge/framework-agentUniverse-pink)
![](https://img.shields.io/badge/python-3.10%2B-blue?logo=Python)
[![](https://img.shields.io/badge/%20license-Apache--2.0-yellow)](LICENSE)
[![Static Badge](https://img.shields.io/badge/pypi-v0.0.13-blue?logo=pypi)](https://pypi.org/project/agentUniverse/)

![](docs/guidebook/_picture/logo_bar.jpg)
****************************************

## 概要
agentUniverseは、大規模言語モデルに基づくマルチエージェントアプリケーションを開発するためのフレームワークです。単一エージェントの構築に必要なすべての基本コンポーネントと、マルチエージェントのコラボレーションメカニズムを提供します。これにより、開発者はマルチエージェントアプリケーションを簡単に構築し、異なる技術およびビジネス分野からのパターンプラクティスを共有することができます。

フレームワークには、実際のビジネスシナリオで効果が証明されたいくつかのプリインストールされたマルチエージェントコラボレーションパターンが含まれており、今後も豊富になる予定です。現在リリース予定のパターンには以下が含まれます：

- PEERパターン：
このパターンは、Plan（計画）、Execute（実行）、Express（表現）、Review（レビュー）の4つの異なるエージェントの役割を利用して、複雑なタスクを多段階に分解し、順次実行します。また、評価フィードバックに基づいて自律的な反復を行い、推論および分析タスクのパフォーマンスを向上させます。

- DOEパターン：
このパターンは、Data-fining（データ精製）、Opinion-inject（意見注入）、Express（表現）の3つのエージェントで構成され、データ集約型および高計算精度のタスクを解決し、事前に収集および構造化された専門家の意見と組み合わせることで、最終結果を生成します。

これからもっと多くのパターンが登場します...

![](docs/guidebook/_picture/agent_universe_framework_resize.jpg)

## agentUniverseサンプルプロジェクト
[agentUniverse サンプルプロジェクト](examples/sample_standard_app/README.md)

## クイックインストール
pipを使用：
```shell
pip install agentUniverse
```

## クイックスタート
以下の内容をご紹介します：
* 環境とアプリケーションプロジェクトの準備
* シンプルなエージェントの構築
* パターンコンポーネントを使用してマルチエージェントのコラボレーションを完了する
* エージェントのパフォーマンスをテストおよび最適化する
* エージェントを迅速に提供する
詳細は、[クイックスタート](docs/guidebook/en/1_3_Quick_Start.md)をご覧ください。

## 使用ケース
[法律相談Agent](./docs/guidebook/en/7_1_1_Legal_Consultation_Case.md)

[Pythonコード生成と実行Agent](./docs/guidebook/en/7_1_1_Python_Auto_Runner.md)

[多回多Agentによるディスカッショングループ](./docs/guidebook/en/6_2_1_Discussion_Group.md)

[PEERマルチAgentモードに基づいた金融イベント分析](./docs/guidebook/en/6_4_1_Financial_Event_Analysis_Case.md)

## ガイドブック
詳細情報については、[ガイドブック](docs/guidebook/en/0_index.md)を参照してください。

## APIリファレンス
[readthedocs](https://agentuniverse.readthedocs.io/en/latest/)

## お問い合わせ
* github: https://github.com/antgroup/agentUniverse
* gitee: https://gitee.com/agentUniverse/agentUniverse
* gitcode: https://gitcode.com/agentUniverse
* Stack Overflow: https://stackoverflowteams.com/c/agentuniverse/questions
* Discord: https://discord.gg/DHFcdkWAhn
* WeChat公式アカウント: agentUniverse智多星
