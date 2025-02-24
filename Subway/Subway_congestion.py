class SubwayCongestion:
    def __init__(self, stations, condict):
        self.stations = stations
        self.condict = condict

    def remove_bus_stations(self):
        subway_stations = []
        for station in self.stations:
            if station in self.condict:
                subway_stations.append(station)
        return subway_stations

    def calculate_total_congestion(self):
        subway_stations = self.remove_bus_stations()
        total_congestion = 0
        count = 0
        idx = 0

        while idx < len(subway_stations):
            station = subway_stations[idx]
            congestion = self.condict.get(station, 0)

            if congestion == 0:
                next_idx = idx + 1
                while next_idx < len(subway_stations):
                    next_congestion = self.condict.get(subway_stations[next_idx], 0)
                    if next_congestion != 0:
                        congestion = next_congestion * 0.8
                        break
                    next_idx += 1

            total_congestion += congestion
            count += 1
            idx += 1

        if count == 0:
            return 0, 0

        avg_congestion = total_congestion / count
        congestion_indicator = (total_congestion / avg_congestion) if avg_congestion != 0 else 0
        congestion_weight = (congestion_indicator / (congestion_indicator + 100)) * 0.1

        return total_congestion, total_congestion * congestion_weight

    def get_congestion_result(self):
        total_congestion, total_weighted_congestion = self.calculate_total_congestion()
        return f'최종 혼잡도: {total_congestion:.2f}, 최종 혼잡도 가중치 결과값은 {total_weighted_congestion:.2f}입니다.'


def load_station_data(filepath):
    data = {}
    with open(filepath, "r", encoding="utf-8") as file:
        exec(file.read(), {}, data)

    stations = data["stations"]
    condict = {key.replace("역", ""): value for key, value in data["condict"].items()}

    return stations, condict

