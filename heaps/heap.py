"""
Heap data structure is a complete binary tree that satisfies the heap property, where any given node is

- always greater than its child node/s and the key of the root node is the largest among all other nodes. 
This property is also called max heap property.

MAX heap:

           9
          /  \
         5    4
        / \   /
       1   3  2

- always smaller than the child node/s and the key of the root node is the smallest among all other nodes. 
This property is also called min heap property.

        MIN heap:

           1
          /  \
         2    3
        / \   /
       4   5  9

This type of data structure is also called a binary heap.

Heap operations

Heapify
Heapify is the process of creating a heap data structure from a binary tree. 
It is used to create a Min-Heap or a Max-Heap.

1. Let the input array be:

[ 3 9 2 1 4 5 ]
  0 1 2 3 4 5 

2. Create a complete binary tree from the array:
       
        3
      /   \
     9     2 
    / \   / 
   1   4  5

3. Start from the first index of non-leaf node whose index is given by n/2 - 1

It will be node containing 2(index is 2)

4. Set current element i as largest. 
i is index, i=2 in the current situation.

5. The index of left child is given by 2i+1 and the right child is given by 2i+2.
if leftChild is greater than currentElement(i.e. element at index i), set
leftChildIndex as largest.
if rightChild is greater than element than element in largest, set rightChildIndex as largest.

6.Swap largest with currentElement.
        3
      /   \
     9     5
    / \   /
   1   4  2
7. Repeat steps 3-7 until the subtrees are also heapified.

Algorithm

Heapify(array, size, i)
  set i as largest
  leftChild = 2i + 1
  rightChild = 2i + 2
  
  if leftChild > array[largest]
    set leftChildIndex as largest
  if rightChild > array[largest]
    set rightChildIndex as largest

  swap array[i] and array[largest]

To create a Max-Heap:
MaxHeap(array, size)
  loop from the first index of non-leaf node down to zero
    call heapify

For Min-Heap, both leftChild and rightChild must be larger than the parent for all nodes.

Insert element into Heap.

Algorithm for insertion into Max heap:
If there is no node, 
  create a newNode.
else (a node is already present)
  insert the newNode at the end (last node from left to right.)
  
heapify the array

1. Insert the new element at the end of the tree

        9
      /   \
     4     5
    / \   / \
   1   3  2  7  '7' was inserted

2. Heapify the tree

        9
      /   \
     4     7
    / \   / \
   1   3  2  5

For Min Heap, the above algorithm is modified so that parentNode is always smaller than newNode.


Delete element from Heap

Algorithm for deletion in Max Heap:
If nodeToBeDeleted is the leafNode
  remove the node
Else swap nodeToBeDeleted with the lastLeafNode
  remove nodeToBeDeleted
   
heapify the array

1. Select node to be deleted
        9
      /   \
     3     7
    / \   / \
   1   4  2  5 '3' is to be deleted

2. Swap it with the last element
        9
      /   \
     5     7
    / \   / \
   1   4  2  3  '5' was swapped with '3'

3. Remove the last element
        9
      /   \
     5     7
    / \   / 
   1   4  2    '3' was removed

4. Heapify the tree
        9
      /   \
     5     7
    / \   / 
   1   4  2 

For Min Heap, above algorithm is modified so that both childNodes are greater than currentNode.


Peek(return Max/Min)

Peek operation returns the maximum element from Max Heap or minimum element from Min Heap without deleting the node.

For both Max heap and Min Heap
return rootNode

Extract-Max/Min
Extract-Max returns the node with maximum value 
after removing it from a Max Heap whereas 
Extract-Min returns the node with minimum after removing it from Min Heap.

"""

# Python implementation of the Max-Heap


def heapify(arr: list, n, i: int):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def insert(array: list, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


def deleteNode(array: list, num: int):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size-1] = array[size-1], array[i]
    array.remove(num)

    for i in range((len(array)//2)-1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
