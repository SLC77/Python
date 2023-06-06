
class Node:
    def __init__(self, value):
        self.right = None
        self.left = None        
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                    self.left = Node(value)
            else:
                    self.left.insert(value)
        else:
            if self.right is None:
                     self.right = Node(value)
            else:
                     self.right.insert(value)

    def inorder_traversal(self):
        if self.left:
                self.left.inorder_traversal()
        print(self.value)
        if self.right:
                self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.value)
        if self.left:
              self.left.preorder_traversal()
        if self.right:
              self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
              self.left.preorder_traversal()
        if self.right:
              self.right.preorder_traversal()
        print(self.value)


tree = Node(12)
tree.insert(10)
tree.insert(15)
tree.insert(7)
tree.insert(8)
tree.insert(4)
tree.insert(3)
tree.insert(5)
tree.insert(1)

tree.postorder_traversal()