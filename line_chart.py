import requests
import schedule
import time
import pickle

# Load prices and time
try:
    stored_prices = pickle.load( open('stored_prices.p', 'rb'))
    prices_time = pickle.load( open('prices_time.p', 'rb'))
except:
    stored_prices = []
    prices_time = []

def get_prices():
    t = time.localtime()
    current_time = time.strftime("%A:%H:%M", t)

    crypto_data = requests.get("https://api.pancakeswap.info/api/v2/tokens/0x3e07a8a8f260edeeca24139B6767A073918E8674").json()
    price = float(crypto_data["data"]["price"])
    stored_prices.append(round((float(price) * 1000000), 6))
    prices_time.append(current_time)

    #Keep only 864 most recent records
    if len(stored_prices) > 864:
        crypto_data.pop(0)
        prices_time.pop(0)

    pickle.dump(stored_prices, open('stored_prices.p', 'wb'))
    pickle.dump(prices_time, open('prices_time.p', 'wb'))

# Function to create backup
def backup_pickle():
    pickle.dump(stored_prices, open('stored_prices_backup.p', 'wb'))
    pickle.dump(prices_time, open('prices_time_backup.p', 'wb'))

# Schedule price snapshot every 5 minutes
schedule.every().hour.at(':00').do(get_prices)
schedule.every().hour.at(':05').do(get_prices)
schedule.every().hour.at(':10').do(get_prices)
schedule.every().hour.at(':15').do(get_prices)
schedule.every().hour.at(':20').do(get_prices)
schedule.every().hour.at(':25').do(get_prices)
schedule.every().hour.at(':30').do(get_prices)
schedule.every().hour.at(':35').do(get_prices)
schedule.every().hour.at(':40').do(get_prices)
schedule.every().hour.at(':45').do(get_prices)
schedule.every().hour.at(':50').do(get_prices)
schedule.every().hour.at(':55').do(get_prices)

# Schedule Backup every 6 hours
schedule.every(6).hours.do(backup_pickle)

while True:
    schedule.run_pending()
    time.sleep(1)