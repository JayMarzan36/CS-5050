def peak_entry(array, left=0, right=None):

    if right is None:

        right = len(array) - 1

    mid = (left + right) // 2

    if (mid == 0 or array[mid] >= array[mid - 1]) and (
        mid == len(array) - 1 or array[mid] >= array[mid + 1]
    ):

        return mid

    if mid > 0 and array[mid - 1] > array[mid]:

        return peak_entry(array, left, mid - 1)

    else:

        return peak_entry(array, mid + 1, right)


test_case = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 10, 5, 4, 3, 2, 1]

result = peak_entry(test_case)

print(f"Index {result} with value of {test_case[result]}")
