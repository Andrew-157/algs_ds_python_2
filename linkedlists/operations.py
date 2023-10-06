

class NodeNotInTheList(Exception):
    pass


class IndexOutOfRangeOfTheLinkedList(Exception):
    pass


class Node:
    def __init__(self, item):
        self.item = item
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = Node

    def insert_beginning(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, item):
        if not self.head:
            return None
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = Node(item)

    def insert_after(self, prev: Node, item):
        in_list = False
        temp = self.head
        while temp:
            if temp == prev:
                in_list = True
            temp = temp.next
        if not in_list:
            raise NodeNotInTheList
        new_node = Node(item)
        new_node.next = prev.next
        prev.next = new_node

    def insert_at_index(self, index, item):
        # Assuming head has index of zero
        # New node is inserted at the index
        # if this index is not out of range of the list
        if index == 0:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
            return None

        index_in_llist = -1

        temp = self.head
        while temp.next:
            index_in_llist += 1
            if index_in_llist == index - 1:
                break
            temp = temp.next
        if index_in_llist != index - 1:
            raise IndexOutOfRangeOfTheLinkedList

        new_node = Node(item)
        new_node.next = temp.next
        temp.next = new_node

    def delete_beginning(self):
        if not self.head:
            return None
        self.head = self.head.next

    def delete_end(self):
        if self.head == None:
            return None
        if self.head.next == None:

            self.head = None
            return None
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def delete_at_index(self, index):

        if self.head is None:
            return None

        temp = self.head

        if index == 0:
            self.head = temp.next
            return None

        for i in range(index-1):
            temp = temp.next
            if temp is None:
                break

        if temp is None:
            return None

        if temp.next is None:
            return None

        next = temp.next.next
        temp.next = None
        temp.next = next

    def find_length(self):
        length = 0

        temp = self.head
        while temp:
            length += 1
            temp = temp.next

        return length

    def search(self, item):
        temp = self.head
        while temp:
            if temp.item == item:
                return True
            temp = temp.next

        return False

    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev

    def traverse(self):
        temp = self.head
        if not temp:
            print('HEAD -> NULL')
            return None
        print('HEAD', end=" -> ")
        while temp:
            if not temp.next:
                print(temp.item, end=" -> NULL\n")
            else:
                print(temp.item, end=" -> ")
            temp = temp.next


llist = LinkedList()
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)

llist.head = node_1
node_1.next = node_2
node_2.next = node_3

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

llist.traverse()

llist.insert_after(node_2, 9)

llist.traverse()

try:
    llist.insert_after(node_3, 8)
except NodeNotInTheList:
    print("Node is not in the list.")


try:
    llist.insert_at_index(3, 9)
except IndexOutOfRangeOfTheLinkedList:
    print('Index is out of range of the linked list')

llist.insert_at_index(0, 2)

llist.traverse()

llist.delete_at_index(2)

llist.traverse()

print(llist.find_length())

print(llist.search(9))
print(llist.search(14))
llist.reverse()
llist.traverse()
