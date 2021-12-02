import time
import matplotlib.pyplot as plt
import pickle
import schedule
import matplotlib.ticker as plticker
import matplotlib.dates as mdates
from datetime import datetime
from PIL import Image

def create_chart():
    stored_prices = pickle.load( open('stored_prices.p', 'rb'))
    prices_time = pickle.load( open('prices_time.p', 'rb'))
    time_only = [datetime.strptime(hour, '%A:%H:%M') for hour in prices_time]

    fig, ax = plt.subplots()

    plt.title("CATGE Price over last 3 days")
    plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)

    plt.plot(time_only, stored_prices)
    plt.grid()
    plt.subplots_adjust(left=0.03, right=0.86)
    fig.autofmt_xdate()
    date_form = mdates.DateFormatter("%H:%M")
    ax.xaxis.set_major_formatter(date_form)
    loc = plticker.MultipleLocator(base=4) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(plticker.AutoLocator())
    plt.show() #Preview of chart
    plt.savefig('chart.png')

    # Blend two images
    image1 = Image.open('chart.png')
    image2 = Image.open('Catge.png')

    # Image.blend(image1, image2, alpha=.3).save('chart_logo.png')

schedule.every(5).minutes.do(create_chart)

stored_prices = pickle.load( open('stored_prices.p', 'rb'))
prices_time = pickle.load( open('prices_time.p', 'rb'))


print(stored_prices, prices_time)
create_chart()
# while True:
#     schedule.run_pending()
#     time.sleep(1)