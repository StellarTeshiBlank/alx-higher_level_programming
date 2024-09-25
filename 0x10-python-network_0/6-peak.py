#!/usr/bin/python3
"""
Finds a peak element in a list of unsorted integers using binary search.
"""


def find_peak(list_of_integers):
    """
    Find a peak element in the list of integers.

    A peak element is an element that is greater than or
    equal to its neighbors.
    This function uses a binary search approach to
    find the peak in O(log n) time.

    Args:
        list_of_integers (list): A list of unsorted integers.

    Returns:
        int: A peak element if the list is not empty, otherwise None.
    """
    if not list_of_integers:
        return None

    return binary_search_peak(list_of_integers, 0, len(list_of_integers) - 1)


def binary_search_peak(li, low, high):
    """
    Helper function to perform binary search for peak element.

    Args:
        li (list): The list of integers.
        low (int): The starting index of the current search range.
        high (int): The ending index of the current search range.

    Returns:
        int: A peak element.
    """
    mid = (low + high) // 2

    if (mid == 0 or li[mid] >= li[mid - 1]) and \
       (mid == len(li) - 1 or li[mid] >= li[mid + 1]):
        return li[mid]

    if mid > 0 and li[mid - 1] > li[mid]:
        return binary_search_peak(li, low, mid - 1)

    return binary_search_peak(li, mid + 1, high)
