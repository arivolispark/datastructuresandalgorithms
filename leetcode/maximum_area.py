"""
Title:  Maximum Area

    Given an array arr, each item arr[i] in array represents a vertical line of length a[i].  You have to find the
    maximum area that can be formed by choosing two vertical lines in the array.

    Example:
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49

Time:  O(N)
Space:  O(1)
"""

import math


def max_area(arr):
    maximum_area = -math.inf
    left, right = 0, len(arr) - 1

    while left < right:
        length = right - left
        breadth = min(arr[left], arr[right])
        area = length * breadth
        maximum_area = max(area, maximum_area)

        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return maximum_area


if __name__ == "__main__":
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("\n arr: ", arr)

    maximum_area = max_area(arr)
    print("\n maximum_area: ", maximum_area)
