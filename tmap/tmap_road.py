# import requests
# import json
# from datetime import datetime

# # 1️⃣ API 요청을 위한 설정
# url = "https://apis.openapi.sk.com/tmap/routes?version=1&callback=function"
# current_time = datetime.now()
# formatted_time = current_time.strftime("%Y%m%d%H%M%S")

# payload = {
#     "tollgateFareOption": 16,
#     "roadType": 32,
#     "directionOption": 1,
#     "endX": 126.864931,
#     "endY": 37.526065,
#     "endRpFlag": "G",
#     "reqCoordType": "WGS84GEO",
#     "startX": 126.798153,
#     "startY": 37.578608,
#     "gpsTime": f"{formatted_time}",
#     "speed": 0,
#     "uncetaintyP": 1,
#     "uncetaintyA": 1,
#     "uncetaintyAP": 1,
#     "carType": 1,
#     "startName": "%EC%9D%84%EC%A7%80%EB%A1%9C%20%EC%9E%85%EA%B5%AC%EC%97%AD",
#     "endName": "%ED%97%A4%EC%9D%B4%EB%A6%AC",
#     "gpsInfoList": "126.939376564495,37.470947057194365,120430,20,50,5,2,12,1_126.939376564495,37.470947057194365,120430,20,50,5,2,12,1",
#     "detailPosFlag": "1",
#     "resCoordType": "WGS84GEO",
#     "sort": "index",
#     "trafficInfo": "Y",
#     "mainRoadInfo": "Y",
#     "searchOption": 0,
#     "totalValue": 1
# }

# headers = {
#     "accept": "application/json",
#     "appKey": "KEY",
#     "content-type": "application/json"
# }

# # 2️⃣ API 호출
# response = requests.post(url, json=payload, headers=headers)

# # 3️⃣ 응답 데이터 확인 및 `coordinates` 제거 후 저장
# if response.status_code == 200:
#     data = response.json()  # JSON 변환

#     # 🔹 coordinates 정보 제거
#     if "features" in data:
#         for feature in data["features"]:
#             if "geometry" in feature and "coordinates" in feature["geometry"]:
#                 del feature["geometry"]["coordinates"]

#     # 🔹 JSON 데이터를 파일로 저장 (coordinates 제거된 데이터)
#     with open("car_route_data.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)

#     # 🔹 JSON 데이터 출력 (보기 좋게 출력)
#     print("\n📌 자동차 경로 안내 데이터 (JSON 저장 완료, coordinates 제외)\n")
#     print(json.dumps(data, indent=4, ensure_ascii=False))

# else:
#     print(f"⚠️ API 요청 실패: {response.status_code}, {response.text}")

# ---------------------------------------------------------------------

import requests
import json
from datetime import datetime

# 1️⃣ API 요청을 위한 설정
url = "https://apis.openapi.sk.com/tmap/routes?version=1"
current_time = datetime.now().strftime("%Y%m%d%H%M%S")

payload = {
    "tollgateFareOption": 16,
    "roadType": 32,
    "directionOption": 1,
    "endX": 126.864931,
    "endY": 37.526065,
    "endRpFlag": "G",
    "reqCoordType": "WGS84GEO",
    "startX": 126.798153,
    "startY": 37.578608,
    "gpsTime": f"{current_time}",
    "speed": 0,
    "uncetaintyP": 1,
    "uncetaintyA": 1,
    "uncetaintyAP": 1,
    "carType": 1,
    # "startName": "을지로 입구역",
    # "endName": "헤이리",
    "detailPosFlag": "1",
    "resCoordType": "WGS84GEO",
    "sort": "index",
    "trafficInfo": "Y",
    "mainRoadInfo": "Y",
    "searchOption": 0,
    "totalValue": 1
}

headers = {
    "accept": "application/json",
    "appKey": "KEY",
    "content-type": "application/json"
}

# 2️⃣ API 호출
response = requests.post(url, json=payload, headers=headers)

# 3️⃣ 응답 데이터 확인 및 추출
if response.status_code == 200:
    data = response.json()  # JSON 변환

    # 🚀 전체 경로 정보 추출 (총 거리, 시간, 요금 정보)
    summary = data.get("features", [])[0].get("properties", {})
    total_distance = summary.get("totalDistance", "정보 없음")  # 총 이동 거리 (m)
    total_time = summary.get("totalTime", "정보 없음")  # 총 소요 시간 (초)
    total_fare = summary.get("totalFare", "정보 없음")  # 총 요금 정보 (원)
    taxi_fare = summary.get("taxiFare", "정보 없음")  # 택시 요금 정보 (원)

    # 🚀 경로 세부 정보 추출 (설명 + 교통상황)
    route_list = []
    for feature in data.get("features", []):
        properties = feature.get("properties", {})
        if "description" in properties:  # 경로 설명이 있는 데이터만 필터링
            route_list.append({
                "구간 설명": properties.get("description", "정보 없음"),
                "교통상황": properties.get("congestion", "정보 없음"),  # "원활", "정체" 등
                "거리(m)": properties.get("distance", "정보 없음"),
                "소요 시간(초)": properties.get("time", "정보 없음"),
                "도로명": properties.get("roadName", "정보 없음")
            })

    # 🚀 결과 JSON 생성
    result_json = {
        "총 이동 거리(km)": round(total_distance / 1000, 2),
        "총 소요 시간": f"{total_time // 60}분 {total_time % 60}초",
        "총 요금 정보(원)": f"{total_fare:,}",
        "택시 예상 요금(원)": f"{taxi_fare:,}",
        "경로 상세 정보": route_list
    }

    # 🚀 JSON 데이터를 파일로 저장
    with open("car_route_data.json", "w", encoding="utf-8") as f:
        json.dump(result_json, f, indent=4, ensure_ascii=False)

    # 🚀 JSON 데이터 출력 (보기 좋게 출력)
    print("\n📌 🚗 TMap 자동차 경로 안내 데이터 (JSON 저장 완료)\n")
    print(json.dumps(result_json, indent=4, ensure_ascii=False))

else:
    print(f"⚠️ API 요청 실패: {response.status_code}, {response.text}")


