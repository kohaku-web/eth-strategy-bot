import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def get_strategy(prompt):
    print("🤖 get_strategy 開始")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたはプロの仮想通貨トレーダーです。"},
            {"role": "user", "content": prompt}
        ]
    )

    strategy = response['choices'][0]['message']['content'].strip()
    return strategy
