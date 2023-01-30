import numpy as np

class SparseMatrix:
    def __init__(self,m,n):
        self.sm = [[m,n,0]] # non-zero가 몇개나 있는지 (header)
        self.m = m
        self.n = n

    def append(self, cell):
        self.sm.append(cell)
        self.sm[0][2] += 1 # cell을 추가할 때 마다 header에 non-zero 개수 하나씩 더 추가하기


    # 행렬의 shpae
    def shape(self):
        return self.m , self.n

    # 해당 행,렬에 있는 값 찾기
    def getValue(self, row, col):
        for i in range(1, len(self.sm)): # header가 첫번째 리스트 형태로 있으므로 이를 제외하고 +1 해줘야함
            if row == self.sm[i][0] and col == self.sm[i][1]:
                return self.sm[i][2]
        return 0 # 찾는게 없을경우

    # array 형식으로 저장된 것을 행렬 형태로 프린트
    def printArray(self):
        mat = np.zeros((self.m,self.n)) # 0의 행렬 리스트
        for i in range(1,len(self.sm)):
            mat[self.sm[i][0] -1, self.sm[i][1] -1] = self.sm[i][2] # 행렬의 시작은 0부터이ㅈ만 커퓨터에서는 0부터 저장하므로 1을 빼줘야함.
        print(mat)

    # 행렬의 합을 구하는 클래스 메소드
    @classmethod
    def add(cls, a, b):
        c = SparseMatrix(a.m, a.n)  # 행렬의 합을 저장할 빈 희소행렬 생성
        if a.m != b.m or a.n != b.n: # 행렬의 shape이 다르면 연산이 불가능하므로
            return 1
        else:
            u = set() # 두 행렬에서의 non zero값 위치를 저장해줄 셋
            for i in range(1, a.sm[0][2]+1): # a 행렬의 길이만
                u.add((a.sm[i][0], a.sm[i][1])) # non-zero들의 m,n d 위치 저장
            for i in range(1, len(b.sm)):
                u.add((b.sm[i][0],b.sm[i][1]))
            for term in list(u):
                # 각각의 non zero의 위치들이 들어있는 u에 대해 각 위치의 a,b 숫자를 더하기
                _tmp = a.getValue(term[0],term[1]) + b.getValue(term[0],term[1])
                # 둘 둥 하나라도 non zero 값이 들어있어 tmp가 0이 아닐 경우
                if _tmp != 0:
                    c.append([term[0], term[1], _tmp])
            return c


A = SparseMatrix(3,3)
A.append([1,1,1])
A.append([2,2,2])
A.append([3,3,3])
print(A.sm)   # 저장하는건 이 형태
A.printArray() # 사용자에게 보여주는 건 이 형태 => 저장공간 효율적 사용

B = SparseMatrix(3,3)
B.append([1,1,1])
B.append([1,2,1])
B.append([2,2,1])
B.append([2,3,1])
B.append([3,3,1])
B.printArray()

C = SparseMatrix.add(A,B)
C.printArray()

