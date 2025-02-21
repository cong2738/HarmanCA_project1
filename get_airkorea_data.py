import requests
key = _
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustWeekFrcstDspth'
params ={'serviceKey' : key, 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'searchDate' : '2020-11-09' }
response = requests.get(url, params=params)
print(response.content)