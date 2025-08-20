import os
import openai

openai.api_key = os.getenv("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")

def get_strategy(prompt):
    print("🧠 get_strategy 開始")
    try:
        client = openai.OpenAI(api_key=openai.api_key)

        response = client.chat.completions.create(
            model="gpt-4o",  # ← ここを "gpt-4o" に
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
