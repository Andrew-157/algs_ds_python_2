"""
A priority queue is a special type of queue in which each element is associated with a priority value. 
And, elements are served on the basis of their priority. 
That is, higher priority elements are served first.

However, if elements with the same priority occur, they are served according to their order in the queue.

Assigning Priority Value
Generally, the value of the element itself is considered for assigning the priority. For example,

The element with the highest value is considered the highest priority element. 
However, in other cases, we can assume the element with the lowest value as the highest priority element.

We can also set priorities according to our needs.

Difference between Priority Queue and Normal Queue
In a queue, the first-in-first-out rule is implemented whereas, in a priority queue, 
the values are removed on the basis of priority. 
The element with the highest priority is removed first.

Implementation of Priority Queue
Priority queue can be implemented using an array, a linked list, a heap data structure, or a binary search tree. 
Among these data structures, heap data structure provides an efficient implementation of priority queues.

Here Priority Queue will be implemented using Heap.

Operation on Priority Queue:

1. Inserting an Element into the Priority Queue

Inserting an element into a priority queue (max-heap) is done by the following steps.

-Insert the new element at the end of the tree.
-Heapify the tree

Algorithm for insertion of an element into priority queue (max-heap):
If there is no node, 
  create a newNode.
else (a node is already present)
  insert the newNode at the end (last node from left to right.)
  
heapify the array


For Min Heap, the above algorithm is modified so that parentNode is always smaller than newNode.

2. Deleting an Element from the Priority Queue

- Select the element to be deleted.

- Swap it with the last element

- Remove the last element

- Heapify the tree


Algorithm for deletion of an element in the priority queue (max-heap):
If nodeToBeDeleted is the leafNode
  remove the node
Else swap nodeToBeDeleted with the lastLeafNode
  remove noteToBeDeleted
   
heapify the array

For Min Heap, the above algorithm is modified so that the both childNodes are smaller than currentNode.
"""
