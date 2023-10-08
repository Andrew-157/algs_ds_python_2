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
    def __init__(self, item):
        self.item = item
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def calculate_depth(node: Node):
    # Calculate the depth
    d = 0
    while node is not None:
        d += 1
        node = node.left
    return d


def is_perfect(root: Node, d, level=0):
    # Check if the tree is the perfect binary tree

    if root is None:
        # Check if the tree is empty
        return True

    # Check the presence of trees
    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False

    return (is_perfect(root.left, d, level + 1) and
            is_perfect(root.right, d, level + 1))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


if (is_perfect(root, calculate_depth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")
