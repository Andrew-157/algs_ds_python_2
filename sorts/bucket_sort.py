# Bucket Sort in Python

# Use any stable sort to sort elements inside each bucket
def insertion_sort(array: list) -> None:

    for step in range(len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key


def bucket_sort(array: list) -> list:

    num_slots = 10

    buckets = []

    for _ in range(num_slots):
        buckets.append([])

    for j in array:
        index = int(j * 10)
        buckets[index].append(j)

    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    k = 0

    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            array[k] = buckets[i][j]
            k += 1


array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print(f"Array before Bucket Sort: {array}")
bucket_sort(array)
print(f"Array after Bucket Sort: {array}")
