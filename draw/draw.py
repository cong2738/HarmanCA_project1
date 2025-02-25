import pandas as pd
import matplotlib.pyplot as plt

class draw_plot:
    
     def __init__(self, car_percentage, pub_percentage):
        """
        차량과 대중교통 백분율을 받아서 표와 그래프를 출력하는 클래스
        :param car_percentage: 차량 가중치 백분율 (float)
        :param pub_percentage: 대중교통 가중치 백분율 (float)
        """
        self.car_percentage = car_percentage
        self.pub_percentage = pub_percentage

     def display_table(self):
        """ 백분율 데이터를 표로 출력 """
        data = {
            "이동 수단": ["차량", "대중교통"],
            "가중치 비율": [self.car_percentage, self.pub_percentage]
        }
        df = pd.DataFrame(data)
        print(df)

        def plot_comparison(self):
            """ 차량 vs 대중교통 가중치를 막대 그래프로 출력 """
        labels = ["차량", "대중교통"]
        values = [self.car_percentage, self.pub_percentage]

        plt.figure(figsize=(6, 4))
        plt.bar(labels, values, color=['blue', 'green'])
        plt.xlabel("이동 수단")
        plt.ylabel("가중치 비율")
        plt.title("차량 vs 대중교통 가중치 비교")
        plt.ylim(0, 1)  # 백분율이므로 0~1 범위 설정
        plt.show()
    