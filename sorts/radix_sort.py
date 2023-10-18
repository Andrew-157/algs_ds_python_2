# Radix Sort algorithm in Python


def counting_sort(array: list, exp1):
    # Performs counting sort on an array
    # according to the digit represented by exp
    n = len(array)

    output_array = [0] * n

    count_array = [0] * 10

    for i in range(0, n):
        index = array[i] // exp1
        count_array[index % 10] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    i = n - 1

    while i >= 0:
        index = array[i] // exp1
        output_array[count_array[index % 10] - 1] = array[i]
        count_array[index % 10] -= 1
        i -= 1

    for i in range(0, len(array)):
        array[i] = output_array[i]


def radix_sort(array: list):

    max1 = max(array)

    exp = 1
    while max1 / exp >= 1:
        counting_sort(array, exp)
        exp *= 10


array = [170, 45, 75, 90, 802, 24, 2, 66]


radix_sort(array)


print(array)
