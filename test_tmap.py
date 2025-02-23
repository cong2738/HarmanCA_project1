
from tmap.getLoc.geocoder import Geocoder

rode_id = "서울 강서구 공항대로 525"
rode_type = "ROAD"
gloc = Geocoder(rode_id, rode_type)
print(gloc.location())