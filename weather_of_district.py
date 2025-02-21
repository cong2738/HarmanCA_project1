import requests
import make_districtPosion_dic

KEY ="Tdkh73UoWaP3uvgZc%2FAn32wh9oel2JvlSQs23ZUjYdM472sbLLv46g1w5betnvsoIoxuNsPcmVrYR3I3nAWgsg%3D%3D"
district = "종로구"
todayString = '20250220'
currentTime = '1000'
x,y = make_districtPosion_dic.get_districtPosion_dic()[district]
URL = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey={KEY}&pageNo=1&numOfRows=1000&dataType=JSON&base_date={todayString}&base_time={currentTime}&nx={x}&ny={y}"
response = requests.get(URL)
data = response.json()
# print(data)
target_data = {"T1H":"기온", "RN1":"강수량", "REH":"습도", "PTY":"강수형태", "WSD":"풍속"}

print(data["response"]["body"]["item"]["item"])

