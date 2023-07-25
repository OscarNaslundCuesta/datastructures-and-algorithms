"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def sort_part(array, lo, hi):
    """
    Sorts an array between the low and high indices (lo/hi).
    Returns the pivot_index
    :param array:
    :param lo:
    :param hi:
    :return:
    """
    pivot_index = hi  # convention of picking last item
    pivot_value = array[hi]
    left_index = lo

    while pivot_index != left_index:

        left_item = array[left_index]

        if pivot_value >= left_item:
            left_index += 1  # continues to next value if left_item is smaller than pivot_value
        else:
            # moves the values according to the algo and pivot_index decreases
            array[left_index] = array[pivot_index - 1]
            array[pivot_index - 1] = pivot_value
            array[pivot_index] = left_item
            pivot_index -= 1
            print(array)

    # return pivot_index to later use in recursion
    return pivot_index


def sort_and_split(array, lo, hi):
    """
    Handles the recursive part of the function.
    Splits the array into two arrays.
    Then calls sort_part to do the real sorting of arrays.
    :param array:
    :param lo:
    :param hi:
    :return:
    """
    if lo >= hi:  # finished if true
        return

    pivot_index = sort_part(array, lo, hi)
    sort_and_split(array, lo, pivot_index - 1)  # sorts lower part of array
    sort_and_split(array, pivot_index + 1, hi)  # sorts upper part of array


def quicksort(array):
    sort_and_split(array, 0, len(array) - 1)
    print("Final array:")
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
