import requests
import json
import xml.etree.ElementTree as ET  # XML 파싱 모듈

class BusArrivalFinder:
    """
    서울시 버스 도착 정보를 조회하는 클래스
    """

    def __init__(self, api_key: str):
        """
        생성자: API Key 설정
        :param api_key: 서울시 공공데이터포털에서 발급받은 API Key
        """
        self.api_key = api_key
        self.url = "http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll"

    def normalize_congestion(self, reride_num: str, route_type: str) -> str:
        """
        잔여좌석 수 또는 혼잡도 값을 정규화하여 혼잡도로 변환
        :param reride_num: 잔여좌석 수 또는 혼잡도 (API에서 제공하는 값)
        :param route_type: 노선 유형 (6: 광역버스)
        :return: 혼잡도 (0: 데이터없음, 3: 여유, 4: 보통, 5: 혼잡)
        """
        if reride_num == "정보 없음":
            return "0"  # 데이터 없음
        
        reride_num = int(reride_num)

        if route_type == "6":  # 광역버스(빨간 버스)
            if reride_num > 10:
                return "3"  # 여유
            elif 5 <= reride_num <= 10:
                return "4"  # 보통
            else:
                return "5"  # 혼잡
        else:
            # 일반 혼잡도 값 그대로 사용
            return str(reride_num)

    def get_bus_arrival(self, bus_route_id: str):
        """
        특정 버스 노선의 모든 정류장 도착 정보를 조회
        :param bus_route_id: 조회할 버스 노선 ID
        :return: 버스 도착 정보 JSON 데이터
        """
        params = {
            "serviceKey": self.api_key,  # API 인증키
            "busRouteId": bus_route_id  # 버스 노선 ID
        }

        # API 호출
        response = requests.get(self.url, params=params)

        # 응답 확인 및 XML → JSON 변환
        if response.status_code == 200:
            # XML 데이터 파싱
            root = ET.fromstring(response.text)
            
            # JSON 변환을 위한 리스트 생성
            bus_arrival_list = []
            
            for item in root.findall(".//itemList"):
                
                bus_info = {
                    "노선명": item.findtext("busRouteAbrv", "정보 없음"),
                    "정류소명": item.findtext("stNm", "정보 없음"),
                    "도착예정시간1": item.findtext("arrmsg1", "정보 없음"),
                    "도착예정시간2": item.findtext("arrmsg2", "정보 없음"),
                    "잔여좌석수1": item.findtext("reride_Num1", "정보 없음"),
                    "잔여좌석수2": item.findtext("reride_Num2", "정보 없음"),
                    "재차 구분1": item.findtext("rerdie_Div1", "정보 없음"),
                }
                bus_arrival_list.append(bus_info)
            
            # JSON 데이터 저장
            json_filename = "bus_arrival.json"
            with open(json_filename, "w", encoding="utf-8") as f:
                json.dump(bus_arrival_list, f, indent=4, ensure_ascii=False)

            # JSON 데이터 출력
            print(f"\n📌 버스 도착 정보 (JSON 저장 완료: {json_filename})\n")
            print(json.dumps(bus_arrival_list, indent=4, ensure_ascii=False))

            return bus_arrival_list

        else:
            print(f"⚠️ API 요청 실패: {response.status_code}")
            return None
