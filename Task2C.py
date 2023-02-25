from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    for s in stations_highest_rel_level(stations, 15):
        print(s.name, s.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()