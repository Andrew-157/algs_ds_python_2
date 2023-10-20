
# Shell Sort implementation in Python

def shell_sort(array: list) -> None:

    gap = len(array) // 2  # initialize the gap

    while gap > 0:

        i = 0
        j = gap

        # check the array in from left to right
        # till the last possible index
        while j < len(array):

            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

            i += 1
            j += 1

            # now, we look back from the ith index to the left
            # we swap the values which are not in the right order.
            k = i
            while k - gap > -1:

                if array[k - gap] > array[k]:
                    array[k], array[k-gap] = array[k - gap], array[k]
                k -= 1

        gap //= 2


array = [12, 34, 54, 2, 3]

print(array)

shell_sort(array)

print(array)
