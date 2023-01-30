class Stack:
    def __init__(self):
        self.s = []
    # 스택의 top에 원소를 삽입하는 연산
    def push(self, item):
        self.s.append(item)
    # 스택이 공백인지 아닌지를 확인하는 연산
    def isEmpty(self):
        return len(self.s) == 0 # Boolean 값으로 저장
    # 스택의 top에 있는 원소를 삭제하고 반환하는 연산
    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(-1)  # 가장 최근에 저장된 값을 pop
        else:
            return None

    def size(self):
        return len(self.s)
    # 스택의 top에 있는 원소를 반환하는 연산
    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None

s = Stack()
s.push("Apple")
s.push("Pear")
s.push("Cherry")

print(s.peek)

for i in range(5):
    print(s.pop()) # 3개의 아이템만 저장되어있으므로 이후에는 none을 리턴

# Stack 응용문제: 문자열 reverse

def reverse(a):
    s = Stack()
    b = ""
    for i in range(len(a)):
        s.push(a[i])
    for i in range(len(a)):
        b += s.pop()
    return b

a = "abcdefg"
print(reverse(a))

# 수식 괄호 체크 응용문제

def eqBraketCheck(f):
    s = Stack()
    for i in range(len(f)):
        if f[i] == '(':
            s.push(f[i])
        elif f[i] == ")":
            if s.pop() == None:
                return False
    if s.isEmpty() == True:
        return True
    else:
        return False
f = '(1+2) + (3+4)) ='
eqBraketCheck(f)

print(eval(" 12.2 + (2*3) "))  # eval 함수는 수식을 입력받아 결과값을 리턴한다.

''' Postfix Algorithm (수식후위 표기 알고리즘)'''
# 연산자 여부 리턴
def isOper(item):
    if item == '+' or item == '-' or item == '*' or item == '/':
        return True
    else:
        return False

# 주어진 문자가 숫자인지 여부 리턴
def isNum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# 방법2
def isNum2(s):
    res = True
    for char in s:
        if ord(char) < 48 or ord(char) > 57:
            if char != ".":
                res = False
    return res


eq = "( 12.3 + 6 ) * 3 / 6"
eqList = eq.split(" ")
s = Stack()
postEq = []

for item in eqList:
    if item == '(':
        s.push(item)
    elif item == ')':
        while True:
            _tmp = s.pop()
            # ( ) 짝이 맞을 경우
            if _tmp == '(':
                break
            # )가 존재하지 않는 경우 다시 ( 를 추가해주기
            else:
                postEq.append(_tmp)
    elif item == "+" or item == "-":
        while isOper(s.peek()) == True:
            postEq.append(s.pop())
        s.push(item)
    elif item == "*" or item == "/":
        while s.peek() == "*" or s.peek() == "/":
            postEq.append(s.pop())
        s.push(item)
    elif isNum(item) == True:
        postEq.append(item)
    print(postEq)

while s.isEmpty() == False:
    postEq.append(s.pop())


''' QUEUE '''

import numpy as np
import matplotlib.pyplot as pit

# 지수분포를 통해 나타냄
lamda = 1 # 단위시간당 한명
x = np.linspace(0, 10, 100)  # 0부터 10까지 100등분
# pdf: probability density function (확률밀도함수)
pdf = (1/lamda * np.exp(-x/lamda))
pit.plot(x.pdf)
pit.show()

# x는 한사람이 도착 후, 다음 고객이 도착하는 시간 사이 간격을 의미함
import numpy as np
np.random.seed(seed=1)
x = np.random.exponential(1, 10)
print(x)
# print(np.mean(x), np.std(x))
entTime = np.cumsum(x)    # cumsum - 누적되는 원소들의 누적 합
print(entTime)
