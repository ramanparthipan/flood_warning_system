import numpy as np
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
import matplotlib
import matplotlib.pyplot as plt
from floodsystem.analysis import *

def test_polyfit():
    stations = build_station_list()
    station = stations[10]

    dt = 1
    dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=timedelta(days=dt))

    datesfloat = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(datesfloat, levels, 4)
    datesshifted = datesfloat - d0
    print(datesshifted)
    print(d0)

        # Plot original data points
    plt.plot(datesshifted, levels, '.')
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.tight_layout() 


    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(datesshifted[0], datesshifted[-1], 30)
    plt.plot(x1, poly(x1))

    # Display plot
    #plt.show()

    assert isinstance(poly, np.poly1d)



if __name__ == "__main__":
    test_polyfit()