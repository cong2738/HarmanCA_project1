import requests,json,os

class subway_congestionAPI:
    def __init__(self):
        station_code = self.set_subway_stations_code()
        station_congestionDict = self.set_station_congestion()
    
    def make_stationCode_json(self):
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
            return None

        data = response.json()  # JSON 데이터 변환    
        with open("./_data/subway_stations_code.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # JSON 저장
        print("JSON 데이터가 subway_stations_code.json 파일로 저장되었습니다.")

    def make_stationCongestion_json(self):
        # 요청 헤더
        API_KEY = os.getenv("TMAP_PT_KEY")
        url = "https://apis.openapi.sk.com/puzzle/subway/congestion/stat/train/stations/0"
        headers = {
            "appkey": API_KEY
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")  # 오류 메시지 출력
            return None

        data = response.json()  # JSON 데이터 변환    
        with open("./_data/stations_congestion.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # JSON 저장
        print("JSON 데이터가 stations_congestion.json 파일로 저장되었습니다.")

    def set_subway_stations_code(self):
        try:
            stations_id = self.set_code()
        except:
            print("Fail to  open json")
            self.make_stationCode_json()
            stations_id = self.set_code()
        return stations_id
    
    def set_station_congestion(self):
        try:
            station_congestion = self.set_congestion()
        except:
            print("Fail to  open json")
            self.make_stationCongestion_json()
            station_congestion = self.set_congestion()
        return station_congestion

    def set_code(self):
        res = dict()
        with open("./_data/subway_stations_code.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
        for station_data in data["contents"]:
            res[station_data["stationName"]] = station_data["stationCode"]

        return res
    
    def set_congestion(self):
        res = dict()
        with open("./_data/stations_congestion.json", "r", encoding="UTF-8") as file:
            data = json.load(file)

        return res

if __name__ == "__main__":
    sc = subway_congestionAPI()
    print(sc)