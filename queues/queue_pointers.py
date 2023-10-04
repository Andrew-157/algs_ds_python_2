# The following is the code how to implement Queue in Python
# using pointers FRONT and REAR

"""
Working Queue:
- two pointers FRONT and REAR
- FRONT tracks the first element of the queue
- REAR tracks the last element of the queue
- initially, set values of FRONT and REAR to -1

Enqueue Operation:
- check if the queue is full
- for the first element, set the value of FRONT to 0
- increase the REAR index by 1
- add the new element in the position pointed to by REAR

Dequeue Operation:
- check if the queue is empty
- return the value pointed to by FRONT
- increase the FRONT index by 1
- for the last element, reset value of FRONT and REAR to -1

"""


class QueueIsFullException(Exception):
    pass


class QueueIsEmptyException(Exception):
    pass


class Queue:
    def __init__(self):
        # Create dictionary where key is index and value is element added to queue
        self.queue: dict = {}
        # Set up two pointers
        self.front: int = -1
        self.rear: int = -1
        # Set the maximum size for the queue
        self.queue_size: int = 5

    def is_full(self):
        # Method to check if queue has reached its max size
        return self.rear == self.queue_size - 1

    def is_empty(self):
        # Method to check if queue is empty
        return self.front == -1

    def show_queue(self):
        # Method to return elements of the queue
        return list(self.queue.values())

    def enqueue(self, element):
        # Check if queue is full
        if self.is_full():
            # if it is, raise custom Exception
            raise QueueIsFullException("Queue is full, cannot enqueue")
        # set FRONT to 0
        self.front = 0
        # increment REAR by 1
        self.rear += 1
        # if it is the first element in the queue, then both REAR and FRONT will
        # be 0
        # Set element in queue to REAR index
        self.queue[self.rear] = element

    def dequeue(self):
        # Check if queue is empty
        if self.is_empty():
            # if it is, raise custom Exception
            raise QueueIsEmptyException("Queue is empty, cannot dequeue")

        # Remove the element to which FRONT points
        to_dequeue = self.queue.pop(self.front)

        # If the element we returned was the only element in the queue
        # reset both REAR and FRONT to -1
        if not self.queue:
            self.front = -1
            self.rear = -1
        else:
            # if not, than increment FRONT by 1
            self.front += 1

        # Return the element that was dequeued
        return to_dequeue

    def peek(self):
        # Check if the queue is empty
        if self.is_empty():
            # Raise the exception if queue is empty
            raise QueueIsEmptyException("Queue is empty, cannot peek it")
        # Just return the element to which FRONT points
        return self.queue[self.front]


queue = Queue()
queue.enqueue(0)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
try:
    queue.enqueue(5)
except QueueIsFullException:
    print('Queue is full')

print(queue.show_queue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

try:
    print(queue.dequeue())
except QueueIsEmptyException:
    print('Queue is empty')
