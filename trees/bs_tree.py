from typing import Optional

# Binary Search Tree operations in Python


class Node:
    def __init__(self, key):
        self.key = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def inorder(root: Node):

    if root:
        inorder(root.left)

        print(str(root.key) + "->", end=' ')

        inorder(root.right)


def insert(node: Node, key):

    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)

    if key > node.key:
        node.right = insert(node.right, key)

    return node


def min_value_node(node: Node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def delete_node(root: Node, key):

    if root is None:
        return None

    if key < root.key:
        root.left = delete_node(root.left, key)

    elif key > root.key:
        root.right = delete_node(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)

        root.key = temp.key

        root.right = delete_node(root.right, temp.key)

    return root


root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 10")
root = delete_node(root, 10)
print("Inorder traversal: ", end=' ')
inorder(root)
