# Implementation of Insertion Sort in Python


def insertion_sort(arr: list) -> None:

    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1

        array[j+1] = key


array = [9, 5, 1, 4, 3]

print(f"Unsorted array: {array}")

insertion_sort(arr=array)

print(f"Sorted array: {array}")
