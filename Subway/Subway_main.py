from subway_congestion import SubwayCongestion

def get_user_selection(options, prompt):
    """ 사용자가 입력한 값을 검증 후 반환하는 함수 """
    print(f"\n📌 사용 가능한 목록: {options}")
    
    while True:
        user_input = input(f"\n{prompt}: ")
        selected_items = [item.strip() for item in user_input.split(',') if item.strip() in options]
        if selected_items:
            return selected_items
        print("❌ 입력한 값이 유효하지 않습니다. 다시 입력하세요.")

# 🚨 CSV 파일 경로 설정
file_path = r"C:\Users\park ji ho\Desktop\subway_혼잡도_정규화.csv"

# SubwayCongestion 객체 생성
subway = SubwayCongestion(file_path)

# ✅ 사용자로부터 역 & 시간대 입력받기
selected_stations = get_user_selection(subway.stations[0], "🚇 혼잡도를 확인할 역을 입력하세요 (쉼표로 구분, 예: 서울역,강남,잠실)")
selected_times = get_user_selection(subway.df.columns[5:].tolist(), "⏰ 혼잡도를 확인할 시간대를 입력하세요 (쉼표로 구분, 예: 07시00분,08시00분)")

# 📊 평균 혼잡도 출력 & 그래프 시각화
for time in selected_times:
    avg_congestion = subway.calculate_avg_congestion(selected_stations, time)
    print(f"✅ 선택한 {len(selected_stations)}개 역의 {time} 기준 예상 평균 혼잡도: {avg_congestion:.2f}")

subway.plot_congestion_change(selected_stations, selected_times)
