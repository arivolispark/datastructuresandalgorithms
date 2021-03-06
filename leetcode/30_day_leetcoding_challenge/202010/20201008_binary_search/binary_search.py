"""
Title:  Binary Search

Given a sorted (in ascending order) integer array nums of n elements and a target
value, write a function to search target in nums. If target exists, then return
its index, otherwise return -1.



Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4



Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1



Note:

1) You may assume that all elements in nums are unique.
2) n will be in the range [1, 10000].
3) The value of each element in nums will be in the range [-9999, 9999].

"""

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        if nums:
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.search([5], 5), 0)
    test(solution.search([-1,0,3,5,9,12], 9), 4)
    test(solution.search([-1,0,3,5,9,12], 2), -1)
