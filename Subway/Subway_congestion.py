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

    def remove_bus_stations(self) -> list:
        """
        버스 정류장을 목록에서 제거하고 지하철 역만 반환하는 메서드.

        Returns:
            list: 혼잡도 정보가 있는 지하철 역의 이름 목록.
        """
        return [station for station in self.stations if station in self.condict]

    def calculate_total_congestion(self) -> tuple:
        """
        선택된 지하철 역들의 총 혼잡도와 가중치를 계산하는 메서드.

        Returns:
            tuple: 총 혼잡도 (float)와 혼잡도 가중치 (float).
        """
        subway_stations = self.remove_bus_stations()
        total_congestion = 0
        count = len(subway_stations)

        for idx, station in enumerate(subway_stations):
            congestion = self.condict.get(station, 0)
            if congestion == 0:
                congestion = next(
                    (self.condict.get(subway_stations[next_idx], 0) * 0.8
                     for next_idx in range(idx + 1, len(subway_stations))
                     if self.condict.get(subway_stations[next_idx], 0) != 0),
                    0
                )
            total_congestion += congestion

        if count == 0:
            return 0, 0

        avg_congestion = total_congestion / count

        # 혼잡도가 높을수록 가중치가 낮아지는 로직
        congestion_indicator = avg_congestion
        congestion_weight = (100 / (congestion_indicator + 100))

        # 가중치가 0 미만이면 0으로 처리
        congestion_weight = max(congestion_weight, 0)

        return total_congestion, congestion_weight

    def get_congestion_result(self) -> str:
        """
        총 혼잡도와 가중치를 계산하여 결과 문자열을 반환하는 메서드.

        Returns:
            str: 총 혼잡도와 가중치를 포함한 결과 문자열.
        """
        total_congestion, congestion_weight = self.calculate_total_congestion()
        return (f'최종 혼잡도: {total_congestion:.2f}, '
                f'최종 혼잡도 가중치 결과값은 {congestion_weight:.2f}입니다.')

    def set_selected_stations(self, selected_stations: list):
        """
        분석할 지하철 역을 선택하는 메서드.

        Args:
            selected_stations (list): 선택된 지하철 역의 이름 목록.
        """
        self.stations = selected_stations


def load_station_data(filepath: str) -> tuple:
    """
    파일에서 역 정보와 혼잡도 데이터를 로드하는 함수.

    Args:
        filepath (str): 역 정보와 혼잡도 데이터가 저장된 파일의 경로.

    Returns:
        tuple: 역 이름 목록 (list)과 역별 혼잡도 사전 (dict).
    """
    data = {}
    with open(filepath, "r", encoding="utf-8") as file:
        exec(file.read(), {}, data)

    stations = data["stations"]
    condict = {key.replace("역", ""): value for key, value in data["condict"].items()}

    return stations, condict
