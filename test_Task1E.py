from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
def test_rivers_with_station():
    stations = build_station_list()
    x = rivers_with_station(stations)
    print(x)

def test_stations_by_river():
    stations = build_station_list()
    x = stations_by_river(stations[:3])
    print(x)
test_stations_by_river()
test_rivers_with_station()