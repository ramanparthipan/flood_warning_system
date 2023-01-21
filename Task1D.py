from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D"""
    stations = build_station_list()
    rivers_with_station_set = rivers_with_station(stations)
    print("Number of rivers with atleast one station: {}".format(len(rivers_with_station_set)))
    rivers_with_station_list = list(rivers_with_station_set)
    print(sorted(rivers_with_station_list)[:10]) #prints first 10 rivers alphabetically

    stations_by_river_dict = stations_by_river(stations)
    river_aire_station_names = []
    for station in stations_by_river_dict['River Aire']:
        river_aire_station_names.append(station.name)
    print(f'Stations on River Aire: {sorted(river_aire_station_names)}')

    river_cam_station_names = []
    for station in stations_by_river_dict['River Cam']:
        river_cam_station_names.append(station.name)
    print(f'Stations on River Cam: {sorted(river_cam_station_names)}')

    river_thames_station_names = []
    for station in stations_by_river_dict['River Thames']:
        river_thames_station_names.append(station.name)
    print(f'Stations on River Thames: {sorted(river_thames_station_names)}')



if __name__ == "__main__":
    run()