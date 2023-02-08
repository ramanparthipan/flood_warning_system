from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
all_data = build_station_list()
output = []

inconsistent_stations = MonitoringStation.inconsistent_typical_range_stations(all_data)
for station in inconsistent_stations:
    output.append(station.name)

print(sorted(output))