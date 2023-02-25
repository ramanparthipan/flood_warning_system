from floodsystem.plot import plot_water_level_with_fit
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels


def run():
    """Requirements for Task 2F"""    
    stations = build_station_list()
    update_water_levels(stations)
    for s in stations_highest_rel_level(stations, 5):
        print(s.name, s.relative_water_level()) # stations at which current relative water level is greatest.
        dt = 2
        dates, levels = fetch_measure_levels(s.measure_id,
                                     dt=timedelta(days=dt))
        p = 4
        plot_water_level_with_fit(s, dates, levels, p)
# TODO: Once Task2C is completed, implement Task2F as in the instructions



if __name__ == "__main__":
    run()
