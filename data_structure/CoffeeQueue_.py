import numpy as np

''' 큐 클래스 '''
class Queue:
    def __init__(self):
        self.q = list()  # 빈 리스트 생성

    def isEmpty(self):
        return len(self.q) == 0 # 큐 안에 원소가 있는 지 여부를 Bool로 반환

    def size(self):
        return len(self.q) # 큐의 사이즈 반환

    def enQueue(self, item):
        self.q.append(item) # 큐에 아이템 추가

    def deQueue(self): # 큐에 아이템 삭제 (큐이므로 가장 먼저 들어온 아이템 삭제)
        if self.isEmpty() == True: # 큐에 원소가 없을 경우
            return None
        else:
            return self.q.pop(0)

    def peek(self): # 가장 먼저 들어온 (앞에 있는) 아이템 반환
        return self.q[0]

    def getLast(self): # 가장 마지막에 들어온 아이템 반환
        return self.q[-1]

''' Cust 클래스 '''
class Cust:
    # 고객이 들어온 시간, 주문 시간, 나간 시간 관리
    def __init__(self, arriveTime, orderTime = None, outTime= None):
        self.arriveTime = arriveTime
        self.orderTime = orderTime
        self. outTime = outTime

''' Shop 클래스 '''
class Shop:
    def __init__(self):
        self.q = Queue() # 고객 대기열을 담을 큐 생성

    def getSize(self):
        return self.q.size()

    def entCust(self, cust):
        self.q.enQueue(cust) # 들어온 고객을 큐에 넣어줌

    # 현재 시간보다 outTime이 작은 고객에 대해 큐에서 삭제하기
    def outCust(self, curTime):
        while self.getSize() != 0 and self.q.peek().outTime < curTime:
            self.q.deQueue()

    def getLast(self):
        return self.q.getLast()


Cafe = Shop()
curTime = 0
while curTime < 14 * 60: # 오전 8시(0)에서 오후 10시까지 운영시간이므로 해당 운영시간 내를 조건으로 함.
    curTime += np.random.exponential(1)
    # outTime이 현재 시간에서 지난 고객들 대기열에서 제거해주기
    Cafe.outCust(curTime)
    cus = Cust(curTime)

    if Cafe.getSize() == 0:
        cus.orderTime = cus.arriveTime # 손님이 없으면 대기인원이 없으므로 바로 주문 가능하기에 동일 시간
    else:
        # 손님이 나갔을 때 주문이 가능하므로
        cus.orderTime = Cafe.getLast().outTime

    # 손님이 도착하여 커피를 주문하고 받는 시간의 확률변수 Y가 Y ~ N(1, 0.2^)이라고 가정했기에 손님이 커피를 가지고 나가는 시간은 아래와 같음.
    cus.outTime = cus.orderTime + np.random.normal(1, 0.2, 1)

    Cafe.entCust(cus)
    print(f"손님 도착시간: {cus.arriveTime}, 손님 주문 시간: {float(cus.orderTime)}, 손님 나간 시간: {float(cus.outTime)}, "
          f"현재 남은 손님 수: {int(Cafe.getSize())} ")

