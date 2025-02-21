import json

class Get_starionXY:
    def __init__(self, station_name):
        self.XY = self.set_XY(station_name)

    def set_XY(self, station_name):
        result = self.set_station_location(station_name)
        return (result['위도'],result['경도']) if result else None

    def set_station_location(self, station_name):
        # JSON 데이터 (파일에서 불러오는 경우와 동일한 구조라고 가정)
        with open ("./data/seoul_subwaystation.json", "r", encoding="UTF-8") as f:
            json_data = json.load(f)
        for item in json_data["DATA"]:
            if item["bldn_nm"] == station_name:
                return {"역사명": station_name, "위도": float(item["lat"]), "경도": float(item["lot"])}
        return None  # 해당 역사명이 없을 경우
    
    def get_stationLoc(self):
        return self.XY

if __name__ == "__main__":
    station_name = "시청"
    station_loc = Get_starionXY(station_name)
    print(station_loc.get_stationLoc())
