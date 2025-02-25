import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rc('font', family='Malgun Gothic') #한글 깨짐 방지  
plt.rcParams['axes.unicode_minus'] = False  
class draw_plot:
    
     def __init__(self, car_percentage, pub_percentage):
        """
        차량과 대중교통 백분율을 받아서 그래프를 출력하는 클래스
        :param car_percentage: 차량 가중치 백분율 (float)
        :param pub_percentage: 대중교통 가중치 백분율 (float)
        """
        self.car_percentage = car_percentage
        self.pub_percentage = pub_percentage

     def traffic_pie_chart(self): #파이차트 출력 메소드
        
        labels = ["차량", "대중교통"]
        values = [self.car_percentage, self.pub_percentage]
        colors = ['blue', 'green']

        plt.figure(figsize=(6, 6))
        plt.pie(values, labels=labels, colors=colors, startangle=90, textprops={'fontsize': 12})
        plt.title("차량 vs 대중교통 가중치 비교", fontsize=14)
        plt.show()


    
def main():
    # 테스트용 고정 값 (API 값 대신 사용)
        car = 0.42857142857142855  # 차량 백분율
        pub = 0.5714285714285714  # 대중교통 백분율

    # **DrawPlot 클래스 인스턴스 생성**
        plotter = draw_plot(car, pub)

    # 표 출력
        plotter.traffic_pie_chart()
    
   

if __name__ == "__main__":
    main()