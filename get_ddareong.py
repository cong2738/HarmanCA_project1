import requests
from os import getenv

key = getenv("SEOUL_API_KEY")
url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params ={'KEY' : key, 
         'TYPE' : 'json', 
         'SERVICE' : 'bikeList', 
         'START_INDEX' : '0', 
         'END_INDEX' : '100',
         }
response = requests.get(url, params=params)
print(response.content)