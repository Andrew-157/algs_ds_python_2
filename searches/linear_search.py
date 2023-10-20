
# Linear Search implementation in Python


def linear_search(array: list, x: int) -> int:

    n = len(array)

    for i in range(0, n):
        if array[i] == x:
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 9
found_index = linear_search(array, x)
if found_index == -1:
    print("Element was not found in the array")
else:
    print(f'Index of element x={x} is: {found_index}')
