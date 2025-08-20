def build_prompt(price, bids, asks, prev_price):
    print("🧠 build_prompt 開始")

    # 差分計算
    diff = price - prev_price
    rate = (diff / prev_price) * 100 if prev_price != 0 else 0
    direction = "上昇" if diff > 0 else "下落" if diff < 0 else "変化なし"

    # 板情報から価格を数値に変換
    bid_price = float(bids[0]['price'])
    ask_price = float(asks[0]['price'])
    spread = ask_price - bid_price

    prompt = f"""
あなたはプロの暗号資産トレーダーです。
ETH/JPYの価格・板情報・スプレッド・価格変化・短期モメンタムなどを考慮し、
以下のテンプレートに従って、1つの最適戦略を出力してください。

【テンプレート】
---
📊 ETH/JPY 戦略通知（リアルタイム）

- 💰 現在価格：{price:,.0f}円  
- 🔄 直近との価格変化：{direction}（{diff:+,.1f}円／{rate:+.2f}%）  
- 📉 板情報：買い板 {bid_price:,.0f}円 ／ 売り板 {ask_price:,.0f}円  
- 📏 スプレッド：{spread:,.0f}円  
- 📈 戦略判断：ロングエントリー／ショートエントリー／様子見（いずれか1つ）  
- 🎯 利確ライン：現在の価格と相場状況から適切な価格を予測して記入してください  
- ⛑️ ロスカットライン：リスク管理を考慮して記入してください  

🧠 理由：板の厚さ、価格推移、スプレッド、短期トレンドなどを加味して、1〜2文で判断根拠を述べてください。
---

【補足】
- 上位3件 板情報：
    🟩 Bids: {bids[:3]}
    🟥 Asks: {asks[:3]}
- スプレッド幅：{spread:,.0f}円

※テンプレート以外の出力は禁止。形式を守って簡潔に出力してください。
"""

    return prompt.strip()
