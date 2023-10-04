# Queue implementation using array


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()


"""
Complexity Analysis
The complexity of enqueue and dequeue operations in a queue using an array is O(1). 
If you use pop(N) in python code, 
then the complexity might be O(n) depending on the position of the item to be popped.
"""
