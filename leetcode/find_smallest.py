"""
Find smallest number in rotated sorted array

Consider an array of sorted integers. Example - [1, 2, 3, 4, 5, 6, 7, 8, 9].
Now this is rotated by some number k where k < length of array. Example, for
k = 3, array becomes - [4, 5, 6, 7, 8, 9, 1, 2, 3].

Given a sorted array which has been rotated by an unknown value, return the
index of smallest element in the array.

Example 1:
Input
[4, 5, 6, 7, 8, 9, 1, 2, 3]

Output
6



Example 2:
Input
[3, 4, 5, 6, 7, 8, 9, 1, 2]

Output
7


Write an algorithm to solve this problem and discuss the time complexity. Your
algorithm must be faster than O(n).
"""

from typing import List


class Solution:

    """
    def getSmallestIndex(arr):
        l = len(arr)
        return arr.index(min(arr))


    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
    print("rotation",getSmallestIndex(arr))
    """

    def find_smallest(self, nums: List[int]) -> int:
        if nums:
            start, end = 0, len(nums) - 1
            while start < end:
                mid = start + (end - start) // 2

                if nums[mid] > nums[start]:
                    start = mid
                elif nums[mid] < nums[start]:
                    end = mid
                else:
                    return mid + 1
            return mid
        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.find_smallest([4, 5, 6, 7, 8, 9, 1, 2, 3]), 6)
    test(solution.find_smallest([3, 4, 5, 6, 7, 8, 9, 1, 2]), 7)
