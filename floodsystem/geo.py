# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
#from haversine import haversine, Unit


"""def stations_by_distance(stations, p):
    Given a list of stations and a coordinate p, returns a list of tuples containing the station object
    and its distance to p, sorted in increasing order of distance. 
    distances = []
    for station in stations:
        distances.append((station, haversine(p, station.coord))) #distance in km
    return sorted_by_key(distances, 1)

def stations_within_radius(stations, centre, r):
    Returns the list of stations within a distance r from a point.
    distances = stations_by_distance(stations, centre)
    stations_within_radius_list = []
    for item in distances:
        if item[1] > r:
            break
        stations_within_radius_list.append(item[0])
    return stations_within_radius_list"""

def rivers_with_station(stations):
    """Returns a set of the names of the rivers from each station object"""
    river_names = set()
    for station in stations:
        river_names.add(station.river)
    return river_names

def stations_by_river(stations):
    """Returns a dictionary of the stations by each river"""
    stations_by_river_dict = {}
    for station in stations:
        if station.river in stations_by_river_dict: #if river is already a key
            stations_by_river_dict[station.river].append(station)
        else:
            stations_by_river_dict[station.river] = [station]
    return stations_by_river_dict

def rivers_by_station_number(stations, N):
    rivers_list = stations_by_river(stations)
    "Tuple of rivers and station numbers"
    river_station_number_list =[]
    for rivers in rivers_list:
        len(rivers)
        X = (rivers,len(rivers))
        river_station_number_list.append(X)
        """Sorting by the number of stations"""
    Ordered = sorted_by_key(river_station_number_list, 1, reverse=True)
    "Take the first N terms"
    End_list = Ordered[:N]

    for p in Ordered[N:]:

        if p[1] == End_list[N-1][1]:
            "Checking for rivers with same number of stations as the last river added"

            End_list.append(p)

    return End_list






