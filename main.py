from tmap import public_transportation, subway_congestionAPI
from weather import kma_weather
from airconrition import seoul_airCondition

"""
여기는 메인 실행 어플리캐이션입니다..
"""

weather = kma_weather.KMA_Weather()
aircondition = seoul_airCondition.Seoul_Air_Quality()

n = 4
pt_param = {
    "num_of_routes" : n,
    "start_adress" : "서울 양천구 목동로 201",
    "end_adress" : "서울 강서구 화곡로 179",
    "adress_type" : "ROAD"
}
my_tmap =public_transportation.Trip(*pt_param.values())
# sbway_congestion = subway_congestionAPI.Subway_congestionAPI()


print(weather.get_weatherDict())
print(aircondition.get_Air_Qualitys())
print(*my_tmap.get_routes(), sep='\n')

# station_congestionDict = subway_congestion.get_station_congestionDict()
# print(station_congestionDict)

station_congestionDict = {'5호선 목동': 25, '5호선 신정': 25, '5호선 까치산': 28, '5호선 화곡': 28}