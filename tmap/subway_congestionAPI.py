import requests,json,os

def make_json():
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
    with open("./data/subway_stations_id.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)  # JSON 저장
    print("JSON 데이터가 subway_stations_id.json 파일로 저장되었습니다.")

def make_subway_stations_id():
    try:
        stations_id = set_code()
    except:
        print("Fail to  open json")
        make_json()
        stations_id = set_code()
    return stations_id

def set_code():
    res = dict()
    with open("./_data/subway_stations_id.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    for station_data in data["contents"]:
        res[station_data["stationName"]] = station_data["stationCode"]

    return res

if __name__ == "__main__":
    sc = make_subway_stations_id()
    print(sc)