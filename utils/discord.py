import requests
import os

def send_to_discord(message):
    print("📤 Discord通知送信 開始")

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        raise ValueError("DISCORD_WEBHOOK_URL が設定されていません")

    payload = {
        "content": f"📣 ETH戦略通知：{message}"
    }

    response = requests.post(webhook_url, json=payload)

    if response.status_code != 204:
        raise Exception(f"Discord送信失敗: {response.status_code}, {response.text}")
