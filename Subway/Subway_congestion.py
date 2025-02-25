class SubwayCongestion:
    def __init__(self, stations, condict):
        self.stations = stations
        self.condict = condict

    def remove_bus_stations(self):
        return [station for station in self.stations if station in self.condict]

    def calculate_total_congestion(self):
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

        # 혼잡도가 높을수록 가중치가 낮아지는 올바른 로직
        congestion_indicator = avg_congestion
        congestion_weight = (100 / (congestion_indicator + 100))

        # 0 미만이면 0으로 처리 (사실상 불가능하지만 안전장치)
        congestion_weight = max(congestion_weight, 0)

        return total_congestion, congestion_weight

    def get_congestion_result(self):
        total_congestion, congestion_weight = self.calculate_total_congestion()
        return (f'최종 혼잡도: {total_congestion:.2f}, '
                f'최종 혼잡도 가중치 결과값은 {congestion_weight:.2f}입니다.')

    def set_selected_stations(self, selected_stations):
        self.stations = selected_stations


def load_station_data(filepath):
    data = {}
    with open(filepath, "r", encoding="utf-8") as file:
        exec(file.read(), {}, data)

    stations = data["stations"]
    condict = {key.replace("역", ""): value for key, value in data["condict"].items()}

    return stations, condict

