class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_inorder(self, node):
        if node is not None:
            self.print_inorder(node.left_child)
            print(node.data)
            self.print_inorder(node.right_child)

bst = BinarySearchTree()