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
carTrip = TMapRouteFinder.TMapRouteFinder(*pt_param.values()) #TMAP차량지도API CLASS
my_tmap =public_transportation.Trip(num_of_routes, *pt_param.values()) #TMAP대중교통API CLASS
# sbway_congestion = subway_congestionAPI.Subway_congestionAPI() #TMAP지하철혼잡도API CLASS
weather = kma_weather.KMA_Weather() #단기기상예보API CLASS
aircondition = seoul_airCondition.Seoul_Air_Quality() #서울미세먼지현황API CLASS

seoul_weather = weather.get_weatherDict() #날씨dictionary 
ari_condition = aircondition.get_Air_Qualitys() #미세먼지정보 dictionary
totalFare,totalTime,totalWalkTime,stations = my_tmap.get_routes()[0] #0번 루트의 요금, 시간, 걷는시간, 경로의 역들
# station_congestionDict = subway_congestion.get_station_congestionDict() #혼잡도정보 dictionary
station_congestionDict = {'5호선 목동': 25, '5호선 신정': 25, '5호선 까치산': 28, '5호선 화곡': 28} # 토큰증발을 방지하기 위해 사용하는 임시데이터

subway_congestion = SubwayCongestion(stations, station_congestionDict) #지하철 혼잡도 계산CLASS
sub_weight = subway_congestion.get_weight() #지하철 루트 혼잡도평균

#Car_weight CLASS
car_weight = TMapRouteFinder.Car_weight()

#Pub_weights CLASS
pub_weigh = public_transportation.Pub_weight(seoul_weather, ari_condition, sub_weight)

cw = car_weight.get_carweight()
pw = pub_weigh.get_weight()

#차와 대중교통의 비교를 위한 백분율 계산
cwpw = cw+pw
car = cw/cwpw
pub = pw/cwpw

print(f"{car}:{pub}")