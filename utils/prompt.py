def build_prompt(price, bids, asks):
    print("🧠 build_prompt 開始")

    prompt = f"""
    あなたはプロの暗号資産トレーダーです。
    現在のETH/JPY価格は{price}円です。

    板情報（上位3件）:
    Bids（買い板）:
    {bids[:3]}
    Asks（売り板）:
    {asks[:3]}

    上記データをもとに、短期戦略（ロング or ショート or 様子見）を日本語で簡潔に1文で判断してください。
    """
    return prompt.strip()
