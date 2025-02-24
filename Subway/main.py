from Subway_congestion import SubwayCongestion, load_station_data

filepath = r"C:\Users\kccistc\Desktop\project\HarmanCA_project1\Subway\EXDATA.TXT"

stations, condict = load_station_data(filepath)

subway_congestion = SubwayCongestion(stations, condict)

result = subway_congestion.get_congestion_result()

print(result)

