
# Bubble Sort Implementation in Python

def bubble_sort(array: list) -> None:
    n = len(array)

    # loop to access each array element
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


data = [-2, 45, 0, 11, -9]

print(f"Unsorted array: {data}")

bubble_sort(array=data)

print(f"Sorted array: {data}")
