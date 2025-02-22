import get_weather
import tmap

"""
여기는 메인 실행 어플리케이션입니다. 
"""

weather = get_weather.kma_weather()
my_tmap = tmap()

weather.get_weatherDict()