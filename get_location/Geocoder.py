"""
modDate: 2025-02-21
Geocoder API 2.0을 활용한 주소-좌표 변환기
"""

import requests
import os

def XY_at(rode_id,road_type): #'ROAD':도로명 주소 'PARCEL':지번 주소
    key = os.getenv("V_WORLD_KEY") 
    import requests
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
    if response.status_code == 200:
        data = response.json()
        x,y = tuple(data["response"]["result"]["point"].values())
        
    return x,y

if __name__ == "__main__":
    print(geocoder_XYat("판교로 242","ROAD") )