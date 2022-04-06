
# 1. Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.

def selection_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


test_array = [6, 3, 8, 1, 9, 10, 2]
print(test_array)
print(selection_sort(test_array))


# 2. Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.

'''
def bubble_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


test_array = [5, 6, 2, 9, 11, 3]
print(test_array)
print(bubble_sort(test_array))
'''

# 3. Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.

'''
def insertion_sort(arr):
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


test_list = [4, 2, 6, 1, 8, 9]
print(test_list)
print(insertion_sort(test_list))
'''

# 4. Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.

'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))


def merge_arrays(left_arr, right_arr):
    merged_array = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_array.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_array.append(left_arr[i])
            i += 1
            continue

        if left_arr[i] >= right_arr[j]:
            merged_array.append(left_arr[i])
            i += 1
        else:
            merged_array.append(right_arr[j])
            j += 1
    return merged_array


test_array = [4, 8, 2, 1, 9, 6]
print(test_array)
print(merge_sort(test_array))
'''
