import requests
import traceback

def get_market_data():
    print("🔍 get_market_data 開始")
    try:
        response = requests.get("https://api.coin.z.com/public/v1/orderbooks?symbol=ETH_JPY")
        print("🛰️ API レスポンス取得")
        data = response.json()
        print("📦 レスポンス内容取得")

        bids = data["data"]["bids"]
        asks = data["data"]["asks"]

        print("🟩 bids[0]:", bids[0])
        print("🟥 asks[0]:", asks[0])

        # ✅ 正しく辞書から取得
        price = (float(bids[0]["price"]) + float(asks[0]["price"])) / 2
        print("💰 現在価格:", price)

        return price, bids, asks

    except Exception as e:
        print("🚨 get_market_data で例外発生:", e)
        traceback.print_exc()
        raise
