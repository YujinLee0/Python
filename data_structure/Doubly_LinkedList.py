class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # 접근 메소드
    def find_node_at(self,index):
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator

    # 탐색 메소드
    def find_node_with_data(self,data):
        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return None

    # STR 메소드
    def __str__(self):
        res_str = "|"
        iterator = self.head
        while iterator is not None:
            # str 방식 기억해두기
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next
        return res_str

    ## 위의 접근, 탐색, STR 메소드는 single linked list와 동일한 코드임

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
        new_node = Node(data)

        # tail 노드 뒤에 추가하는 경우
        if previous_node == self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        # 중간에 추가하는 경우
        else:
            new_node.next = previous_node.next
            new_node.prev = previous_node
            # 주의할점!! previous_node.next를 new_node로 바꾸기 전에 next의 prev를 할당해줘야 함 (순서에 주의)
            previous_node.next.prev = new_node
            previous_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is not None:
            # 이것도 순서에 주의할 것 (순서가 안맞으면 중간에 써야하는 데이터를 표현할 방법이 없어짐)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def delete(self, node_to_delete):

        # 리스트에 node_to_delete만 존재하는 경우
        if node_to_delete == self.head and node_to_delete == self.tail:
            self.head = None
            self.tail = None
        # head 노드를 삭제하는 경우
        elif node_to_delete == self.head:
            self.head = self.head.next
            self.head.prev = None
        # tail 노드를 삭제하는 경우
        elif node_to_delete == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        # 중간에 있는 노드를 삭제하는 경우
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        # 삭제하는 데이터의 값을 반환한다.
        return node_to_delete.data


myList = LinkedList()
myList.append(2)
myList.append(3)
myList.append(5)
myList.append(7)
myList.append(9)
print(myList)

