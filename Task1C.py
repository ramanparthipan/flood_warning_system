from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""
    stations = build_station_list()
    stations_within_radius_list = stations_within_radius(stations, (52.2053, 0.1218), 10)
    station_names = []
    for station in stations_within_radius_list:
        station_names.append(station.name)
    return sorted(station_names)

if __name__ == "__main__":
    print(run())