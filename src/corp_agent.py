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
def transfer_to_corp_agent():
    return corp_agent

def transfer_to_labor_agent():
    return labor_agent

# 各マルチエージェントのクラス定義
triage_agent = Agent(
    name="トリアージエージェント",  # エージェントの名前
    model="gpt-4o-mini", # モデル名
    # エージェントへの指示、役割を記載
    instructions="ユーザーの提案に対し、法人エージェントと労働者エージェントを使用して、両者の意見を引き出してください。両者の意見を紹介したうえで、より優れた意見を選択してください",
    functions=[transfer_to_labor_agent,transfer_to_corp_agent],
)

corp_agent = Agent(
    name="法人エージェント",
    model="gpt-4o-mini",
    instructions="ユーザーの提案に対して、法人経営者の立場から意見してください。",
)

labor_agent = Agent(
    name="労働者エージェント",
    model="gpt-4o-mini",
    instructions="企業に雇われて働く労働者の立場で、法人エージェントが出した意見を引用したうえで、反論してください。",
#    instructions="企業に雇われて働く労働者の立場で、法人エージェントが出した意見を引用したうえで、反論してください。",
#    functions=[transfer_to_corp_agent],
)


# エージェント起動
response = client.run(
    agent=triage_agent,
    # 入力プロンプト。討論すべきテーマをここに書く。
    messages=[{"role": "user", "content": "退職金はこれまで退職時に一括支給していたが、来年から月々の給料に上乗せして、先払いの形に変更したい。"}],
)

print(response.messages[-1]["content"])