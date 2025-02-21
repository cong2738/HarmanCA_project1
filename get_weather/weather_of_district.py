import requests
import make_districtPosion_dic
import os

KEY =os.getenv("API_KEY")
district = "종로구"
todayString = '20250220'
currentTime = '1000'
x,y = make_districtPosion_dic.get_districtPosion_dic()[district]
URL = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={KEY}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={todayString}&base_time={currentTime}&nx={x}&ny={y}"
response = requests.get(URL)
data = response.json()
# print(data)

#"T1H":"기온", "RN1":"강수량", "REH":"습도", "PTY":"강수형태", "WSD":"풍속"
target_category = ["T1H", "RN1", "REH", "PTY", "WSD"]
target_value = "obsrValue"

res = dict()

# print(data["response"]["body"]["items"]["item"])
for weather_dict in data["response"]["body"]["items"]["item"]:
    print(weather_dict["category"])

    if not weather_dict["category"] in target_category: continue
    print(weather_dict["obsrValue"])
    res[weather_dict["category"]] = weather_dict["obsrValue"]

print(res)