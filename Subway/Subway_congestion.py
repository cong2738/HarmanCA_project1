import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SubwayCongestion:
    def __init__(self, file_path):
       
       

    def get_congestion(self, station, time):
        """ 특정 역과 시간대의 혼잡도 반환 """
        filtered_data = self.df[self.df['출발역'] == station]
        if filtered_data.empty:
            return None
        return filtered_data[time].values[0]

    def calculate_avg_congestion(self, selected_stations, time):
        """ 사용자가 입력한 역들의 특정 시간 평균 혼잡도 계산 """
        congestions = [self.get_congestion(station, time) for station in selected_stations if self.get_congestion(station, time) is not None]
        if not congestions:
            return 0
        
        base_avg = np.mean(congestions)
        
        # 역 개수 증가 시 가중치 반영 (예: 5% 증가)
        adjustment_factor = 1 + (len(selected_stations) - 2) * 0.05  
        adjusted_avg = base_avg * adjustment_factor
        
        return min(adjusted_avg, 100)  # 100을 넘지 않도록 제한

  