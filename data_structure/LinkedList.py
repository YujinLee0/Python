class Node:
    #링크드 리스트의 노드 클래스 정의
    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스

# 데이터 2,3,5,7,11 을 담는 노드를 생성
head_node = Node(2) # 가장 먼저 오는 노드
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11) # 가장 끝에 오는 노드

# 노드들을 연결하기
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드 순서대로 출력
iterator = head_node

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next


# 링크드 리스트 클래스 추가 연산하기
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:  # LinkedList가 비어있는 경우
            self.head = new_node
            self.tail = new_node

        else:  # LinkedList가 비어있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node

    # 링크드 리스트를 문자열로 표현해서 리턴하는 메소드
    def __str__(self):  # __str__ 메소드는 자동으로 해당 내용을 사람들이 이해할 수 있는 문자열로 리턴해주는 메소드
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            # res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

    # Linked List 접근 연산 메소드 (파라미터 인덱스는 항상 있다고 가정)
    def find_node_at(self, index):
        iterator = self.head

        # for문에서 _를 사용하는 것은 i와 같은 변수 지정 필요 없을 때 (값을 무시하는 경우)
        for _ in range(index):
            iterator = iterator.next
        return iterator

    # 위의 방식은 어떻게 링크드 리스트 메소드가 돌아가는지를 코드로 표기한 것이고 아래의 방식은 실제 찾기위해 쓰는 코드

    # Linked List 탐색 연산 메소드
    def find_node_with_data(self, data):
        iterator = self.head # head 노드에서부터 돌아가므로 iterator를 head 노드로 지정
        while iterator is not None:  # 리스트의 끝까지 다 돌때까지
            if iterator.data == data: # 내가 찾고있는 데이터가 맞을 경우
                return iterator
            iterator = iterator.next # (else가 생략됨) - 해당 데이터가 아닌경우 다음 iterator로 넘어감
        # 링크드 리스트 안에 원하는 데이터 없을 경우
        return None

    # 링크드 리스트 주어진 노드 뒤 삽입 연산 메소드
    def insert_after(self, previous_node, data):
        new_node = Node(data)

        # 가장 마지막 순서 삽입하는 경우
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        # 두 노드 사이에 삽입하는 경우
        else:
            new_node.next = previous_node.next # 기존 previous노드 다음에 오는 노드를 new 노드의 next에 설정해줌으로써 가운데에 넣기
            previous_node.next = new_node

    # 링크드 리스트의 가장 앞에 데이터 삽입(insert_after 함수의 경우 링크드 리스트 맨 앞에는 노드추가를 하지 못하기에 이를 보완)
    def prepend(self, data):
        newNode = Node(data)

        # 링크드 리스트가 비어있을 경우
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        # 링크드 리스트가 비어있지 않는 경우
        else:
            newNode.next = self.head
            self.head = newNode

    # 링크드 리스트 주어진 이전노드 다음의 노드 삭제하기
    def delete_after(self, previous_node):
        data = previous_node.next.data
        # 지우려는 노드가 tail노드일 때
        if previous_node.next is self.tail:
            previous_node.next = None  # next 지정을 안해줌으로써 삭제된것과 같은 효과
            self.tail = previous_node
        # 두 사이 노드를 지울 때
        else:
            previous_node.next = previous_node.next.next
        # 지워진 노드 리턴
        return data

    # 링크드 리스트의 가장 앞 노드 삭제 메소드
    def pop_left(self):
        data = self.head.data # 지워지는 데이터

        # 해당 노드가 삭제되었을 때 리스트가 비게되는 경우
        if self.head is self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next

        return data

# 데이터 2를 갖는 노드 탐색
node_with_2 = LinkedList.find_node_with_data(2)

if not node_with_2 is None:
    print(node_with_2.data)
else:
    print("2를 갖는 노드는 없습니다")

# 데이터 11을 갖는 노드 탐색
node_with_11 = LinkedList.find_node_with_data(11)

if not node_with_11 is None:
    print(node_with_11.data)
else:
    print("11를 갖는 노드는 없습니다")

# 데이터 6 갖는 노드 탐색
node_with_6 = LinkedList.find_node_with_data(6)

if not node_with_6 is None:
    print(node_with_6.data)
else:
    print("6을 갖는 노드는 없습니다")


# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(1)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(9)

# 노드 순서대로 출력하기
iterator = my_list.head

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next

# 새로운 링크드 리스트 생성 (str메소드)
linked_list = LinkedList()

# 링크드 리스트에 데이터 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

print(linked_list)

# 주어진 노드 뒤 삽입 연산 메소드
node_2 = my_list.find_node_at(2)
my_list.insert_after(node_2, 6)

print(my_list)