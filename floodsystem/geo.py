# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):
    """Given a list of stations and a coordinate p, returns a list of tuples containing the station object
    and its distance to p, sorted in increasing order of distance.""" 
    distances = []
    for station in stations:
        distances.append((station, haversine(p, station.coord))) #distance in km
    return sorted_by_key(distances, 1)

def stations_within_radius(stations, centre, r):
    """Returns the list of stations within a distance r from a point."""
    distances = stations_by_distance(stations, centre)
    stations_within_radius_list = []
    for item in distances:
        if item[1] > r:
            break
        stations_within_radius_list.append(item[0])
    return stations_within_radius_list

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

    """Take in a list of stations object and an integer N
	
	Returns a list of tuples that shows the name of top N rivers 
	with the greatest number of monitoring stations, and their respective numbers
    The tuples are arranged from the ones with the most stations to the least stations
    """

    river_dict = stations_by_river(stations)
    river_list = [] 
    for river_name, station_obj_list in river_dict.items():
        river_tuple = (river_name, len(station_obj_list))
        river_list.append(river_tuple)
    greatest_list = sorted(river_list, key = lambda x: x[1], reverse=True)
    greatest_N_list = greatest_list[:N]
    for i in range(N):
        greatest_list.pop(0)
    while True:
        if greatest_list[0][1] == greatest_N_list[-1][1]:
            greatest_N_list.append(greatest_list[0])
            greatest_list.pop(0)
        else:
            break
    return greatest_N_list
    return End_list






