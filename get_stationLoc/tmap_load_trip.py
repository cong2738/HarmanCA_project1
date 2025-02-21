import requests
import json
import os
from get_stationXY import Get_starionXY

def get_route (start_station, end_station):
    # API_KEY
    API_KEY = os.getenv("TMAP_PT_KEY")
    TEST_KEY = os.getenv("TMAP_TEST_KEY")

    # API URL
    URL = "https://apis.openapi.sk.com/transit/routes"
    start_stationXY = Get_starionXY(start_station)
    end_stationXY = Get_starionXY(end_station)

    print(start_stationXY.get_stationLoc())
    print(end_stationXY.get_stationLoc())

    if start_stationXY.get_stationLoc() and end_stationXY.get_stationLoc():
        sx,sy = start_stationXY.get_stationLoc()
        ex,ey = end_stationXY.get_stationLoc()

        # 요청 헤더
        headers = {
            "accept": "application/json",
            "appKey": TEST_KEY,  # 실제 API 키 사용
            "content-type": "application/json"
        }

        # 요청 데이터 (JSON)
        data = {
            "startX": sx,
            "startY": sy,
            "endX": ex,
            "endY": ey,
            "lang": 0,
            "format": "json",
            "count": 10,
        }   

        # POST 요청 보내기
        response = requests.post(URL, json=data, headers=headers)

        # 응답 저장
        if response.status_code == 200:
            response_data = response.json()
            
            # JSON 데이터를 파일로 저장
            with open("tmap_subway.json", "w", encoding="utf-8") as f:
                json.dump(response_data, f, ensure_ascii=False, indent=4)
            
            print("✅ tmap_subway.json 파일 저장 완료!")
        else:
            print(f"❌ API 호출 실패: {response.status_code}, {response.text}")

if __name__ == "__main__":
    print(get_route("개화","목동"))