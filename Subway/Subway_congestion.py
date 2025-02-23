import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SubwayCongestion:
    def __init__(self, file_path):
        """ CSV 파일 로드 및 데이터 전처리 (역 목록 자동 설정) """
        try:
            self.df = pd.read_csv(file_path, encoding='cp949')
        except UnicodeDecodeError:
            self.df = pd.read_csv(file_path, encoding='utf-8')
        
        # 데이터 타입 변환 (문자 → 숫자)
        for col in self.df.columns[5:]:  # 5번째 컬럼 이후 (시간대 데이터)
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')
        
        # 혼잡도 정규화 (최댓값을 100으로 변환)
        self.df.iloc[:, 5:] = self.df.iloc[:, 5:].apply(lambda x: (x / x.max()) * 100)

        # 📌 CSV 파일에서 자동으로 역 목록 가져오기
        self.stations = [self.df['출발역'].unique().tolist()]  # 2차원 리스트 형태로 저장

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

    def plot_congestion_change(self, selected_stations, times):
        """ 선택한 시간대의 혼잡도 변화 그래프 """
        congestion_values = [self.calculate_avg_congestion(selected_stations, time) for time in times]
        
        plt.figure(figsize=(10, 5))
        plt.plot(times, congestion_values, marker='o', linestyle='-', color='b')
        plt.xlabel("시간대")
        plt.ylabel("평균 혼잡도")
        plt.title(f"시간대별 평균 혼잡도 변화 ({', '.join(selected_stations)})")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
