import requests

def get_market_data():
    print("🔍 get_market_data 開始")
    url = 'https://api.coin.z.com/public/v1/orderbooks?symbol=ETH_JPY'
    response = requests.get(url)
    data = response.json()

    bids = data['data']['bids']
    asks = data['data']['asks']
    price = (float(bids[0][0]) + float(asks[0][0])) / 2

    print("📈 現在価格:", price)
    return price, bids, asks
