
class BinaryTree:

    def __init__(self):
        self.t = [None]  # [None] => None이 원소로 들어가있는 리스트

    def append(self, item):
        self.t.append(item)

    def size(self):
        return len(self.t) - 1 # - 1 을 하는 이유는 인덱스0에 노드가 아닌 None이 위치하기 떄문

    ''' 자식 노드를 찾는 메소드 '''
    def getChild(self, item):
        # item이 해당 리스트에 있는 경우
        if item in self.t:
            k = self.t.index(item) # 부모노드의 인덱스 저장
            lidx = 2 * k
            ridx = 2 * k + 1
            # list 범위 내에 자식노드가 있는지 확인 ( 부모노드에 대해 자식이 없는 경우도 있으므로 해당 경우에 대해 None을 반한해줘야함)
            if lidx <= self.size():
                lnode = self.t[lidx]
            else:
                lnode = None
            if ridx <= self.size():
                rnode = self.t[ridx]
            else:
                rnode = None
            return lnode, rnode
        else:
            print('Item is not founded.')

    ''' 부모 노드 찾기 메소드 '''
    def getParent(self, item):
        if item in self.t:
            k = self.t.index(item)
            pidx = k // 2
            if pidx > 0:  # 부모노드 찾기는 아래에서 위로 번호가 올라가는 것이기에 len에 대한 범위지정을 하지 않아도 됨.
                return self.t[pidx]
            else:
                return None
        else:
            print('Item is not founded.')

tree = BinaryTree()
for i in range(12):
    tree.append(chr(65+i))
print(tree.t)
print(tree.getChild('C'))
print(tree.getChild('E'))
print(tree.getParent('G'))
print(tree.getParent('N'))