"""
writer: 박호윤
기상청 관측소 데이터(엑셀)에서 서울시의 좌표관련 데이터만 추출
"""

import pandas as pd
def set_data(city):
    df = pd.read_csv("./data/weather_grid.csv", encoding="cp949") #기상청 관측소 데이터
    df = df.loc[(df["1단계"] == city)][["2단계", "격자 X",  "격자 Y"]] #기상청 관측소 데이터 필터링
    df = df.dropna() #결측값이 들어간 데이터를 삭제한다.
    df = df.drop_duplicates(["2단계"]) #데이터 활용의 편의성을 위해 같은 구의 다른 좌표는 제거한다.
    districtPosion_dic = dict() #지역구-날씨 딕셔너리
    #CSV데이터 딕셔너리에 저장
    for row in df.to_csv().split('\r\n')[1:-1]:  
        box = row.split(',')
        districtPosion_dic[box[1]] = (box[2],box[3])
    return districtPosion_dic #딕셔너리 반환

def get_districtPosion_dic():
    res = set_data("서울특별시")
    res.update(set_data("경기도"))    
    return res
