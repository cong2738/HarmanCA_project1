from congestion import subway_congestion

# 클래스 객체 생성 (CSV 파일 경로 입력)
subway = subway_congestion(r"C:\Users\kccistc\Desktop\subway_혼잡도_정규화.csv")

# 전체 역과 시간 확인 (필요 시 사용)
print(subway.get_available_stations())
print(subway.get_available_times())

# 혼잡도를 확인할 역과 시간 지정
stations = ['서울역', '강남', '잠실']
times = ['7시00분', '8시00분', '9시00분', '9시30분']

# 혼잡도 결과 출력
congestion_result = subway.get_congestion(stations, times)
print(congestion_result)

# 혼잡도 변화 그래프 출력
subway.plot_congestion(stations, times)
