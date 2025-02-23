import requests
import os
class Geocoder:
    """
    writer: 박호윤
    Geocoder API 2.0을 활용한 주소-좌표 변환기
    'ROAD':도로명 주소 'PARCEL':지번 주소
    검색 키워드
        지번주소 : 법정동 + 지번까지 입력
        ex) 관양동 1588-8
        ex) 경기도 안양시 동안구 관양동 1588-8

        도로명주소 : 시군구 + 도로명 + 건물번호 입력
        ex) 부림로169번길 22
        ex) 안양시 동안구 부림로169번길 22
    """

    def __init__(self, rode_id, rode_type):
        self.xy = self.setloc_at(rode_id,rode_type)
                                
    def setloc_at(self,rode_id,road_type): #'ROAD':도로명 주소 'PARCEL':지번 주소
        key = os.getenv("V_WORLD_KEY") 
        apiurl = "https://api.vworld.kr/req/address?"
        params = {
            "service": "address",
            "request": "getcoord",
            "crs": "epsg:4326",
            "address": rode_id,
            "format": "json",
            "type": road_type,
            "key": key
        }
        response = requests.get(apiurl, params=params)
        if response.status_code != 200: # 응답완료가 아닐시 에러
            return None
        
        data = response.json()["response"]
        if data["status"] != "OK": #비정상 상태시 에러
            return None
        
        (x,y) = tuple(data["result"]["point"].values())
            
        return x,y
    
    def location(self):
        return self.xy

if __name__ == "__main__":
    loc = Geocoder("판교로 242","ROAD")
    print(loc.location() )