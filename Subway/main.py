from Subway_congestion import SubwayCongestion, load_station_data

# 전체 파일경로 (절대 경로)로 정확하게 지정
filepath = r"C:\Users\kccistc\Desktop\project\HarmanCA_project1\Subway\EXDATA.TXT"

stations, condict = load_station_data(filepath)

subway_congestion = SubwayCongestion(stations, condict)

station_name = "1호선 시청"
result = subway_congestion.get_congestion_status(station_name)
print(result)

