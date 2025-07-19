import requests
from telegram.ext import Updater, CommandHandler
import os

def get_pepe_price():
    url = "https://api.coingecko.com/api/v3/coins/pepe"
    response = requests.get(url)
    data = response.json()
    price = data['market_data']['current_price']['usd']
    return f"{price:.10f}"

def start(update, context):
    price = get_pepe_price()
    update.message.reply_text(f"🐸 Pepe Coin Price: ${price}")

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
