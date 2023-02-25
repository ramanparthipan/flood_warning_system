def test_stations_level_over_threshold():
    """tests requirements of stations level over threshold"""
    # creates a list of stations
    stations = []
    for level in [1, None, 2, 3, 'b', 5, 6, 7]:
        x = MonitoringStation(None, None, None, None, (1, 3), None, None)
        x.latest_level = level
        stations.append(x)
    stations[-1].typical_range = (3, 1)
    over_threshold = stations_level_over_threshold(stations, 1)
    # checks for the expected length of the list returned
    assert len(over_threshold) == 2
    # checks the ordering of list
    assert over_threshold[0][1] == 2.5
    assert over_threshold[1][1] == 2

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    length = len(stations_highest_rel_level(stations,15))
    assert length==15
    #assert correct length of returned list