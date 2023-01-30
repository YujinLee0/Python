from collections import deque

class StationNode:
    """ 지하철 역을 나타내는 역 """
    def __init__(self, station_name):
        self.station_name = station_name
        self.adjacent_stations = []
        self.visited = False
        self.predecessor = None

    def add_connection(self, station):
        """ 파라미터로 받은 역과 엣지를 만들어주는 메소드 """
        # 현재 지하철역 self와 연결하려는 station을 인접리스트에 저장
        self.adjacent_stations.append(station)
        # 연결하려는 station에도 현재 지하철 역을 인접리스트에 저장 (현재 역은 self 노드로 받고있으므로 self를 추가해주면 된다.)
        station.adjacent_stations.append(self)

    def __str__(self):
        """ 지하철 노드 문자열 메소드, 지하철 역 이름과 연결 된 역들을 모두 출력해준다. """
        res_str = f"{self.station_name}: " # 리턴할 역 이름
        # 리턴할 문자열에 인접한 역 이름들 저장
        for station in self.adjacent_stations:
            res_str += f"{station.station_name} " # 리턴할 역과 인접한 역 저장

        return res_str

def create_subway_graph(input_file):
    """ input file에서 데이터를 읽어 와서 지하철 그래프를 리턴하는 함수 """
    stations = {} # 지하철 역 노드들을 담을 딕셔너리

    with open(input_file) as station_raw_file:
        for line in station_raw_file:
            previous_station = None # 엣지를 저장하기위한 도우미 변수. (현재 보고 있는 역 전 역을 저장한다.)
            subway_line = line.strip().split("-") # 앞뒤 띄어쓰기 없애고 '-'를 기준점으로 데이터 나누기
            for name in subway_line:
                station_name = name.strip() # 앞 뒤 띄어쓰기 없애기

                # 지하철역 이름이 이미 저장한 key인지 학인 ( 해당 txt파일은 노선에 대한 정리로 역의 중복이 존재 )
                if station_name not in stations:
                    current_station = StationNode(station_name) # 새로운 인스턴스 생성
                    stations[station_name] = current_station # dictionary에 역 이름은 key로 역 노드 인스턴스를 value로 저장한다.

                else:
                    current_station = stations[station_name]

                if previous_station is not None:
                    current_station.add_connection(previous_station)
                previous_station = current_station

    return stations

stations = create_subway_graph('stations.txt')
# for station in sorted(stations.keys()):
#     print(stations[station])

def bfs1(graph, start_node):
    """ 시작 노드에서 bfs를 실행하는 함수 """
    queue = deque()

    # 모든 노드를 방문하지 않은 노드로 표시
    for station_node in graph.values():
        station_node.visited = False

    # 시작점 노드를 방문표시 후 큐에 넣어준다.
    start_node.visited = True
    queue.append(start_node)

    while queue: # 큐에 노드가 있는 동안
        current_station = queue.popleft() # 큐의 가장 앞 데이터를 가지고 온다.
        for neighbor in current_station.adjacent_stations:
            if not neighbor.visited:
                neighbor.visited = True
                queue.append(neighbor)

def bfs2(graph, start_node):
    """ 최단 경로용 BFS 함수 """
    queue = deque() # 빈 큐 생성

    # 모든 노드를 방문하지 않은 노드로 표시, 모든 predecessor는 None으로 초기화
    for station_node in graph.values():
        station_node.visited = False
        start_node.predecessor = None

    start_node.visited = True
    queue.append(start_node)

    while queue: # 큐에 노드가 있을 때 까지
        current_station = queue.popleft() # 큐의 가장 앞 데이터를 가지고온다.

        for neighbor in current_station.adjacent_stations: # 인접하 노드들을 돌면서
            if not neighbor.visited: # 방문하지 않은 노드면 방문표시를 하고 큐에 넣는다.
                neighbor.visited = True
                neighbor.predecessor = current_station
                queue.append(neighbor)

def back_track(destination_node):
    """ 최단 경로를 찾기 위한 back tracking 함수 """
    res_str = "" # 리턴할 역
    temp = destination_node # 도착 노드에서 시작 노드까지 찾아가는데 사용할 변수

    # 시작 노드까지 갈 때 까지
    while temp is not None:
        res_str = f"{temp.station_name} {res_str}" # 결과 문자열에 역 이름을 더하고
        temp = temp.predecessor # Temp를 다음 노드로 바꿔준다.

    return res_str

stations = create_subway_graph("new_stations.txt")
bfs2(stations, stations["지식정보단지"]) # 지하철 그래프에서 _역을 시작 노드로 bfs 실행
print(back_track(stations['송도'])) # _에서 ~까지 최단 경로 출력