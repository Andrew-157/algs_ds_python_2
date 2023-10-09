from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def inorder(root: Optional[Node]):

    if root is not None:
        inorder(root.left)

        print(root.data, end=" ")

        inorder(root.right)


def insert(root: Node, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)

    elif data > root.data:
        root.right = insert(root.right, data)

    return root


def find_successor(node: Optional[Node]):
    current = node

    while current.left is not None:
        current = current.left

    return current


def delete_node(root: Node, key):

    # If the tree is empty
    if root is None:
        return None

    # Find the node to be deleted
    if key < root.data:
        root.left = delete_node(root.left, key)

    elif key > root.data:
        root.right = delete_node(root.right, key)

    else:
        # If the node is with only one child or no children
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = find_successor(root.right)

        root.data = temp.data

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.data)

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
