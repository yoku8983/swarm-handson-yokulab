# swarm-handson-yokulab

## 概要
OpenAIのマルチエージェントAIフレームワーク「Swarm」を試してみる

## 前提条件
OpenAIのAPIキーが必要です（有料）。
APIキーは`.env` ファイルに記述してください。

## 各コードの解説

### `economic_agent.py`
このスクリプトでは、経済学的な問題提起に対して、経済エージェントと倫理エージェントの見解を提供したうえで、総合的な回答を提示します。
- **経済学エージェント**：経済的な視点に基づいた見解を提供します。
- **倫理エージェント**：倫理的な観点からの見解を提供します。
- **トリアージエージェント**：経済学エージェントと倫理エージェントの見解を総合し、中立的な判断を行います。

ただし、GPT自体反倫理的な回答はできないので、マルチエージェントの効果や相互作用は実感しづらいかも。