
# Counting Sort implementation in Python


def counting_sort(input_array: list) -> list:
    # FInd the maximum element of the input array
    M = max(input_array)

    # Initialize the count_array
    count_array = [0] * (M + 1)

    # Mapping each element of input array as an index of the count array
    for num in input_array:
        count_array[num] += 1

    # Calculating the prefix sum(cumulative sum) at every index of count_array
    for i in range(1, M + 1):
        count_array[i] += count_array[i-1]

    # Creating output_array
    output_array = [0] * len(input_array)

    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1

    return output_array


array = [4, 3, 12, 1, 5, 5, 3, 9]
print(f"Array before Counting Sort: {array}")
array = counting_sort(input_array=array)
print(f"Array after Counting Sort: {array}")
