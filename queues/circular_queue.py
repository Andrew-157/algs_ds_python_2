"""
A circular queue is the extended version of a regular queue where the last element is 
connected to the first element. Thus forming a circle-like structure.

The circular queue solves the major limitation of the normal queue. 
In a normal queue, after a bit of insertion and deletion, there will be non-usable empty space.

Normal queue after some dequeueing:
      FRONT  REAR    
       |     | 
-1 0 1 2 3 4 5
_  ____________

       2 3 4 5 
_  ____________

Here, indexes 0 and 1 can only be used after resetting the queue (deletion of all elements). 
This reduces the actual size of the queue.

How Circular Queue Works

Circular Queue works by the process of circular increment i.e. 
when we try to increment the pointer and we reach the end of the queue, 
we start from the beginning of the queue.

Here, the circular increment is performed by modulo division with the queue size. That is,
if REAR + 1 == 6 (overflow!), REAR = (REAR + 1) % 6 == 0 (start of queue)

Circular Queue Operations:
- two pointers FRONT and REAR
- FRONT track the first element of the queue
- REAR track the last element of the queue
- initially, set value of FRONT and REAR to -1

Enqueue operation:
- check if the queue is full
- for the first element, set value of FRONT to 0
- circularly increase the REAR index by 1 
(i.e. if the rear reaches the end, next it would be at the start of the queue)
- add the new element in the position pointed to by REAR

Dequeue operation:
- check if the queue is empty
- return the value pointed by FRONT
- circularly increase the FRONT index by 1
- for the last element, reset the values of FRONT and REAR to -1

However, the check for full queue has a new additional case:

Case 1: FRONT = 0 && REAR == SIZE - 1
Case 2: FRONT = REAR + 1

The second case happens when REAR starts from 0 due to circular 
increment and when its value is just 1 less than FRONT, the queue is full.
"""

# Circular Queue implementation in Python


class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def enqueue(self, data):
        # Insert an element into the circular queue
        if (self.rear + 1) % self.k == self.front:
            print('Queue is full')

        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = data

    def dequeue(self):

        if self.front == -1:
            print('Queue is empty')

        elif self.rear == self.front:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.k
            return temp

    def printCQueue(self):
        if self.front == -1:
            print('Queue is empty')

        elif self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=' ')
            print()
        else:
            for i in range(self.front, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


# Your MyCircularQueue object will be instantiated and called as such:
obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()


"""
Circular Queue Complexity Analysis
The complexity of the enqueue and dequeue operations of a circular queue is O(1) for (array implementations).
"""
