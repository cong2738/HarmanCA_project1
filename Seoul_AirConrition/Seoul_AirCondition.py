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
        res = dict()
        url = f"http://openAPI.seoul.go.kr:8088/{api_key}/json/RealtimeCityAir/1/100/"
        response = requests.get(url)
        data = response.json()
        key_names = ["MSRSTE_NM","O3","PM10","PM25","SO2"]
        top_line = data["RealtimeCityAir"]["row"][0]
        print(top_line)
        for key_name in key_names:
            res[key_name] = top_line[key_name] 

        return res

    def get_Air_Qualitys(self):
        return self.Seoul_Air_Quality_dict

if __name__ == "__main__":
    A = Seoul_Air_Quality()
    print(A.get_Air_Qualitys())