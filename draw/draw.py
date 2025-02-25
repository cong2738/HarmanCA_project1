import pandas as pd
import matplotlib.pyplot as plt

# ✅ 한글 폰트 설정 (윈도우 & 맥 대응)
plt.rc('font', family='Malgun Gothic')  # Windows
# plt.rc('font', family='AppleGothic')  # Mac
plt.rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지

class draw_plot:
    def __init__(self, car_percentage, pub_percentage):
        """
        차량과 대중교통 백분율을 받아서 원형 그래프와 표를 함께 출력하는 클래스
        :param car_percentage: 차량 가중치 백분율 (float)
        :param pub_percentage: 대중교통 가중치 백분율 (float)
        """
        self.car_percentage = car_percentage
        self.pub_percentage = pub_percentage

    def traffic_pie_chart(self):
        """ 차량 vs 대중교통 가중치 비교 원형 그래프 + 표 삽입 """
        fig, ax = plt.subplots(figsize=(8, 10))

        # ✅ 파이 차트 (회전 90도 적용) + 퍼센트 값 추가
        labels = ["차량", "대중교통"]
        values = [self.car_percentage, self.pub_percentage]
        colors = ['blue', 'green']
        ax.pie(values, labels=labels, colors=colors, startangle=90, autopct='%1.1f%%', textprops={'fontsize': 12})
        ax.set_title("차량 vs 대중교통 가중치 비교", fontsize=14)

        # ✅ 표 데이터 변환 (퍼센트 값 포함)
        df = pd.DataFrame({
            "이동 수단": ["차량", "대중교통"],
            "가중치 비율 (%)": [f"{self.car_percentage * 100:.2f}%", f"{self.pub_percentage * 100:.2f}%"]
        })

        # ✅ 표 삽입 (차트 아래 배치)
        ax_table = plt.gca().table(
            cellText=df.values, 
            colLabels=df.columns, 
            cellLoc='center', 
            loc='bottom', 
            bbox=[0.25, -0.3, 0.5, 0.2]  # 표 위치 조정
        )
        ax_table.auto_set_font_size(False)
        ax_table.set_fontsize(12)

        plt.show()

def main():
    # ✅ 테스트용 고정 값 (API 값 대신 사용)
    car = 0.42857142857142855  # 차량 백분율
    pub = 0.5714285714285714  # 대중교통 백분율

    # ✅ **draw_plot 클래스 인스턴스 생성**
    plotter = draw_plot(car, pub)

    # ✅ **차트 + 표 출력**
    plotter.traffic_pie_chart()

if __name__ == "__main__":
    main()
