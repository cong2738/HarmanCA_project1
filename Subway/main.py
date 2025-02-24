from Subway_congestion import SubwayCongestion, load_station_data

stations = ["505번 속초고등학교", "1호선 서울", "1호선 시청"]
condict = load_station_data("EXDATA.TXT")

subway_congestion = SubwayCongestion(stations, condict)

# 원하는 역 이름 입력(딕셔너리에 저장된 이름으로)
station_name = "1호선 서울"
result = subway_congestion.get_congestion_status(station_name)

print(result)
