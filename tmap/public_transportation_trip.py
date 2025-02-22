"""
티맵 대중교통API 활용 여행 경로 요청
    -input:
        start_adress: 출발위치 주소
        end_adress: 도착위치 주소
        adressType: 주소형식('ROAD':도로명 주소 'PARCEL':지번 주소)
"""

import requests
import json
import os
import getLoc.Geocoder as Geocoder
#from get_location.legacy.get_stationXY import Get_starionXY

def get_route (start_adress, end_adress, adressType):
    # API_KEY
    API_KEY = os.getenv("TMAP_PT_KEY")
    TEST_KEY = os.getenv("TMAP_TEST_KEY")

    # API URL
    URL = "https://apis.openapi.sk.com/transit/routes"
    start_stationXY = Geocoder.XY_at(start_adress, adressType)
    end_stationXY = Geocoder.XY_at(end_adress, adressType)

    print(start_stationXY.get_stationLoc())
    print(end_stationXY.get_stationLoc())

    # 두위치중 하나라도 None이라면 에러
    if not (start_stationXY.get_stationLoc() and end_stationXY.get_stationLoc()): 
        return None
    
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
    
    # 비정상 응답시 에러
    if response.status_code != 200: 
        print(f"❌ API 호출 실패: {response.status_code}, {response.text}")
        return None

    # 응답 저장
    response_data = response.json()
    
    # JSON 데이터를 파일로 저장
    with open("./data/tmap_trip.json", "w", encoding="utf-8") as f:
        json.dump(response_data, f, ensure_ascii=False, indent=4)
    
    print("✅ tmap_trip.json 파일 저장 완료!")
    

if __name__ == "__main__":
    print(get_route("개화동 664","목동 926-3", "ROAD"))