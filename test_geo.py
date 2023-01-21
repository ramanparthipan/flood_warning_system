from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def test_stations_by_distance():
    stations = build_station_list()
    x = stations_by_distance(stations[:3], (52.2053, 0.1218))
    print(x)

