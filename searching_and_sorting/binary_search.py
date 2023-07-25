"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""


def binary_search(input_array, value):
    found = False
    modified_array = input_array

    while len(modified_array) >= 1:

        middle_value = modified_array[int(round(len(modified_array) / 2))]
        middle_index = int(round(len(modified_array) / 2))

        if value == middle_value:
            return input_array.index(value)

        elif value > middle_value:
            modified_array = modified_array[middle_index + 1:]

        elif value < middle_value:
            modified_array = modified_array[:middle_index]

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
test_val3 = 29
test_val4 = 19
test_val5 = 1
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
print(binary_search(test_list, test_val3))
# print binary_search(test_list, test_val4)
# print binary_search(test_list, test_val5)