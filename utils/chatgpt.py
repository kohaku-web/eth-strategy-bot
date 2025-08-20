import os
import openai

# ✅ 環境変数から安全に読み込む
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_strategy(prompt):
    print("🧠 get_strategy 開始")
    try:
        client = openai.OpenAI(api_key=openai.api_key)

        response = client.chat.completions.create(
            model="gpt-4o",  # 最新高速モデル
            messages=[
                {"role": "system", "content": "あなたはプロの暗号資産トレーダーです。"},
                {"role": "user", "content": prompt}
            ]
        )
        strategy = response.choices[0].message.content.strip()
        print("📈 get_strategy 戦略生成:", strategy)
        return strategy

    except Exception as e:
        print("🚨 get_strategy で例外発生:", e)
        raise
