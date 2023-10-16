# Quicksort implementation in Python

# function to find the partition position
def partition(array: list, low: int, high: int) -> int:

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for the greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than the pivot is found
            # swap it with the greater element pointed by i
            i += 1

            # swapping element at i with element at j
            array[i], array[j] = array[j], array[i]

    # swap the pivot element with the greater element specified by i
    array[i+1], array[high] = array[high], array[i+1]

    # return the position from where partition is done
    return i + 1


# function to perform Quicksort
def quick_sort(array: list, low: int, high: int) -> None:
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quick_sort(array, low, pi-1)

        # recursive call on the right of pivot
        quick_sort(array, pi+1, high)


array = [8, 7, 2, 1, 0, 9, 6]

print(f"Before Quicksort: {array}")

quick_sort(array, 0, len(array)-1)

print(f"After Quicksort: {array}")
