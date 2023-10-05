

class Node:
    def __init__(self, item):
        self.item = item
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None


llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)

second.next = third

llist.head.next = second


curr = llist.head
print('HEAD', end=" -> ")
while curr:
    if not curr.next:
        print(curr.item, end=" -> NULL")
    else:
        print(curr.item, end=" -> ")
    curr = curr.next
