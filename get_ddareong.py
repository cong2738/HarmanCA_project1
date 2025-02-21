import requests
from os import getenv

key = getenv("SEOUL_API_KEY")
url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params ={'KEY' : key, 
         'TYPE' : 'json', 
         'SERVICE' : '100', 
         'START_INDEX' : '2020', 
         'END_INDEX' : 'PM10',
         'stationId' : 'STRING(선택)'
         }
response = requests.get(url, params=params)
print(response.content)