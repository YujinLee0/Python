class DNode:
    def __init__(self, item=None, rlink=None, llink=None):
        self.item = item
        self.llink = llink
        self.rlink = rlink

class DLinkedList:
    def __init__(self):
        self.root = DNode()
        self.current = self.root

    def append(self, item):
        newNode = DNode(item)
        if self.root.item == None:
            self.root = newNode
        else:
            curNode = self.root
            while curNode.rlink is not None:
                curNode = curNode.rlink
            curNode.rlink = newNode
            newNode.llink = curNode

    def print(self):
        curNode = self.root
        print(curNode.item, end="|")
        while curNode.rlink is not None:
            curNode = curNode.rlink
            print(curNode.item, end="|")

    def setCurrent(self, item):
        curNode = self.root
        if curNode.item == item:
            self.current = curNode
            print("현재 위치는",self.current.item,"입니다.")
        else:
            while curNode.rlink is not None:
                curNode = curNode.rlink
                if curNode.item == item:
                    self.current = curNode
                    print("현재 위치는", self.current.item, "입니다.")

    def moveLeft(self):
        if self.current == self.root:
            print("맨 처음입니다.")
        else:
            self.current = self.current.llink
            print("현재 위치는", self.current.item, "입니다.")

    def moveRight(self):
        if self.current.rlink is None:
            print("마지입니다.")
        else:
            self.current = self.current.rlink
            print("현재 위치는", self.current.item, "입니다.")


a = DLinkedList()
a.append("Apple")
a.append("Pear")
a.append("Grape")

a.print()
a.setCurrent("Pear")
a.moveLeft()
a.moveRight()


