class SubwayCongestion:
    def __init__(self, stations: list, condict: dict):
        """
        지하철 혼잡도 계산을 위한 클래스 초기화 메서드.

        Args:
            stations (list): 지하철 역의 이름 목록.
            condict (dict): 각 역의 혼잡도 정보를 담은 사전.
        """
        self.stations = stations
        self.condict = condict
        self.con_avg = self.set_conavg_stations() #역 평균 혼잡도
        self.weight = self.set_weight() #최종 혼잡도 가중치 결과값

   
        
    def set_weight(self):
        
        self.con_avg
        effective = self.con_avg
        
        # if/elif를 통해 단위 계단 함수의 조건에 따른 multiplier 결정
        if effective >= 80:
            multiplier = 0.2
        elif effective >= 60: #혼잡
            multiplier = 0.3
        elif effective >= 40: #보통
            multiplier = 0.5
        else:
            multiplier = 1  #여유(1에 가까울수록 여유로움움)

        
        weight = multiplier
        return weight

    def get_weight(self): 
        return self.weight
    
    def set_conavg_stations(self): 
        """
        혼잡도가 비어있는(0)인 지하철의 혼잡도를 채워주고 평균을 계산
        """       
        for i, station in enumerate(self.stations):
            if self.condict[station] != 0: break
        
        target_data = self.condict[self.stations[i]]
        target_idx = i

        stations_len = len(self.stations)
        if target_idx == stations_len - 1: 
            target_data = 20 # 평균 CSV 보면서 값 조정해나가면 됨
            for station in self.stations:
                self.condict[station] = target_data

        for j in range(target_idx):
            self.condict[self.stations[j]] = target_data
        
        con_avg = sum(self.condict.values())/len(self.condict.values())
        return con_avg

    
    def print_congestion_result(self) -> str:
        """
        평균 및 가중치 출력 매소드

        Returns:
            str: 총 혼잡도와 가중치를 포함한 결과 문자열.
        """
        print (f'역 평균 혼잡도: {self.con_avg:.2f}, 최종 혼잡도 가중치 결과값은 {self.weight:.2f}입니다.')

   