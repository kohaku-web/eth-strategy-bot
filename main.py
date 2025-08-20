import requests
import openai

# 🔑 OpenAI APIキー
openai.api_key = "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"  # ←自分のキーに書き換えてください

# 🔔 Discord Webhook URL
WEBHOOK_URL = "https://discordapp.com/api/webhooks/1407617625319538779/nbfVIuC_had2m_aZl693-oKLWqj80kPqA51Y_KkQfyxG8NtXaIipX-xByLcSUZKBglnc"  # ←自分のURLに書き換えてください

# ① GMOコインの価格と板データを取得
def get_market_data():
    print("① get_market_data 実行")
    ticker_url = "https://api.coin.z.com/public/v1/ticker?symbol=ETH_JPY"
    board_url = "https://api.coin.z.com/public/v1/orderbooks?symbol=ETH_JPY"

    print("✅ get_market_data 開始")
    ticker_res = requests.get(ticker_url)
    board_res = requests.get(board_url)

    price = float(ticker_res.json()['data'][0]['last'])
    print(f"🟩 現在価格: {price}")

    bids = board_res.json()['data']['bids'][:1]  # 買い板 上位1件
    asks = board_res.json()['data']['asks'][:1]  # 売り板 上位1件

    return price, bids, asks

# ② ChatGPT用プロンプトを生成
def build_prompt(price, bids, asks):
    print("② build_prompt 実行")
    print("✅ build_prompt 開始")
    prompt = f"""
あなたは暗号資産のトレーディングアドバイザーです。
以下の情報を元に、ETH/JPYに関する「短期の戦略（ロング/ショート/様子見）」を日本語で1文で判断してください。

■ 現在価格：{price} 円
■ 板情報：
- 売り板：{asks[0][0]}円（{asks[0][1]}ETH）
- 買い板：{bids[0][0]}円（{bids[0][1]}ETH）

判断だけを一言で答えてください。
"""
    print("📤 生成されたプロンプト:\n", prompt)
    return prompt

# ③ ChatGPTで戦略を判断
def get_strategy(prompt):
    print("③ get_strategy 実行")
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
    print("💬 ChatGPT戦略判断：", strategy)
    return strategy

# ④ Discord通知
def send_to_discord(message):
    print("④ send_to_discord 実行")
    payload = {
        "content": f"📊 **ETH/JPY 戦略通知**\n{message}"
    }
    res = requests.post(WEBHOOK_URL, json=payload)
    print(f"🔁 Discord Response: {res.status_code} - {res.text}")
    if res.status_code == 204:
        print("✅ Discord通知 成功")
    else:
        print("⚠️ Discord通知 失敗")

# ⑤ メイン処理
def main():
    try:
        price, bids, asks = get_market_data()
        prompt = build_prompt(price, bids, asks)
        strategy = get_strategy(prompt)
        send_to_discord(strategy)
    except Exception as e:
        print("❌ エラー発生：", e)

if __name__ == "__main__":
    main()
