from tmap import public_transportation
from weather import kma_weather
from airconrition import seoul_airCondition


"""
여기는 메인 실행 어플리캐이션입니다. 
"""

weather = kma_weather.KMA_Weather()
aircondition = seoul_airCondition.Seoul_Air_Quality()

pt_param = {
    "num_of_routes" : 1,
    "start_adress" : "서울 양천구 목동로 201",
    "end_adress" : "서울 강서구 화곡로 179",
    "adress_type" : "ROAD"
}
my_tmap =public_transportation.Trip(*pt_param.values())

print(weather.get_weatherDict())
print(aircondition.get_Air_Qualitys())
print(my_tmap.get_routes())