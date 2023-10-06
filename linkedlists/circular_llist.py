from typing import Optional


class Node:
    def __init__(self, item):
        self.item = item
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.last: Optional[Node] = None

    def add_empty(self, item):

        if self.last != None:
            return self.last

        new_node = Node(item)

        self.last = new_node
        new_node.next = new_node
        return self.last

    def add_front(self, item):

        if not self.last:
            return self.add_empty(item)

        new_node = Node(item)

        new_node.next = self.last.next

        self.last.next = new_node

        return self.last

    def add_end(self, item):
        if self.last == None:
            return self.add_empty(item)

        new_node = Node(item)

        new_node.next = self.last.next

        self.last = new_node

        return self.last
