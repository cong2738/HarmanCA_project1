import requests,json,os
from getLoc.geocoder import Geocoder

class Trip:
    """
    티맵 대중교통API 활용 여행 경로 요청
        -input:
            num_of_routes:  경로 갯수
            start_adress:   출발위치 주소
            end_adress:     도착위치 주소
            adressType:     주소형식('ROAD':도로명 주소 'PARCEL':지번 주소)
        
        -object:
            routes:         경로리스트
    """
    def __init__(self, num_of_routes, start_adress, end_adress, adressType):
        try:
            self.routes = self.set_routes(num_of_routes)
        except:
            print("Fail to  open json")
            self.set_travel(start_adress, end_adress, adressType)
            self.routes = self.set_routes(num_of_routes)
    
    def get_routes(self):
        return self.routes

    def set_routes(self, n:int):
        res = list()
        with open("./data/tmap_publicTp.json", "r", encoding="UTF-8") as file:
            data = json.load(file)
        route_list = data["metaData"]["plan"]["itineraries"]
        for i in range(n):
            fare = route_list[i]["fare"]["regular"]["totalFare"]
            totalWalkTime = route_list[i]["totalWalkTime"]
            totalTime = route_list[i]["totalTime"]
            
            station_list = list()
            # ["WALK","SUBWAY","BUS"]
            for section in route_list[i]["legs"]:       
                section_type = section["mode"]
                if section_type == "WALK": continue
                # route = section["route"]
                passStopList = section["passStopList"]["stationList"]
                station_list = [station["stationName"] for station in passStopList]
            res.append([fare,totalTime,totalWalkTime,station_list])

        return res

    def set_travel (self, start_adress, end_adress, adressType):
        # API_KEY
        API_KEY = os.getenv("TMAP_PT_KEY")
        TEST_KEY = os.getenv("TMAP_TEST_KEY")

        # API URL
        URL = "https://apis.openapi.sk.com/transit/routes"
        
        start = Geocoder(start_adress, adressType)
        end = Geocoder(end_adress, adressType)


        # 두위치중 하나라도 None이라면 에러
        if not (start.location() and end.location()): 
            return None
        
        sx,sy = start.location()
        ex,ey = end.location()

        # 요청 헤더
        headers = {
            "accept": "application/json",
            "appKey": API_KEY,  # 실제 API 키 사용
            "content-type": "application/json"
        }

        # 요청 데이터 (JSON)
        data = {
            "startX": sx,
            "startY": sy,
            "endX": ex,
            "endY": ey,
            "lang": 0,
            "format": "json",
            "count": 10,
        }   

        # POST 요청 보내기
        response = requests.post(URL, json=data, headers=headers)
        
        # 비정상 응답시 에러
        if response.status_code != 200: 
            print(f"❌ API 호출 실패: {response.status_code}, {response.text}")
            return None

        # 응답 저장
        response_data = response.json()
        
        # JSON 데이터를 파일로 저장
        with open("./data/tmap_publicTp.json", "w", encoding="utf-8") as f:
            json.dump(response_data, f, ensure_ascii=False, indent=4)
        
        print("✅ tmap_trip.json 파일 저장 완료!")
    

if __name__ == "__main__":
    trip = Trip(1,"서울 양천구 목동로 201","서울 강서구 화곡로 179 ", "ROAD")
    print(*(trip.get_routes()), sep='\n')