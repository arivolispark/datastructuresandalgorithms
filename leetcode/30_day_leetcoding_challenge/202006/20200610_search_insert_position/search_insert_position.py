"""
Title:  Search Insert Position

Given a sorted array and a target value, return the index
if the target is found. If not, return the index where it
would be if it were inserted in order.

You may assume no duplicates in the array.


Example 1:
Input: [1,3,5,6], 5
Output: 2


Example 2:
Input: [1,3,5,6], 2
Output: 1


Example 3:
Input: [1,3,5,6], 7
Output: 4


Example 4:
Input: [1,3,5,6], 0
Output: 0

"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums:
            start, end = 0, len(nums) - 1

            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.searchInsert([1,3,5,6], 5), 2)
    test(solution.searchInsert([1,3,5,6], 2), 1)
    test(solution.searchInsert([1,3,5,6], 7), 4)
    test(solution.searchInsert([1,3,5,6], 0), 0)
