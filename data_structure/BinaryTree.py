''' 이진 트리 노드 클래스 '''
class Node:
    ''' 데이터와 두 자식 노드에 대한 레퍼런스를 갖는다. '''
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

rootNode = Node(2)
nodeB = Node(3)
nodeC = Node(5)
nodeD = Node(7)
nodeE = Node(11)

# B와 C를 루트 노드의 자식으로 지정
rootNode.leftChild = nodeB
rootNode.rightChild = nodeC
# D와 E를 B의 자식으로 지정
nodeB.leftChild = nodeD
nodeB.rightChild = nodeE

testNode = rootNode.rightChild
print(testNode.data)


''' 완전 이진 트리 리스트로 구현하기 '''
# 완전 이진 트리는 마지막 레벨을 제외한 모든 레벨에서 노드들이 꽉 차있고 마지막 레벨에서는 노드들이 왼쪽에서 오른쪽으로 차있는 것이 특징이기에
# 하단의 코드 구현이 가능함. * 자식노드찾기 = 부모인덱스 * 2 / 부모노드 찾기 = 자식인덱스 / 2



''' index번째 노드의 부모노드의 인덱스 리턴 '''
def get_parent_index(complete_binary_tree, index):
    parent_index = index // 2

    # 부모 노드가 있으면 인덱스를 리턴한다.
    if 0 < parent_index < len(complete_binary_tree):
        return parent_index
    return None


''' index번째 노드의 왼쪽자식 노드의 인덱스 리턴 '''
def get_left_child_index(complete_binary_tree, index):
    left_child_index = 2 * index

    # 왼쪽 자식 노드가 있으면 인덱스 리턴한다.
    if 0 < left_child_index < len(complete_binary_tree):
        return left_child_index

    return None

''' index번째 노드의 오른쪽 자식 노드의 인덱스 리탄 '''
def get_right_child_index(complete_binary_tree, index):

    right_child_index = 2 * index + 1

    # 오른쪽 자식 노드가 있으면 인덱스를 리턴한다
    if 0 < right_child_index < len(complete_binary_tree):
        return right_child_index

    return None

# 실행 코드
root_node_index = 1 # root 노드

tree = [None, 1, 5, 12, 11, 9, 10, 14, 2, 10]  # 과제 이미지에 있는 완전 이진 트리

# root 노드의 왼쪽과 오른쪽 자식 노드의 인덱스를 받아온다
left_child_index = get_left_child_index(tree, root_node_index)
right_child_index = get_right_child_index(tree,root_node_index)

print(tree[left_child_index])
print(tree[right_child_index])

# 9번째 노드의 부모 노드의 인덱스를 받아온다
parent_index = get_parent_index(tree, 9)

print(tree[parent_index])

# 부모나 자식 노드들이 없는 경우들
parent_index = get_parent_index(tree, 1)  # root 노드의 부모 노드의 인덱스를 받아온다
print(parent_index)

left_child_index = get_left_child_index(tree, 6)  # 6번째 노드의 왼쪽 자식 노드의 인덱스를 받아온다
print(left_child_index)

right_child_index = get_right_child_index(tree, 8)  # 8번째 노드의 오른쪽 자식 노드의 인덱스를 받아온다
print(right_child_index)

''' in-order 순회 구현하기 '''
# 왼쪽 부분 트리 순회 -> 현재 노드의 데이터 출력 -> 오른쪽 부분 트리 순회

def traverse_inorder(node):

    if node is not None: # 왼쪽 or 오른쪽 자식 노드가 없으면 == None 이면 순회를 멈춤
        traverse_inorder(node.left_child)
        print(node.data)
        traverse_inorder(node.right_child)

# 여러 노드 인스턴스 생성
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 생성한 노드 인스턴스들 연결
node_F.left_child = node_B
node_F.right_child = node_G

node_B.left_child = node_A
node_B.right_child = node_D

node_D.left_child = node_C
node_D.right_child = node_E

node_G.right_child = node_I

node_I.left_child = node_H

# 노드 F를 root 노드로 만든다
root_node = node_F

# 만들어 놓은 트리를 in-order 순회한다
traverse_inorder(root_node)

''' pre-order 구현하기 '''
def traverse_preorder(node):
    if node is not None:
        print(node.data)  # 데이터 출력
        traverse_preorder(node.left_child)  # 재귀적으로 왼쪽 부분 트리 순회
        traverse_preorder(node.right_child)  # 재귀적으로 오른쪽 부분 트리 순회

''' post-order 순회 구현하'''
def traverse_postorder(node):
    if node is not None:
        traverse_postorder(node.left_child)  # 재귀적으로 왼쪽 부분 트리 순회
        traverse_postorder(node.right_child)  # 재귀적으로 오른쪽 부분 트리 순회
        print(node.data)  # 데이터 출력