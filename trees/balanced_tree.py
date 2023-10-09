from typing import Optional

# Checking if binary tree is height balanced in Python

from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def get_height(root: Optional[Node]):

    if root is None:
        return 0

    return 1 + max(get_height(root.left), get_height(root.right))


def is_balanced(root: Optional[Node]):

    if root is None:
        return True

    return is_balanced(root.left)\
        and is_balanced(root.right)\
        and abs(get_height(root.left) - get_height(root.right)) <= 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.left.left = Node(10)

if is_balanced(root):
    print("The tree is balanced")
else:
    print("The tree is not balanced")
