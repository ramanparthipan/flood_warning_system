from floodsystem.stationdata import build_station_list
from floodsystem.geo import *


def test_stations_by_distance():
    stations = build_station_list()
    x = stations_by_distance(stations[:3], (52.2053, 0.1218))
    print(x)

def test_stations_within_radius():
    stations = build_station_list()
    x = stations_within_radius(stations, (52.2053, 0.1218), 7)
    print(x)
    print(len(x))

def test_rivers_with_station():
    stations = build_station_list()
    x = rivers_with_station(stations)
    print(x)

def test_stations_by_river():
    stations = build_station_list()
    x = stations_by_river(stations[:3])
    print(x)

if __name__ == "__main__":
    test_stations_by_river()
