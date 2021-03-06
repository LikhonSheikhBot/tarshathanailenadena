import telegram
from telegram import message
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import ParseMode
from catge_selenium import bogged, bscscan
from datetime import date
import requests

# Bot token
telegram_bot_token = "5070028001:AAHD0PJdWlgueiGVXpsFaVa8Ydq8hKI3QHY"
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher
job = updater.job_queue
message = ''


def get_prices():

    crypto_data = requests.get("https://api.pancakeswap.info/api/v2/tokens/0x3e07a8a8f260edeeca24139b6767a073918e8674").json()
    burned_api = requests.get('https://api.bscscan.com/api?module=account&action=tokenbalance&contractaddress=0x3e07a8a8f260edeeca24139b6767a073918e8674&address=0x000000000000000000000000000000000000dead&tag=latest&apikey=EIDB6X2C6SNDVGD7STTYTYZ5BXKP2ZRG8B').json()
    bnb_price = requests.get('https://api.bscscan.com/api?module=stats&action=bnbprice&apikey=EIDB6X2C6SNDVGD7STTYTYZ5BXKP2ZRG8B').json()

    return crypto_data, burned_api, bnb_price


def start(context):
    chat_id = '@testing_area'
    global message
    message = ''
    boggedf = bogged()
    bsc_scan = bscscan()
    crypto_data = get_prices()[0]
    coin = crypto_data["data"]["name"]
    symbol = crypto_data["data"]["symbol"]
    price = float(crypto_data["data"]["price"])
    price_per_m = round((float(price) * 1000000), 6)
    price_per_m = str(price_per_m).replace('.', ',')
    bnb_busd = get_prices()[2]['result']['ethusd'].replace('.', ',')
    holders = bsc_scan
    burned = str(1000000000000000 - int(boggedf[0].replace(',', '')))[0:3]
    c_supply = boggedf[0][0:5]
    mcap = boggedf[1].replace('.', ',')
    volume = boggedf[2]    

    message += f"๐ {symbol} ๐๐ \n\n<b>๐ค 1M tokens</b> ${price_per_m}\n\n<b>๐ฒ Market Cap</b> {mcap}\n\n<b>๐ฐ Circulating Supply</b> {c_supply}t\n\n<b>๐ฆ BNB/BUSD</b> {bnb_busd}\n\n<b>๐จโ๐งโ๐ฆ Holders</b> {holders}\n\n<b>๐ต Total Supply</b> 1quad\n\n<b>๐ฐ Volume 24h</> {volume}\n\n<b>๐ฅ Burned Tokens</b> {burned}t"

    context.bot.send_photo(chat_id=chat_id, photo=open('chart_logo.png', 'rb'), caption=message, parse_mode=ParseMode.HTML)


def old_chart(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('chart_logo.png', 'rb'), caption=message, parse_mode=ParseMode.HTML)

def catge_info(update, context):
    buy_sell = '<a href="https://exchange.pancakeswap.finance/\#/swap?outputCurrency=0x3e07a8a8f260edeeca24139B6767A073918E8674&inputCurrency=BNB"> PancakeSwapV2 </a> | <a href="https://poocoin.app/swap?outputCurrency=0x3e07a8a8f260edeeca24139b6767a073918e8674"> PooCoin Swap </a>'
    cg_chart = '<a href="https://www.coingecko.com/en/coins/catge-coin"> Coingecko </a>'
    cmc_chart = '<a href="https://coinmarketcap.com/currencies/catge-coin/"> CoinMarketCap </a>'
    faq = '<a href="https://t.me/catgecoin/139694"> FAQ </a>'
    reddit = '<a href="https://www.reddit.com/r/catgearmy/"> Reddit </a>'
    twitter = '<a href="https://twitter.com/catgecoinoff"> Twitter </a>'
    discord = '<a href="https://discord.gg/NYf7E4Qs3f"> Discord </a>'
    charts = '<a href="https://ach.tools/#/tabs/home/0x3e07a8a8f260edeeca24139b6767a073918e8674">๐?๏ธ ACH </a> <a href="https://poocoin.app/tokens/0x3e07a8a8f260edeeca24139b6767a073918e8674">๐ฉ PooCoin </a> <a href="https://www.foolstools.net/token/0x3e07a8a8f260edeeca24139b6767a073918e8674">โ?๏ธ Fool\'sTools </a>'
    today = date.today()
    launched = (today - date.fromisoformat('2021-06-27')).days

    information = f'<b>๐ฑ Buy/Sell</b>{buy_sell}\n\n<b>๐ฆ Chart</b> {cg_chart}\n\n<b>๐ Chart</b> {cmc_chart}\n\n<b>โ Help</b> {faq}\n\n<b>๐จโ๐ฆโ๐ฆ Social</b> {reddit}\n\n<b>๐ฆ Social</b> {twitter}\n\n<b>๐ง Social</b> {discord}\n\n<b>๐ Charts</b> {charts}\n\n<b>โฒ๏ธ Time Since Launch</b> {launched} days ago'

    context.bot.send_message(chat_id=update.effective_chat.id, message=information, parse_mode=ParseMode.HTML)

job_hourly = job.run_repeating(start, 3600, 10)
dispatcher.add_handler(CommandHandler("chart", old_chart))
dispatcher.add_handler(CommandHandler("info", catge_info))

updater.start_polling()
