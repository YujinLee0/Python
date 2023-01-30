""" 지하철 역 노드를 나타내는 클래스 """

class StationNode:
    def __init__(self, name, num_exits):
        self.name = name
        self.num_exits = num_exits

# 지하철 역 노드 인스턴스 생성
station_0 = StationNode("교대역", 14)
station_1 = StationNode("사당역", 14)
station_2 = StationNode("종로3가", 16)
station_3 = StationNode("서울역", 16)


# 노드들을 파이썬 리스트에 저장
stations = [station_0,station_1,station_2,station_3]
# 각각의 노드들이 특정 값을 갖기에 트리, 링크드 리스트에서 헤드노드로부터 원하는 노드를 찾았던 것과 달리 한번에 고유값을 통해 접근하기가 가능해짐

# 해시 테이블을 사용하여 저장하는 방식
_stations = {'교대역': station_0, "사당역": station_2, '종로3가역': station_2,'서울역': station_3}
node_1 = _stations["교대역"]

class StationNode:
    """간단한 지하철 역 노드 클래스"""
    def __init__(self, station_name):
        self.station_name = station_name

    def create_station_nodes(input_file):
        """input_file에서 데이터를 읽어 와서 지하철 그래프 노드들을 리턴하는 함수"""
        stations = {}  # 지하철 역 노드들을 담을 딕셔너리

        # 파라미터로 받은 input_file 파일을 연다
        with open(input_file) as stations_raw_file:
            for line in stations_raw_file:  # 파일을 한 줄씩 받아온다
                subway_line = line.strip().split("-")  # 앞 뒤 띄어쓰기를 없애고 "-"를 기준점으로 데이터를 나눈다

                for name in subway_line:
                    station_name = name.strip()  # 앞 뒤 띄어쓰기 없애기

                    # 지하철 역 이름이 이미 저장한 key 인지 확인
                    if station_name not in stations:
                        current_station = StationNode(station_name)  # 새로운 인스턴스를 생성하고
                        stations[station_name] = current_station  # dictionary에 역 이름은 key로, 역 노드 인스턴스를 value로 저장한다

        return stations

    stations = create_station_nodes("stations.txt")  # stations.txt 파일로 그래프 노드들을 만든다

# stations에 저장한 역들 이름 출력 (체점을 위해 역 이름 순서대로 출력)
for station in sorted(stations.keys()):
    print(stations[station].station_name)