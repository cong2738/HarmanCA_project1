import requests,json,os

def make_json(self):
    # 요청 헤더
    API_KEY = os.getenv("TMAP_PT_KEY")

    url = "https://apis.openapi.sk.com/puzzle/subway/meta/stations"
    headers = {
        "appkey": API_KEY
    }
    params = {
        "offset": 0,
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")  # 오류 메시지 출력

    data = response.json()  # JSON 데이터 변환    
    with open("./data/subway_congestion.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # JSON 저장
    print("JSON 데이터가 subway_congestion.json 파일로 저장되었습니다.")

def read_json(self):
    try:
        self.congestion_json = self.set_routes()
    except:
        print("Fail to  open json")
        self.make_json()
        self.congestion_json = self.set_congestion_json()