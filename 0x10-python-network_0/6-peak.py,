#!/usr/bin/python3
"""
This module contains the function find_peak.
"""


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak element (if found), or None if the list is empty.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[low]

# Test the function
if __name__ == "__main__":
    list1 = [1, 2, 4, 6, 3]
    list2 = [4, 2, 1, 2, 3, 1]
    list3 = [2, 2, 2]
    list4 = []
    list5 = [-2, -4, 2, 1]
    list6 = [4, 2, 1, 2, 2, 2, 3, 1]

    print(find_peak(list1))  # Output: 6
    print(find_peak(list2))  # Output: 3
    print(find_peak(list3))  # Output: 2
    print(find_peak(list4))  # Output: None
    print(find_peak(list5))  # Output: 2
    print(find_peak(list6))  # Output: 4
