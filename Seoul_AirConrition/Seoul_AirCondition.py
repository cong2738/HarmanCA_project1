"""
    writer: 박호윤
    서울시 실시간 미세먼지 데이터 class
    Seoul_Air_Quality_dict : 서울시 실시간 미세먼지 데이터가 저장된 dict
"""

import requests
import os

class Seoul_Air_Quality:
    def __init__(self):
        self.Seoul_Air_Quality_dict = self.set_seoul_air_quality()

    def set_seoul_air_quality(self):
        api_key = os.getenv("JIHO_SEOUL_API_KEY") 
        url = f"http://openAPI.seoul.go.kr:8088/{api_key}/json/RealtimeCityAir/1/100/"
        response = requests.get(url)
        data = response.json()

        return data["RealtimeCityAir"]["row"][0] #최상위 도시만 출력

    def get_Air_Qualitys(self):
        self.Seoul_Air_Quality_dict

if __name__ == "__main__":
    A = Seoul_Air_Quality()
    print(A.get_Air_Qualitys())