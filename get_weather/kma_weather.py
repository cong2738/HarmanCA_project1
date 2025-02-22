"""
writer: 박호윤
기상청 단기예보API에서 원하는 기상정보 추출 dict형태 사용

"""

import requests
import make_districtPosion_dic
import os
import datetime

class KMA_Weather:
    def __init__(self):
        self.kma_weather = self.make_weather_dict()

    def timenow(self):
        KST = datetime.timezone(datetime.timedelta(hours=9))
        current_time_kst = datetime.datetime.now(KST)
        return current_time_kst.strftime('%Y%m%d')
    
    def set_data(self):
        KEY = os.getenv("DATAGOKR_API_KEY")
        district = "종로구"
        todayString = self.timenow()
        currentTime = '1000'
        x,y = make_districtPosion_dic.get_districtPosion_dic()[district]
        URL = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={KEY}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={todayString}&base_time={currentTime}&nx={x}&ny={y}"
        response = requests.get(URL)
        data = response.json()
        return data

    def make_weather_dict(self):
        res = dict()
        data = self.set_data()

        #"T1H":"기온", "RN1":"강수량", "REH":"습도", "PTY":"강수형태", "WSD":"풍속"
        target_category = ["T1H", "RN1", "REH", "PTY", "WSD"]

        # print(data["response"]["body"]["items"]["item"])
        for weather_dict in data["response"]["body"]["items"]["item"]:
            if not weather_dict["category"] in target_category: continue
            res[weather_dict["category"]] = weather_dict["obsrValue"]

        return res
    
    def get_weatherDict(self):
        return self.kma_weather
    
if __name__ == "__main__":
    weather = KMA_Weather()
    weather.get_weatherDict()