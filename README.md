# 출근비서
- 박호윤, 박지수, 박지호, 박현민

weather - 기상청 단기 예보API 활용 실시간 날씨 정보 요청
    https://www.data.go.kr/data/15084084/openapi.do

airconrition - 서울시 권역별 실시간 대기환경 현황API 활용 실시간 미세먼지 데이터 요청
    http://data.seoul.go.kr/dataList/OA-2219/S/1/datasetView.do

tmap - TmapAPI활용 데이터 요청
    getLoc - 좌표 검색
        Geocoder: GeocoderAPI를 활용한 주소-좌표 변환 모듈
            https://www.vworld.kr/dev/v4dv_geocoderguide2_s001.do
        get_stationXY: 지하철 정보 데이터시트에서 해당 지하철 위치 검색
    
    public_transportation -tmap 대중교통 API 활용 여행 경로 검색(요청)
        https://transit.tmapmobility.com/

    TMapRouteFinder - tmapAPI활용 자동차 경로 정보 검색

Subway - 지하철 가중치 계산 모듈