from swarm import Swarm, Agent # Swarmライブラリ
from dotenv import load_dotenv # APIキー読み込み用
import os

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")

# Swarmクライアントの初期化
client = Swarm()

# 関数定義: エージェント間の連携を定義
def transfer_to_eco_agent():
    return eco_agent

def transfer_to_ethics_agent():
    return ethics_agent

# 各マルチエージェントのクラス定義
triage_agent = Agent(
    name="トリアージエージェント",  # エージェントの名前
    model="gpt-4o-mini", # モデル名
    # エージェントへの指示
    instructions="ユーザーの提案に対し、経済エージェントと倫理エージェントを使用して、経済学のみの見解と倫理学のみの見解をまず回答に表示してください。その上で、両者の意見から中立的な回答を表示してください",
)

eco_agent = Agent(
    name="経済エージェント",
    model="gpt-4o-mini",
    instructions="ユーザーの提案に対して、経済学の見地のみから是非を判断してください。倫理など別の観点の判断は、別のエージェントが実行する為行わないでください。",
)

ethics_agent = Agent(
    name="倫理エージェント",
    model="gpt-4o-mini",
    instructions="ユーザーの提案に対して、倫理やモラルの見地のみから是非を判断してください。経済学など別の観点の判断は、別のエージェントが実行する為行わないでください。",
)


# クエスト内容
user_message = {"role": "user", "content": "日本政府が積極的に円安誘導して、国の基幹産業である自動車産業の輸出をより有利にすれば日本の景気は回復すると思います。この提案についてどう考えますか。"}

# Step 1: 経済エージェントからの見解を取得
eco_response = client.run(agent=eco_agent, messages=[user_message])
eco_content = eco_response.messages[-1]["content"]

# Step 2: 倫理エージェントからの見解を取得
ethics_response = client.run(agent=ethics_agent, messages=[user_message])
ethics_content = ethics_response.messages[-1]["content"]

# Step 3: トリアージエージェントによる総合判断
# 経済エージェントと倫理エージェントの見解を含めてトリアージエージェントに渡す
combined_message = {
    "role": "user",
    "content": f"経済的見解: {eco_content}\n倫理的見解: {ethics_content}\nこれらを考慮して、総合的な判断を示してください。",
}

triage_response = client.run(agent=triage_agent, messages=[combined_message])
final_content = triage_response.messages[-1]["content"]

# 出力
print("経済的見解:\n", eco_content)
print("倫理的見解:\n", ethics_content)
print("総合的判断:\n", final_content)