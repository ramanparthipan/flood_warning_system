from floodsystem.plot import *
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def test_plot_water_levels():
    stations = build_station_list()
    station = stations[0]

    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=timedelta(days=dt))

    plot_water_levels(station, dates, levels)
    assert isinstance(dates[0], datetime) #checks whether dates is a datetime object
    assert type(levels) == list

def test_plot_water_level_with_fit():
    stations = build_station_list()
    station = stations[50]

    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id,
                                     dt=timedelta(days=dt))

    p = 4
    plot_water_level_with_fit(station, dates, levels, p)
    assert isinstance(dates[0], datetime) #checks whether dates is a datetime object
    assert type(levels) == list


if __name__ == "__main__":
    test_plot_water_level_with_fit()