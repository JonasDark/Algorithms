

# ALGORITHMS HW 4

# Even First
# Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input array).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


def evens_first(a):
    list_even = []
    list_odd = []

    for i in range(0, a):
        element = int(input('Enter your number: '))
        if element % 2 == 0:
            list_even.append(element)
        else:
            list_odd.append(element)

    combined_list = list_even + list_odd
    print(combined_list)


num = int(input('Enter the quantity of elements in your list: '))
evens_first(num)


# Increment a Number
# Write a program that takes as input an array of digits encoding a non-negative decimal integer D and updates
# the array to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

'''
def increment(arr):
    i = len(arr) - 1
    while i >= 0 and arr[i] == 9:
        arr[i] = 0
        i -= 1

    if i >= 0:
        arr[i] += 1
    else:
        arr.insert(0, 1)

    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    
    return arr


a = [9, 9, 9]
print(increment(a))
'''