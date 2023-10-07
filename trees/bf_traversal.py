from typing import Optional
# Breadth-First or Level Order Traversal

"""
For each node, first, the node is visited and then its child nodes are put in a FIFO queue. 
Below is the algorithm for the same:

    - Create an empty queue q
    - temp_node = root /*start from root*/
    - Loop while temp_node is not NULL:
        - print temp_node->data.
        - Enqueue temp_node's children (first left then right children) to q
        - Dequeue a node from q
"""


class Node:
    def __init__(self, key):
        self.data = key
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


def breadth_first(root: Node):

    if root is None:
        return None

    queue: list[Node] = []

    queue.append(root)

    while len(queue) > 0:

        print(queue[0].data, end=" ")
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal: ")
breadth_first(root)
