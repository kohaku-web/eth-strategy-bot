import json
import os

from utils.market import get_market_data
from utils.prompt import build_prompt
from utils.chatgpt import get_strategy
from utils.discord import send_to_discord

PREV_PRICE_FILE = "prev_price.json"

def load_prev_price():
    if os.path.exists(PREV_PRICE_FILE):
        with open(PREV_PRICE_FILE, "r") as f:
            data = json.load(f)
            return data.get("prev_price", 0)
    return 0

def save_prev_price(price):
    with open(PREV_PRICE_FILE, "w") as f:
        json.dump({"prev_price": price}, f)

def main():
    try:
        print("🚀 main() 開始")

        print("① get_market_data 実行")
        price, bids, asks = get_market_data()
        print("✅ get_market_data 完了 / 現在価格:", price)

        print("🕰️ 直近価格をロード")
        prev_price = load_prev_price()
        print("💾 前回の価格:", prev_price)

        print("② build_prompt 実行")
        prompt = build_prompt(price, bids, asks, prev_price)
        print("✅ build_prompt 完了")

        print("③ get_strategy 実行")
        strategy = get_strategy(prompt)
        print("🤖 ChatGPT判断：", strategy)

        print("④ send_to_discord 実行")
        send_to_discord(strategy)
        print("✅ Discord送信 完了")

        print("💾 現在価格を保存")
        save_prev_price(price)

    except Exception as e:
        import traceback
        print("❌ エラー発生：", e)
        traceback.print_exc()

if __name__ == "__main__":
    main()
