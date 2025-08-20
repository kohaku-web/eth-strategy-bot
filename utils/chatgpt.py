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
