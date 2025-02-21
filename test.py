import json

with open("tmap_subway.json", "r", encoding="UTF-8") as f:
    data = json.load(f)



print(data["metaData"]["plan"]["itineraries"][0])