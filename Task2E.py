from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels

def run():
    """Requirements for Task 2E"""
    stations = build_station_list()
    update_water_levels(stations)
    for s in stations_highest_rel_level(stations, 5):
        print(s.name, s.relative_water_level()) # stations at which current relative water level is greatest.
        dt = 10
        dates, levels = fetch_measure_levels(s.measure_id,
                                     dt=timedelta(days=dt))
        plot_water_levels(s, dates, levels)


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
# TODO: Once Task2C is completed, implement
# a program file Task2E.py that plots the water levels over the past 10 days 
# for the 5 stations at which the current relative water level is greatest.


# testing water levels for random stations
#if __name__ == "__main__":
#    stations = build_station_list()
#    station = stations[21]

#    dt = 2
#    dates, levels = fetch_measure_levels(station.measure_id,
#                                     dt=timedelta(days=dt))

#    plot_water_levels(station, dates, levels)

 