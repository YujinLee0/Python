# 노드들의 정보를 저장할 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 링크드 리스트로 연결해주며 각 기능들을 구현할 클래스
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # tail에 새로운 노드 추가하기
    def append(self,data):

        new_data = Node(data)
        # 리스트에 아무 데이터도 존재하지않으면 그냥 추가만 해주면 됨.
        if self.head is None:
            self.head = new_data
            self.tail = new_data
        # 리스트에 노드가 존재할 경우
        else:
            self.tail.next = new_data
            self.tail = new_data

    # 리스트 프린트
    def __str__(self):
        res_str = "|"
        iterator = self.head

        while iterator is not None:
            # res_str += f" {iterator.data} |"
            iterator = iterator.next
        return res_str

    # 사용자가 입력한 데이터로 노드 찾기
    def findNodeWith(self,data):
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return None

    # 사용자가 입력한 인덱스로 노드 찾기
    def findNodeAt(self, idx):
        iterator = self.head

        if idx == 0:
            return iterator
        elif idx < 0:
            print("올바른 index 값을 입력해주세요.")
        elif idx > 0:
            for _ in range(idx):
                iterator = iterator.next
            return iterator.data

    def insertAfter(self, previousNode, data):
        new_node = Node(data)

        # 가장 끝에 노드를 삽입하는 경우
        if previousNode == self.tail:
            self.tail.next = new_node
            self.tail = new_node

        # 가장 앞에 노드를 삽입하는 경우
        elif previousNode == self.head:
            new_node.next = self.head
            self.head = new_node

        # 중간에 노드를 삽입하는 경우
        else:
            new_node.next = previousNode.next
            previousNode.next = new_node

    def deleteAfter(self, previousNode):
        data = previousNode.next

        # head 노드를 지우려고 하는 경우
        if previousNode is None:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        # tail 노드를 지울 때
        elif previousNode.next == self.tail:
            previousNode.next = None
            self.tail = previousNode
        # 중간 노드를 지울 때
        else:
            previousNode.next = data.next
        # 지워진 노드 리턴
        return data


animal = LinkedList()
animal.append("Rabbit")
animal.append("Tiger")
animal.append("Duck")
animal.append("Elephant")
print(animal)
print(animal.findNodeAt(2))
# animal.insertAfter("Tiger","Snake")
animal.deleteAfter("Duck")