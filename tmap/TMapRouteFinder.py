import requests
import json
from datetime import datetime
from typing import Any
from tmap.getLoc.Geocoder import Geocoder  # 🚨 Geocoder 클래스 불러오기

class TMapRouteFinder:
    """
    TMap API를 사용하여 자동차 경로를 찾는 클래스 (Geocoder 사용)
    """

    def __init__(self, api_key: str):
        """
        생성자: API Key 설정
        :param api_key: TMap API Key
        """
        self.api_key = api_key
        self.url_route = "https://apis.openapi.sk.com/tmap/routes?version=1"
        self.headers = {
            "accept": "application/json",
            "appKey": self.api_key,
            "content-type": "application/json"
        }

    def get_route(self, start_address: str, end_address: str, address_type: str = "ROAD", search_option: int = 0):
        """
        자동차 경로 탐색 메서드
        :param start_address: 출발지 주소
        :param end_address: 도착지 주소
        :param address_type: 주소 변환 타입 (기본: "ROAD" - 도로명 주소)
        :param search_option: 경로 탐색 옵션 (0: 최적, 1: 최단, 2: 최소 요금)
        :return: 경로 정보를 JSON으로 반환
        """
        # 🚀 Geocoder 사용하여 주소 → 좌표 변환
        start_coords = Geocoder(start_address, address_type).location()
        end_coords = Geocoder(end_address, address_type).location()
        
        if not start_coords or not end_coords:
            print("⚠️ 좌표 변환 실패로 인해 경로 탐색을 종료합니다.")
            return None

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
        if response.status_code == 200:
            data = response.json()

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
            result_json = {
                "출발지": start_address,
                "도착지": end_address,
                "총 이동 거리(km)": round(total_distance / 1000, 2),
                "총 소요 시간": f"{total_time // 60}분 {total_time % 60}초",
                "총 요금 정보(원)": f"{total_fare:,}",
                "택시 예상 요금(원)": f"{taxi_fare:,}",
                "경로 상세 정보": route_list
            }

            # 🚀 JSON 데이터를 파일로 저장
            with open("car_route_data.json", "w", encoding="utf-8") as f:
                json.dump(result_json, f, indent=4, ensure_ascii=False)

            # 🚀 JSON 데이터 출력
            print("\n📌 🚗 TMap 자동차 경로 안내 데이터 (JSON 저장 완료)\n")
            print(json.dumps(result_json, indent=4, ensure_ascii=False))

            return result_json

        else:
            print(f"⚠️ API 요청 실패: {response.status_code}, {response.text}")
            return None


class Trip:
    def __init__(self, num_of_routes: Any, start_address: Any, end_address: Any, address_type: Any):
        self.num_of_routes = num_of_routes
        self.start_address = start_address
        self.end_address = end_address
        self.address_type = address_type

    def __str__(self):
        return f"🚗 여행 경로: {self.start_address} → {self.end_address} ({self.address_type})"
