
class stationNode:
    """ 지하철 역을 나타내는 노드 설정하기 """
    def __init__(self, stationName):
        self.stationName = stationName
        self.adjacentStations = []
        self.visited = False # 방문 여부를 저장할 변수
        self.predecessor = None # 방문 직전의 노드를 저장할 변수
        self.distance = None
        self.cost = []

    def addConnection(self, station, cost):
        """ 파라미터로 받은 역과 엣지를 만들어주는 메소드 """
        # 현재 지하철역 self와 연결하려는 station을 인접리스트에 저장
        self.adjacentStations.append(station)
        self.cost.append(cost)
        # 연결하려는 station에도 현재 지하철 역을 인접리스트에 저장 (현재 역은 self 노드로 받고있으므로 self를 추가해주면 된다.)
        station.adjacentStations.append(self)
        station.cost.append(cost)

    def __str__(self):
        """ 지하철 노드 문자열 메소드, 지하철 역 이름과 연결된 역들을 모두 출력해준다. """
        res_str = f"{self. stationName}: "
        for i in range(len(self.adjacentStations)):
            res_str += f"{self.adjacentStations[i].stationName} - " \
                       f"거리: {self.cost[i]} ||  "
        return res_str

class Dijkstra:
    """ 지하철 역들을 연결해주는 다익스트라 알고리즘 클래스 """
    def __init__(self, file):
        self.stations = {}

        with open(file) as stationFile:
            for line in stationFile:
                previous_station = None
                subwayLine = line.strip().split(",")

                for name in subwayLine[:2]:
                    stationName = name.strip()

                    if stationName not in self.stations:
                        currentStation = stationNode(stationName)
                        self.stations[stationName] = currentStation
                    else:
                        currentStation = self.stations[stationName]

                    if previous_station is not None:
                        currentStation.addConnection(previous_station, subwayLine[2])
                    previous_station = currentStation

    def __str__(self):
        ret = ""
        for station in sorted(self.stations.keys()):
            ret += f"{self.stations[station]}\n"
        return ret

    def dijkstra(self, strtNode):
        """ 최단 경로 찾기 """

        # 모든 노드들을 방문하지 않은 노드로 표시, predecessor 초기화, 거리는 무한대 설정
        for stationNode in self.stations.values():
            stationNode.visited = False
            stationNode.predecessor = None
            stationNode.distance = float("inf")

        visitedCnt = 0
        strtNode.distance = 0
        temp = strtNode
        #
        # while visitedCnt < len(self.stations):
        #     for neighbor in temp.adjacentStations:
        #         if neighbor.distance > temp.dis

        if stationNode.stationName == strtNode:
            startNode = stationNode

        # 시작노드에 대해 방문표시, 거리0으로 설정, predecessor None
        startNode.visited = True
        startNode.distance = 0

        while True:
            unvisit = []
            for statNode in self.stations.values():
                if statNode.visited == False:
                    unvisit.append(statNode)

            for stationNode in self.stations.values():
                minNode = min(stationNode.distance)

                minNode.visited = True
                unvisit.remove(minNode)

                for neighbor in minNode.adjacentStations:
                    if not neighbor.visited:
                        _idx = minNode.adjacentStations.index(neighbor)
                        dis = minNode.cost(_idx)
                        dis += minNode.distance  # 가중치 값(cost) + 거리(distance)
                        if dis < neighbor.distance:
                            neighbor.predecessor = minNode
                            neighbor.distance = dis

            if unvisit == []:
                break


    def backTrack(self, destinationNode):
        """ 최단 경로 찾기위한 함수 """
        res_str = ""
        temp = destinationNode

        while temp is not None:
            res_str = f"{temp.station_name} {res_str}"  # 결과 문자열에 역 이름을 더하고
            temp = temp.predecessor  # Temp를 다음 노드로 바꿔준다.

        return res_str


stations = Dijkstra('subway.csv')
# print(stations)
stations.dijkstra("홍대입구(2)")
print(stations.backTrack(stations['강남(2)']))

