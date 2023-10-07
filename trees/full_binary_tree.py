"""
A full Binary tree is a special type of binary tree in which every parent node/internal 
node has either two or no children.

It is also known as a proper binary tree.

Full Binary Tree Theorems:

Let, 
    i = the number of internal nodes
    n = be the total number of nodes
    l = number of leaves
    λ = number of levels

1.The number of leaves is i + 1.
2.The total number of nodes is 2i + 1.
3.The number of internal nodes is (n - 1) / 2.
4.The number of leaves is (n + 1) / 2.
5.The total number of nodes 2l - 1.
6.The number of internal nodes is l - 1.
7.The number of leaves is at most 2 to the power of (λ - 1).
"""
from typing import Optional
# Checking if a binary tree is a full binary tree in Python

# Creating a Node


class Node:
    def __init__(self, item):
        self.item = item
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def is_full_tree(root: Node):

    if not root:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return is_full_tree(root.left) and is_full_tree(root.right)

    return False


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.left.right.left = Node(6)
root.left.right.right = Node(7)


if is_full_tree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")
