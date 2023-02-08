from floodsystem.stationdata import build_station_list
from floodsystem.geo import *
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station


# Note, if tests fail, it could be because the real time data has changed so the values that are being compared
# aren't valid anymore

def test_stations_by_distance():
    stations = build_station_list()
    x = stations_by_distance(stations, (52.2053, 0.1218))
    #print(x)
    #print(x[0][0].name)
    assert x[0][0].name == "Cambridge Jesus Lock"
    

def test_stations_within_radius():
    #stations = build_station_list()
    #x = stations_within_radius(stations, (52.2053, 0.1218), 7)
    #print(x)

    stations = build_station_list()
    stations_within_radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    station_names = []
    for station in stations_within_radius_list:
        station_names.append(station.name)
    sorted_station_names = sorted(station_names)
    print(sorted_station_names)
    assert sorted_station_names[0] == 'Bin Brook'
    

def test_rivers_with_station():
    stations = build_station_list()
    rivers_with_station_set = rivers_with_station(stations)
    assert sorted(list(rivers_with_station_set))[0] == "Addlestone Bourne"

def test_stations_by_river():
    stations = build_station_list()
    stations_by_river_dict = stations_by_river(stations)
    river_aire_station_names = []
    for station in stations_by_river_dict['River Aire']:
        river_aire_station_names.append(station.name)
    #print(sorted(river_aire_station_names))
    assert sorted(river_aire_station_names)[0] == "Airmyn"


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

if __name__ == "__main__":
    test_stations_by_river()
    