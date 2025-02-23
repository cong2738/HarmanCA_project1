from weather import kma_weather
from tmap import public_transportation
from airconrition import seoul_airCondition

"""
여기는 메인 실행 어플리캐이션입니다. 
"""

start_adress = "서울 양천구 목동로 201"
end_adress = "서울 강서구 화곡로 179"
adress_type = "ROAD"

weather = kma_weather.KMA_Weather()
aircondition = seoul_airCondition.Seoul_Air_Quality()
my_tmap = public_transportation.Trip(1, start_adress, end_adress, adress_type)

print(weather.get_weatherDict())
print(aircondition.get_Air_Qualitys())
print(my_tmap.get_routes())