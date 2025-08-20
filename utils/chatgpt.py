import openai
import os

openai.api_key = os.environ.get("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")

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
