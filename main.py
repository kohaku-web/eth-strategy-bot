from utils.market import get_market_data
from utils.prompt import build_prompt
from utils.chatgpt import get_strategy
from utils.discord import send_to_discord

def main():
    try:
        print("🚀 main() 開始")

        print("① get_market_data 実行")
        price, bids, asks = get_market_data()
        print("✅ get_market_data 完了 / 現在価格:", price)

        print("② build_prompt 実行")
        prompt = build_prompt(price, bids, asks)
        print("✅ build_prompt 完了")

        print("③ get_strategy 実行")
        strategy = get_strategy(prompt)
        print("🤖 ChatGPT判断：", strategy)

        print("④ send_to_discord 実行")
        send_to_discord(strategy)
        print("✅ Discord送信 完了")

    except Exception as e:
        print("❌ エラー発生：", e)

if __name__ == "__main__":
    main()
