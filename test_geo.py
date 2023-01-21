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

if __name__ == "__main__":
    test_stations_within_radius()
