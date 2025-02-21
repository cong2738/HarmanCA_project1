import requests
from os import getenv

key = getenv("DATAGOKR_API_KEY")
url = 'http://apis.data.go.kr/B552584/UlfptcaAlarmInqireSvc/getUlfptcaAlarmInfo'
params ={'serviceKey' : key, 
         'returnType' : 'json', 
         'numOfRows' : '100', 
         'year' : '2020', 
         'itemCode' : 'PM10' 
         }
response = requests.get(url, params=params)
print(response.content)