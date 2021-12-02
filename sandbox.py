import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as plticker
from datetime import datetime

def create_chart():
    stored_prices = [0.003197, 0.003197, 0.003197, 0.003197, 0.003197]
    prices_time = ['Thursday:09:00', 'Thursday:09:05', 'Thursday:09:10', 'Thursday:09:15', 'Thursday:09:20']
    time_only = [datetime.strptime(hour, '%A:%H:%M') for hour in prices_time]

    fig, ax = plt.subplots()

    plt.tick_params(axis='y', which='both', labelleft=False, labelright=True)

    plt.plot(time_only, stored_prices)
    plt.grid()
    plt.subplots_adjust(left=0.03, right=0.86)
    loc = plticker.MultipleLocator(base=5) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    date_form = mdates.DateFormatter("%H:%M")
    ax.xaxis.set_major_formatter(date_form)
    print(stored_prices, prices_time)
    plt.show() #Preview of chart

create_chart()