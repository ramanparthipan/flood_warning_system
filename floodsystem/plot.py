import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):
    """Plots the water levels against dates for a station. Inputs are a station object, a list of datetime objects
    and a list of levels"""
    
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()
    low, high = station.typical_range
    plt.axhline(y=low)
    plt.axhline(y=high)
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water levels against dates for a station, as well as a line of best fit of polynomial order 'p'. 
    Inputs are a station object, a list of datetime objects, a list of levels and an integer p"""
    datesfloat = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(datesfloat, levels, p)
    datesshifted = datesfloat - d0


    # Plot original data points
    plt.plot(datesshifted, levels, '.')
    plt.xticks(rotation=45);
    plt.tight_layout() 


    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(datesshifted[0], datesshifted[-1], 30)
    plt.plot(x1, poly(x1))

    plt.title(station.name)
    low, high = station.typical_range
    plt.axhline(y=low)
    plt.axhline(y=high)

    # Display plot
    plt.show()
    







