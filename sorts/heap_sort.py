
counter = 0

# Heap Sort implementation in Python


def heapify(array: list, n: int, i: int) -> None:
    # Find the largest among root and its children
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    global counter
    counter += 1

    if left < n and array[left] > array[largest]:
        largest = left

    if right < n and array[right] > array[largest]:
        largest = right

    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def heap_sort(array: list) -> None:
    n = len(array)

    # Build Max-Heap
    for i in range(n//2 - 1, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        # Swap
        array[i], array[0] = array[0], array[i]

        # Heapify Root Element
        heapify(array, i, 0)


array = [1, 12, 9, 5, 6, 10]
print(array)
heap_sort(array)
print(array)
