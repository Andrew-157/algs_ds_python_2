# Python implementation of selection sort


def selection_sort(array: list) -> None:
    size = len(array)

    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            if array[i] < array[min_idx]:
                min_idx = i

        array[step], array[min_idx] = array[min_idx], array[step]


array = [9, 0, -1, 22, 20, -5]

print(array)

selection_sort(array)

print(array)
