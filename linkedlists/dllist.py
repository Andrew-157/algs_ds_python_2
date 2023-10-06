from typing import Optional


class Node:
    def __init__(self, item):
        self.prev: Optional[Node] = None
        self.item = item
        self.next: Optional[Node] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def insert_beginning(self, item):
        if not self.head:
            self.head = Node(item)
            return None
        new_node = Node(item)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_end(self, item):
        new_node = Node(item)

        if not self.head:
            self.head = new_node
            return None

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def delete_beginning(self):
        if not self.head:
            return None

        if not self.head.next:
            self.head = None
            return None

        self.head.next.prev = None
        self.head = self.head.next

    def delete_end(self):
        if not self.head:
            return None

        temp = self.head

        if not temp.next:
            self.head = None
            return None

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def traverse(self):
        print('Doubly-linked list: ', end="")
        temp = self.head
        while temp:
            print(temp.item, end=" ")
            temp = temp.next
        print()


llist = LinkedList()
llist.head = Node(item=1)
node_2 = Node(item=2)
node_3 = Node(item=3)

llist.head.next = node_2
node_2.next = node_3

node_2.prev = llist.head
node_3.prev = node_2

llist.traverse()

llist.insert_beginning(0)

llist.traverse()

llist.insert_end(4)

llist.traverse()


llist.delete_beginning()

llist.traverse()

llist.delete_end()

llist.traverse()

llist.delete_end()
llist.delete_end()

llist.traverse()
