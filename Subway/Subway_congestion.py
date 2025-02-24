import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    def calculate_congestion(self, station_name):
        subway_stations = self.remove_bus_stations()
        total_people = 0
        count = 0
        for idx, station in enumerate(subway_stations):
            if station == station_name:
                if self.condict.get(station, 0) == 0 and idx + 1 < len(subway_stations):
                    next_station = subway_stations[idx + 1]
                    total_people += self.condict.get(next_station, 0) * 0.8
                else:
                    total_people += self.condict.get(station, 0)
                count += 1

        if count == 0:
            return None

        avg_people = total_people / count
        congestion_percentage = (avg_people / 160) * 100

        return congestion_percentage

    def get_congestion_status(self, station_name):
        congestion_percentage = self.calculate_congestion(station_name)

        if congestion_percentage is None:
            return f"{station_name}의 혼잡도 정보가 없습니다."

        if congestion_percentage <= 80:
            status = '여유'
        elif 80 < congestion_percentage <= 130:
            status = '보통'
        elif 130 < congestion_percentage <= 150:
            status = '주의'
        else:
            status = '혼잡'

        return f'"{station_name}"의 혼잡도는 {congestion_percentage:.1f}%이므로 {status}한 상태입니다.'


def load_station_data(filepath):
    condict = {}
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            station, value = line.strip().split(",")
            station = station.replace("역", "")
            condict[station] = int(value)
    return condict
