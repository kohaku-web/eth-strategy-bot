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
