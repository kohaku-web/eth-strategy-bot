import os
from utils.market import get_market_data
from utils.prompt import build_prompt
from utils.chatgpt import get_strategy
from utils.discord import send_to_discord

prev_price = None  # ← グローバル変数で前回価格を保存

def main():
    global prev_price  # ← 前回価格を参照・更新できるように

    try:
        print("🚀 main() 開始")

        # ① 現在の価格と板情報を取得
        price, bids, asks = get_market_data()
        print("✅ get_market_data 完了 / 現在価格:", price)

        # ② プロンプト作成（前回価格がなければ現在価格を基準に）
        if prev_price is None:
            prev_price = price  # 初回は同じ価格で比較
        prompt = build_prompt(price, bids, asks, prev_price)
        print("✅ build_prompt 完了")

        # ③ GPTで戦略を取得
        strategy = get_strategy(prompt)
        print("🤖 ChatGPT判断：", strategy)

        # ④ Discordへ通知
        send_to_discord(strategy)
        print("✅ Discord送信 完了")

        # 次回の比較用に前回価格を更新
        prev_price = price

    except Exception as e:
        import traceback
        print("❌ エラー発生：", e)
        traceback.print_exc()

if __name__ == "__main__":
    main()
