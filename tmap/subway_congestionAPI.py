import requests,json,os

class Subway_congestion:
    def __init__(self,stations):
        congestion_dict = self.set_congestion(stations)
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

    def read_json(self,stations:list):
        try:
            self.congestions = self.set_routes()
        except:
            print("Fail to  open json")
            self.make_json()
            self.congestions = self.set_congestion(stations)

    def set_congestion(self,stations:list):
        res = list()
        with open("./_data/subway_congestion.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
        for station in stations:
            for station_data in data["contents"]:
                if station_data["stationName"] == station: continue

        return res

if __name__ == "__main__":
    sc = Subway_congestion([])