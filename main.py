import requests
import openai

# 🔑 あなたのOpenAI APIキーをここに貼ってください
openai.api_key = "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"

# 🔔 Discord Webhook URLをここに貼ってください
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1407591919646937098/U4T-h85SzS5fX-9WJBfPKs5U23amYH0rgxTpDb4-aVjmXXjHo0XT5dq0Dc_sBMR7ReVg"

# ① GMOコインの価格と板データを取得
def get_market_data():
    print("✅ get_market_data 開始")
    ticker_url = "https://api.coin.z.com/public/v1/ticker?symbol=ETH_JPY"
    board_url = "https://api.coin.z.com/public/v1/orderbooks?symbol=ETH_JPY"

    ticker_res = requests.get(ticker_url)
    board_res = requests.get(board_url)

    price = float(ticker_res.json()['data'][0]['last'])
    bids = board_res.json()['data']['bids'][:3]  # 買い板 上位3件
    asks = board_res.json()['data']['asks'][:3]  # 売り板 上位3件

    print(f"📊 現在価格: {price}")
    return price, bids, asks

# ② ChatGPT用プロンプトを生成
def build_prompt(price, bids, asks):
    print("✅ build_prompt 開始")
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
    return prompt

# ③ ChatGPTで戦略を判断
def get_strategy(prompt):
    print("✅ get_strategy 開始")
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "あなたはプロの仮想通貨トレーダーです。"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.3,
    )
    return response['choices'][0]['message']['content'].strip()

# ④ Discord通知
def send_to_discord(message):
    print("✅ send_to_discord 開始")
    payload = {
        "content": f"📊 **ETH/JPY 戦略通知**\n{message}"
    }
    res = requests.post(WEBHOOK_URL, json=payload)
    print(f"🔁 Discord Response: {res.status_code} - {res.text}")
    if res.status_code == 204:
        print("✅ Discord通知 成功")
    else:
        print("⚠️ Discord通知 失敗")

# ⑤ 実行（main関数）
if __name__ == "__main__":
    def main():
        try:
            print("① get_market_data 実行")
            price, bids, asks = get_market_data()

            print("② build_prompt 実行")
            prompt = build_prompt(price, bids, asks)

            print("③ get_strategy 実行")
            strategy = get_strategy(prompt)

            print("④ ChatGPT判断：", strategy)

            print("⑤ send_to_discord 実行")
            send_to_discord(strategy)
        except Exception as e:
            print("❌ エラー発生：", e)

    main()
