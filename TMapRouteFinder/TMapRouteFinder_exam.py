from TMapRouteFinder import TMapRouteFinder

api_key = "KEY"  # 🚨 실제 API 키 입력 필수
route_finder = TMapRouteFinder(api_key)

start_x, start_y = 126.798153, 37.578608  # 개화산
end_x, end_y = 126.864931, 37.526065  # 목동

route_info = route_finder.get_route(start_x, start_y, end_x, end_y)
# 최단 거리(1) 옵션으로 경로 탐색
route_info_shortest = route_finder.get_route(start_x, start_y, end_x, end_y, search_option=1)
