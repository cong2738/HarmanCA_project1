from weather import kma_weather
from tmap import public_transportation
from Seoul_AirConrition import seoul_airCondition

"""
여기는 메인 실행 어플리케이션입니다. 
"""

weather = get_weather.kma_weather()
my_tmap = tmap()

weather.get_weatherDict()