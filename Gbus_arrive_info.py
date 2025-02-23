import requests
import pandas as pd
import os

# 1️⃣ API 요청 설정
API_KEY = "# 공공데이터포털 API 키"  
URL = "http://apis.data.go.kr/6410000/busarrivalservice/v2/getBusArrivalListv2"
CSV_FILE = "bus_data.csv"


params = {
    "serviceKey": API_KEY,
    "stationId": "203000125",  # 정류장 ID
    "returnType": "json",
}

# 2️⃣ API 요청
response = requests.get(URL, params=params)

# 3️⃣ 응답 데이터 확인 및 필터링
while True:
    if response.status_code == 200:
        data = response.json()  # JSON 응답을 딕셔너리로 변환
        
        if "busArrivalList" in data.get("response", {}).get("msgBody", {}):
            bus_list = data["response"]["msgBody"]["busArrivalList"]

            # 🔹 필요한 정보만 추출
            bus_info = []
            for bus in bus_list:
                def format_time(seconds):
                    """⏳ 초 단위 시간을 'm분 s초' 형식으로 변환"""
                    if not seconds or seconds == "":
                        return "정보 없음"
                    minutes, sec = divmod(int(seconds), 60)
                    return f"{minutes}분 {sec}초"

                bus_info.append({
                    "노선명": bus.get("routeName", "정보 없음"),  # 버스 노선명
                    "목적지": bus.get("routeDestName", "정보 없음"),  # 버스 종점
                    "남은 정류장 수": bus.get("staOrder", "정보 없음"),  # 현재 정류장에서 몇 정거장 남았는지
                    "첫 번째 도착 시간": format_time(bus.get("predictTimeSec1")),  # 첫 번째 버스 도착 예상 시간
                    "첫 번째 차량번호": bus.get("plateNo1", "정보 없음"),  # 첫 번째 버스 차량번호
                    "두 번째 도착 시간": format_time(bus.get("predictTimeSec2")),  # 두 번째 버스 도착 예상 시간
                    "두 번째 차량번호": bus.get("plateNo2", "정보 없음")  # 두 번째 버스 차량번호
                })

            # 🔹 Pandas DataFrame 변환
            df = pd.DataFrame(bus_info)
            if os.path.exists(CSV_FILE):
                df.to_csv(CSV_FILE, mode='a', header=False, index=False, encoding="utf-8-sig")
            else:
                df.to_csv(CSV_FILE, mode='w', header=True, index=False, encoding="utf-8-sig")

            # 🔹 DataFrame 출력 (index 제거하여 깔끔하게 출력)
            print("\n📌 경기도 버스 도착 정보\n")
            print(df.to_string(index=False))
        else:
            print("📌 버스 도착 정보가 없습니다.")

    else:
        print(f"⚠️ API 요청 실패: {response.status_code}")
