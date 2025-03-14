import requests,json,os

class Subway_congestionAPI:
    """
    주의: API토큰먹는 괴물임
    """
    def __init__(self,stations:list):
        self.API_KEY = os.getenv("JIHO_TMAP_KEY")
        self.station_codes = self.set_subway_stations_code()
        self.station_congestionDict = self.set_congestionDict(stations)
    
    def get_station_congestionDict(self):
        return self.station_congestionDict
    
    def make_stationCode_json(self):
        # 요청 헤더
        url = "https://apis.openapi.sk.com/puzzle/subway/meta/stations"
        headers = {
            "appkey": self.API_KEY
        }
        params = {
            "offset": 0,
        }

        response = requests.get(url, headers=headers, params=params)
        print(response.content)
        if response.status_code != 200:
            print(f"Error {response.status_code}: {response.text}")  # 오류 메시지 출력
            return None

        data = response.json()  # JSON 데이터 변환    
        with open("./_data/subway_stations_code.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)  # JSON 저장
        print("JSON 데이터가 subway_stations_code.json 파일로 저장되었습니다.")

    def make_stationCongestion_json(self,station):
        station_name = station+"역"
        # 요청 헤더
        code = self.station_codes[station_name]
        url = f"https://apis.openapi.sk.com/puzzle/subway/congestion/stat/train/stations/{code}"
        headers = {
            "appkey": self.API_KEY
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
    
    def set_congestionDict(self, stations):
        congestionDict = dict()
        for station in stations:
            if station not in self.station_codes.keys():
                congestionDict[station] = self.set_congestion(station)
        return congestionDict
    
    
    def set_code(self):
        res = dict()
        with open("./_data/subway_stations_code.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
        for station_data in data["contents"]:
            res[station_data["subwayLine"] + " " + station_data["stationName"]] = station_data["stationCode"]

        return res
    
    def set_congestion(self,station):
        self.make_stationCongestion_json(station)
        res = dict()
        with open("./_data/stations_congestion.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
        res = data["contents"]["stat"][0]["data"][0]["congestionTrain"]
        return res

if __name__ == "__main__":
    # sc = subway_congestionAPI(['5호선 목동', '5호선 신정', '5호선 까치산', '5호선 화곡'])
    # print(sc.get_station_congestionDict())
    pass