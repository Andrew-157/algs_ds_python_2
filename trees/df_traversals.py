from typing import Optional

# Depth-First traversals

"""
Inorder Traversal:

1.Traverse Left Subtree
2.Traverse Root
3.Traverse Right Subtree

"""


class Node:
    def __init__(self, item):
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.val = item


def inorder(root: Node):
    """
    Inorder Traversal:

    1.Visit Left Subtree
    2.Visit Root
    3.Visit Right Subtree
    """

    if root:
        inorder(root.left)
        print(str(root.val) + " ", end="")
        inorder(root.right)


def preorder(root: Node):
    """
    Preorder Traversal:

    1.Visit Root
    2.Visit Left Subtree
    3.Visit Right Subtree
    """

    if root:
        print(str(root.val) + " ", end="")
        preorder(root.left)
        preorder(root.right)


def postorder(root: Node):
    """
    Postorder Traversal:

    1.Visit Left Subtree
    2.Visit Right Subtree
    3.Visit Root
    """

    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + " ", end="")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal: ")
inorder(root)  # 4 2 5 1 3

print()

print("Preorder traversal: ")
preorder(root)  # 1 2 4 5 3


print()

print("Postorder traversal: ")
postorder(root)  # 4 5 2 3 1
