import requests

def get_market_data():
    print("🔍 get_market_data 開始")
    try:
        response = requests.get("https://api.coin.z.com/public/v1/orderbooks?symbol=ETH_JPY")
        print("🛰️ API レスポンス取得")
        data = response.json()
        print("📦 レスポンス内容取得")

        bids = data["data"]["bids"]
        asks = data["data"]["asks"]
        price = float(bids[0][0])  # 最良買い気配を取得
        print("💰 現在価格:", price)
        return price, bids, asks

    except Exception as e:
        import traceback
        print("🚨 get_market_data で例外発生:", e)
        traceback.print_exc()
        raise  # 上位に再スロー
