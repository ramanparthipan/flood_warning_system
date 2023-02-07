# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    """Test consistency check"""
    station1 = MonitoringStation(station_id = 'stn_id_1',
                                measure_id = 'measure_id_1',
                                label = 'Test 1',
                                coord = (0.0, 1.0),
                                typical_range = (0.0, 1.0),
                                river = 'river1',
                                town = 'town1')
    station2 = MonitoringStation(station_id = 'stn_id_2',
                                measure_id = 'measure_id_2',
                                label = 'Test 2',
                                coord = (1.0, 1.0),
                                typical_range = (5.0, 1.0),
                                river = 'river2',
                                town = 'town2')
    station3 = MonitoringStation(station_id = 'stn_id_3',
                                measure_id = 'measure_id_3',
                                label = 'Test 3',
                                coord = (100.0, 100.0),
                                typical_range = (None),
                                river = 'river3',
                                town = 'town3')
    

    stations = [station1, station2, station3]
    output = MonitoringStation.inconsistent_typical_range_stations(stations)
    answer=[]
    for station in output:
        answer.append(station.name)

    return(answer)

v = test_inconsistent_typical_range_stations()

assert type(v) == list
assert v == ['Test 2', 'Test 3']

