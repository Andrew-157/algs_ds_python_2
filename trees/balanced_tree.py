from typing import Optional

# Checking if binary tree is height balanced in Python


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class Height:
    def __init__(self):
        self.height = 0


def is_height_balanced(root: Node, height):

    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l = is_height_balanced(root.left, left_height)
    r = is_height_balanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False


height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if is_height_balanced(root, height):
    print('The tree is balanced')
else:
    print('The tree is not balanced')
