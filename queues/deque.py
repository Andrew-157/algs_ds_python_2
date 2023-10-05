"""
Deque or Double Ended Queue is a type of queue in which insertion and removal
of elements can either be performed from the front or the rear. Thus, it does not follow FIFO rule 
(First In First Out).

Types of Deque:
- Input Restricted Deque
In this deque, input is restricted at a single end but allows deletion at both the ends.

- Output Restricted Deque
In this deque, output is restricted at a single end but allows insertion at both the ends.

Operations on a Deque

Below is the circular array implementation of deque. In a circular array, if the array is full, 
we start from the beginning.

But in a linear array implementation, if the array is full, no more elements can be inserted. 
In each of the operations below, if the array is full, "overflow message" is thrown.

Before performing the following operations, these steps are followed.

1. Take array(deque) of size n.
2. Set 2 pointers at teh first position and set front = -1 and rear = 0.

 0   1   2   3   4
___ ___ ___ ___ ___
___ ___ ___ ___ ___

 |
 front=-1
 rear=0

1. Insert at the front

This operation adds new element at the front.

1.Check the position of front

 0   1   2   3   4
___ ___ ___ ___ ___
 7   3   1 
___ ___ ___ ___ ___

 |       |
 front   rear

2. If front < 1, reinitialize front = n - 1 (last index).

 0   1   2   3   4
___ ___ ___ ___ ___
 7   3   1 
___ ___ ___ ___ ___

         |       |
        rear     front

3. Else, decrease front by 1.
4. Add new key 5 into array[front].

 0   1   2   3   4
___ ___ ___ ___ ___
 7   3   1       5
___ ___ ___ ___ ___
         
         |       |
        rear     front

2. Insert at the rear

This operation adds an element to the rear.

1. Check if the array is full.
2. If the deque is full, reinitialize rear = 0
3. Else, increase rear by 1

0   1   2   3   4
___ ___ ___ ___ ___
 7   3   1 
___ ___ ___ ___ ___

 |           |
 front      rear

4. Insert the new key 5 into array[rear] 

0   1   2   3   4
___ ___ ___ ___ ___
 7   3   1   5
___ ___ ___ ___ ___

 |           |
 front      rear

3.Delete from the Front 

The operation deletes an element from the front.

1. Check if the deque is empty.
2. If the deque is empty (i.e. front = -1), deletion cannot be performed (underflow condition).
3. If the deque has only one element (i.e. front = rear), set front = -1 and rear = -1.
4. Else if front is at the end (i.e. front = n - 1), set go to the front front = 0.
5. Else, front = front + 1.

0   1   2   3   4
___ ___ ___ ___ ___
    3   1   
___ ___ ___ ___ ___

     |   |       
  front  rear 

4. Delete from the Rear

This operation deletes an element from the rear.

1. Check if the deque is empty.
2. If the deque is empty (i.e. front = -1), deletion cannot be performed (underflow condition).
3. If the deque has only one element (i.e. front = rear), set front = -1 and rear = -1, 
else follow the steps below.
4. If rear is at the front (i.e. rear = 0), set go to the front rear = n - 1.
5. Else, rear = rear - 1.

0   1   2   3   4
___ ___ ___ ___ ___
 7   3      
___ ___ ___ ___ ___

 |   |       
front rear 

5. Check Empty

This operation checks if the deque is empty. If front = -1, the deque is empty.

6. Check Full 

This operation checks if the deque is full. 
If front = 0 and rear = n - 1 OR front = rear + 1, the deque is full.
"""

# Deque implementation in Python


class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)

    def removeRear(self):
        return self.items.pop()

    def removeFront(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
print(d.isEmpty())
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)
print(d.size())
print(d.isEmpty())
d.addRear(11)
print(d.removeRear())
print(d.removeFront())
d.addFront(55)
d.addRear(45)
print(d.items)
