"""
A perfect binary tree is a type of binary tree in which every 
internal node has exactly two child nodes and all the leaf nodes are at the same level.

            1
          /   \
         2     3
       /  \   / \
      4   5  6   7

All the internal nodes have a degree of 2.

Recursively, a perfect binary tree can be defined as:

1.If a single node has no children, it is a perfect binary tree of height h = 0.
2.If a node has h > 0, it is a perfect binary tree if both of
 its subtrees are of height h - 1 and are non-overlapping.

 tree - 1   tree - 2   tree - 3

    1          1            1
             /   \         / \
            2     3       2   3
                         / \ / \
                        4  5 6  7 

"""

from typing import Optional

# Checking if a binary tree is a perfect binary tree in Python


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def calculate_height(node: Node) -> int:
    height = 0

    while node:
        height += 1
        node = node.left

    return height


def is_perfect(node: Node, node_height, level=0):

    if node is None:
        return True

    if node.left is None and node.right is None:
        return node_height == level + 1

    if node.left is None or node.right is None:
        return False

    return is_perfect(node.left, node_height, level + 1) \
        and is_perfect(node.right, node_height, level + 1)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

if (is_perfect(root, calculate_height(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
