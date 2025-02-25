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
        self.con_avg = self.set_conavg_stations()
        self.weight = self.set_weight()

    def set_weight(self,con_avg):
        
        pass   

    def get_weight(self):
        return self.weight
    
    def set_conavg_stations(self):
        for i, station in enumerate(self.stations):
            if self.condict[station] != 0: break
        
        target_data = self.stations[i]
        target_idx = i

        for j in range(target_idx):
            self.condict[self.stations[j]] = target_data
        
        con_avg = sum(self.condict.values())/len(self.condict.values())

        return con_avg

    
    def get_congestion_result(self) -> str:
        """
        평균 및 가중치 출력 매소드

        Returns:
            str: 총 혼잡도와 가중치를 포함한 결과 문자열.
        """
        print (f'역 평균균 혼잡도: {self.con_avg:.2f}, 최종 혼잡도 가중치 결과값은 {self.weight:.2f}입니다.')


        def algo_first(self):

            stations = {'5호선 목동': 50, '5호선 신정': 50, '5호선 까치산': 50, '5호선 화곡': 50}

            flag = 0

            for i,sta in enumerate(stations):
                if sta == 0:
                    continue
                flag = flag + 1

            
    
    
        








        def load_station_data(filepath: str) -> tuple:
        
            data = {}
        with open(filepath, "r", encoding="utf-8") as file:
            exec(file.read(), {}, data)

        stations = data["stations"]
        condict = {key.replace("역", ""): value for key, value in data["condict"].items()}

        return stations, condict
    
    """
        파일에서 역 정보와 혼잡도 데이터를 로드하는 함수.

        Args:
            filepath (str): 역 정보와 혼잡도 데이터가 저장된 파일의 경로.

        Returns:
            tuple: 역 이름 목록 (list)과 역별 혼잡도 사전 (dict).
        """

     

    


    