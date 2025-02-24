import requests
import pandas as pd
from tmap.getLoc.Geocoder import Geocoder  # 🚨 Geocoder 클래스 사용

class BikeStationFinder:
    """
    서울 따릉이 API를 사용하여 대여소 정보를 검색하는 클래스
    """

    def __init__(self, api_key: str):
        """
        생성자: API Key 설정
        :param api_key: 서울 공공데이터포털에서 발급받은 따릉이 API Key
        """
        self.api_key = api_key
        self.url_bike = f"http://openapi.seoul.go.kr:8088/{self.api_key}/json/bikeList"
    
    def get_bike_stations(self, start_address: str, address_type: str = "ROAD", keyword: str = None):
        """
        따릉이 대여소 정보를 검색하는 메서드
        :param start_address: 사용자의 현재 위치 (주소)
        :param address_type: 주소 변환 방식 ("ROAD" - 도로명, "PARCEL" - 지번)
        :param keyword: 특정 키워드 포함하는 대여소만 필터링 (예: "화곡역")
        :return: 검색된 따릉이 대여소 목록 (Pandas DataFrame 또는 JSON)
        """
        # 🚀 Geocoder 사용하여 주소 → 좌표 변환
        location = Geocoder(start_address, address_type).location()
        if not location:
            print("⚠️ 주소 변환 실패로 인해 검색을 종료합니다.")
            return None

        # 1️⃣ API 호출 (최대 1000개 데이터 요청)
        response = requests.get(f"{self.url_bike}/1/1000/")
        if response.status_code != 200:
            print(f"⚠️ API 요청 실패: {response.status_code}")
            return None

        data = response.json()
        rows = data.get('rentBikeStatus', {}).get('row')

        if not rows:
            print("📌 따릉이 대여소 데이터가 없습니다.")
            return None

        # 2️⃣ DataFrame으로 변환
        df = pd.DataFrame(rows)

        # 3️⃣ 특정 키워드가 포함된 대여소만 필터링 (예: "화곡역")
        if keyword:
            df = df[df["stationName"].str.contains(keyword, na=False)]

        # 4️⃣ 필요한 정보만 추출 (대여소명, 거치대 총 개수, 사용 가능 자전거 수, 대여율)
        selected_columns = ["stationName", "rackTotCnt", "parkingBikeTotCnt", "shared"]
        df = df[selected_columns]

        # 🚀 검색된 데이터 반환
        return df.to_dict(orient="records")  # JSON 형태로 반환 가능
