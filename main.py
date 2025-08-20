import requests
import openai
import traceback

# 🔑 OpenAI APIキー
openai.api_key = "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"

# 🔔 Discord Webhook URL
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1407617625319538779/nbfVIuC_had2m_aZl693-oKLWqj80kPqA51Y_KkQfyxG8NtXaIipX-xByLcSUZKBglnc"

# ① 価格＆板データ取得
def get_market_data():
    print("① get_market_data 実行")
    print("✅ get_market_data 開始")

    ticker_url = "https://api.coin.z.com/public/v1/ticker?symbol=ETH_JPY"
    board_url = "https://api.coin.z.com/public/v1/orderbooks?symbol=ETH_JPY"

    ticker_res = requests.get(ticker_url)
    board_res = requests.get(board_url)

    price = float(ticker_res.json()['data'][0]['last'])
    bids = board_res.json()['data']['bids'][:3]
    asks = board_res.json()['data']['asks'][:3]

    print("📈 現在価格:", price)
    return price, bids, asks

# ② プロンプト生成
def build_prompt(price, bids, asks):
    print("② build_prompt 実行")
    print("✅ build_prompt 開始")
    print("🛠 bids 内容:", bids)
    print("🛠 asks 内容:", asks)

    prompt = f"""
あなたは暗号資産のトレーディングアドバイザーです。
以下の情報を元に、ETH/JPYに関する「短期の戦略（ロング/ショート/様子見）」を日本語で1文で判断してください。

■ 現在価格：{price} 円
■ 板情報（上位3）：
- 売り板：{asks[0][0]}円（{asks[0][1]}ETH）、{asks[1][0]}円（{asks[1][1]}ETH）、{asks[2][0]}円（{asks[2][1]}ETH）
- 買い板：{bids[0][0]}円（{bids[0][1]}ETH）、{bids[1][0]}円（{bids[1][1]}ETH）、{bids[2][0]}円（{bids[2][1]}ETH）

回答例：
・「今はショートを検討すべき」
・「押し目なのでロングチャンス」
・「様子見が妥当」

判断だけを一言で答えてください。
"""
    print("📤 生成されたプロンプト:\n", prompt)
    return prompt

# ③ ChatGPTで判断
def get_strategy(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたはプロの仮想通貨トレーダーです。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.3,
    )
    strategy = response['choices'][0]['message']['content'].strip()
    return strategy
