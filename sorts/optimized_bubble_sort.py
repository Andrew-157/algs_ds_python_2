

def bubble_sort(array: list) -> None:

    n = len(array)

    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):

            if array[j] > array[j+1]:

                array[j], array[j+1] = array[j+1], array[j]

                swapped = True

        if not swapped:
            break


array = [9, 0, -1, 22, 20, -5]

print(f"Unsorted array: {array}")

bubble_sort(array)

print(f"Sorted array: {array}")
