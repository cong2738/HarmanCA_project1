import requests
import json
from datetime import datetime
from tmap.getLoc.geocoder import Geocoder   # 🚨 Geocoder 클래스 불러오기
import os

class TMapRouteFinder:
    """
    TMap API를 사용하여 자동차 경로를 찾는 클래스 (Geocoder 사용)
    """

    def __init__(self, start_address:str, end_address:str, search_option:str):
        """
        생성자: API Key 설정
        :param api_key: TMap API Key
        """
        try: #실시간을 위해서는 나중에 지워야할 trycatch - 토큰 아끼려고 만든 구문
            with open("./_data/tmap_car_route.json", "r", encoding="utf-8") as file:
                self.routeJson = json.load(file)
                pass
        except:
            print("tmap_car_route.json가 없습니다.")
            self.routeJson = self.set_route(start_address, end_address, search_option)
        
        self.cooked_data = self.cook_data(self.routeJson, end_address, start_address)

    def get_cooked_data(self):
        """처리된 데이터를 밖으로 가져가는 매소드"""
        return self.cooked_data

    def set_route(self, start_address: str, end_address: str, address_type: str = "ROAD", search_option: int = 0):
        """
        자동차 경로 요청 매소드 - API로 TMAP에 경로를 요청 경로 데이터를 JSON으로 저장.
        :param start_address: 출발지 주소
        :param end_address: 도착지 주소
        :param address_type: 주소 변환 타입 (기본: "ROAD" - 도로명 주소)
        :param search_option: 경로 탐색 옵션 (0: 최적, 1: 최단, 2: 최소 요금)
        :return: 경로 정보를 JSON으로 반환
        """
        self.api_key = os.getenv("HEONMIN_TMAP_KEY")
        self.url_route = "https://apis.openapi.sk.com/tmap/routes?version=1"
        self.headers = {
            "accept": "application/json",
            "appKey": self.api_key,
            "content-type": "application/json"
        }
        
        # 🚀 Geocoder 사용하여 주소 → 좌표 변환
        start_coords = Geocoder(start_address, address_type).location()
        end_coords = Geocoder(end_address, address_type).location()
        
        if not start_coords or not end_coords:
            print("⚠️ 좌표 변환 실패로 인해 경로 탐색을 종료합니다.")
            return {}

        start_x, start_y = start_coords
        end_x, end_y = end_coords
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")

        payload = {
            "tollgateFareOption": 16,
            "roadType": 32,
            "directionOption": 1,
            "endX": end_x,
            "endY": end_y,
            "endRpFlag": "G",
            "reqCoordType": "WGS84GEO",
            "startX": start_x,
            "startY": start_y,
            "gpsTime": f"{current_time}",
            "speed": 0,
            "uncetaintyP": 1,
            "uncetaintyA": 1,
            "uncetaintyAP": 1,
            "carType": 1,
            "detailPosFlag": "1",
            "resCoordType": "WGS84GEO",
            "sort": "index",
            "trafficInfo": "Y",
            "mainRoadInfo": "Y",
            "searchOption": search_option
        }

        # API 요청
        response = requests.post(self.url_route, json=payload, headers=self.headers)

        # 응답 확인 및 데이터 추출
        if response.status_code != 200:
            print(f"⚠️ API 요청 실패: {response.status_code}, {response.text}")
            return {}

        data = response.json()

        # 🚀 JSON 데이터를 파일로 저장
        try:            
            with open("./_data/tmap_car_route.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except:
            print("json 파일 저장 실패.")
            return {}

        print("json 파일 저장 완료")

        return data

    def cook_data(self, data,start_address, end_address):
        """
        API에서 받은 데이터를 상황에 맞게 조리하는 매소드
        """
        # 🚀 전체 경로 정보 추출 (총 거리, 시간, 요금 정보)
        summary = data.get("features", [])[0].get("properties", {})
        total_distance = summary.get("totalDistance", "정보 없음")
        total_time = summary.get("totalTime", "정보 없음")
        total_fare = summary.get("totalFare", "정보 없음")
        taxi_fare = summary.get("taxiFare", "정보 없음")

        # 🚀 경로 세부 정보 추출
        route_list = []
        for feature in data.get("features", []):
            properties = feature.get("properties", {})
            if "description" in properties:
                route_list.append({
                    "구간 설명": properties.get("description", "정보 없음"),
                    "교통상황": properties.get("congestion", "정보 없음"),
                    "거리(m)": properties.get("distance", "정보 없음"),
                    "소요 시간(초)": properties.get("time", "정보 없음"),
                    "도로명": properties.get("roadName", "정보 없음")
                })

        # 🚀 결과 JSON 생성
        cooked_data = {
            "출발지": start_address,
            "도착지": end_address,
            "총 이동 거리(km)": round(total_distance / 1000, 2),
            "총 소요 시간": f"{total_time // 60}분 {total_time % 60}초",
            "총 요금 정보(원)": f"{total_fare:,}",
            "택시 예상 요금(원)": f"{taxi_fare:,}",
            "경로 상세 정보": route_list
        }

        # 🚀 JSON 데이터 출력
        # print("\n📌 🚗 TMap 자동차 경로 안내 데이터\n")
        # print(json.dumps(cooked_data, indent=4, ensure_ascii=False))

        return cooked_data

# class Trip:
#     def __init__(self, num_of_routes, start_address, end_address, address_type):
#         self.num_of_routes = num_of_routes
#         self.start_address = start_address
#         self.end_address = end_address
#         self.address_type = address_type

#     def __str__(self):
#         return f"🚗 여행 경로: {self.start_address} → {self.end_address} ({self.address_type})"

class Car_weight:
    def __init__(self, cooked_route_data, weather_dic:dict):
        self.T1H, self.RN1, self.REH, self.PTY, self.WSD = weather_dic.values() #"T1H":"기온", "RN1":"강수량", "REH":"습도", "PTY":"강수형태", "WSD":"풍속"
        self.cooked_route_data = cooked_route_data
        self.car_weight = self.set_carweight(self.routeJson,self.cooked_data) 

    def set_carweight(self,cooked_data):
        """
        차에 대한 가중치 계산해서 설정하는 매소드(Needs modification)
        """
         # 🚗 **기본 가중치 요소**
        distance_time = cooked_data["총 소요 시간"]
        fare_str = cooked_data["총 요금 정보(원)"].replace(",", "")

        try:
            total_fare = int(fare_str)
        except ValueError:
            total_fare = 0  # 값이 없을 경우 0 처리

        # **1️⃣ 기본 가중치 계산**
        distance_weight = 1 / (distance_time * 3)  # 🚗 주행 시간 가중치
        fare_weight = (total_fare / total_fare + 100)  # 💰 요금 가중치

        # **2️⃣ 날씨 반영 가중치** (기본값 1)
        weather_factor = 1.0  

        # rain_factor = 1 / (self.RN1 + 100)  # ☔ 비/눈 가중치
        snow_factor = 1
        if not self.PTY in [0, 1]:
            snow_factor = 0.5
        temp_factor = abs(self.T1H) * 2 # 🌡️ 기온 가중치

        # **최종 가중치 계산**
        factors = [distance_weight, fare_weight, snow_factor, temp_factor]
        weight = sum(factors)/len(factors)

        return weight

    def get_carweight(self):
        """
        차 가중치 class에서 외부로 가져가는 매소드
        """
        return self.car_weight


if __name__ == "__main__":
    tmap_toutefinder = TMapRouteFinder("서울 양천구 목동로 201","서울 강서구 화곡로 179 ", "ROAD")
    print(tmap_toutefinder.get_cooked_data())