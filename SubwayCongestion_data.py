"""
modDate: 2025-02-21
 서교공 지하철 혼잡도(20241231기준) 가공
 input: _
 output: 해당시간 혼잡도 csv
"""

import pandas as pd
def set_data():
    df = pd.read_csv("./data/weather_grid.csv", encoding="cp949") # 지하철혼잡도 데이터csv
    df = df["출발역", "격자 X",  "격자 Y"]#데이터 필터링
    df = df.dropna() #결측값이 들어간 데이터를 삭제한다.
    df = df.drop_duplicates(["2단계"]) #데이터 활용의 편의성을 위해 같은 구의 다른 좌표는 제거한다.
