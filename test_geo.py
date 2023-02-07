from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station


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

def rivers_by_station_number():
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (6.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River X"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Y"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Y"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    river = "River Z"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    stations = [s, s1,s2,s3,s4]
    N = 2
    output_list = geo.rivers_by_station_number(stations, N)

    assert len(output_list) == 3

    for i in range(1, len(output_list)):
        assert output_list[i][1] >= output_list[i-1][1]

