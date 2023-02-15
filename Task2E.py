from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 2E"""
    pass 
# TODO: Once Task2C is completed, implement
# a program file Task2E.py that plots the water levels over the past 10 days 
# for the 5 stations at which the current relative water level is greatest.



if __name__ == "__main__":
    stations = build_station_list()
    station = stations[10]

    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=timedelta(days=dt))

    plot_water_levels(station, dates, levels)

 