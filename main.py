from Subway.Subway_congestion import SubwayCongestion
from tmap import public_transportation, subway_congestionAPI, TMapRouteFinder
from weather import kma_weather
from airconrition import seoul_airCondition

"""
여기는 메인 실행 어플리캐이션입니다..
"""

num_of_routes = 1
pt_param = {
    "start_adress" : "서울 양천구 목동로 201",
    "end_adress" : "서울 강서구 화곡로 179",
    "adress_type" : "ROAD"
}
carTrip = TMapRouteFinder.TMapRouteFinder(*pt_param.values())
my_tmap =public_transportation.Trip(num_of_routes, *pt_param.values())
# sbway_congestion = subway_congestionAPI.Subway_congestionAPI()
weather = kma_weather.KMA_Weather()
aircondition = seoul_airCondition.Seoul_Air_Quality()

seou_weather = weather.get_weatherDict()
get_Air_Qualitys = aircondition.get_Air_Qualitys()
totalFare,totalTime,totalWalkTime,stations = my_tmap.get_routes()
# station_congestionDict = subway_congestion.get_station_congestionDict()
# print(station_congestionDict)

station_congestionDict = {'5호선 목동': 25, '5호선 신정': 25, '5호선 까치산': 28, '5호선 화곡': 28}
subway_congestion = SubwayCongestion(stations, station_congestionDict)

subway_congestion.get_congestion_status()

#Car_weight CLASS
car_weight = TMapRouteFinder.Car_weight()

#Pub_weights CLASS
pub_weigh = public_transportation.Pub_weight()