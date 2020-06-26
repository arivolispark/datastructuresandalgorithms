"""
Title:  Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is
between 1 and n (inclusive), prove that at least one duplicate number
must exist. Assume that there is only one duplicate number, find the
duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2


Example 2:
Input: [3,1,3,4,2]
Output: 3


Note:
1) You must not modify the array (assume the array is read only).
2) You must use only constant, O(1) extra space.
3) Your runtime complexity should be less than O(n^2).
4) There is only one duplicate number in the array, but it could be repeated more than once.

"""

from typing import List


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findDuplicate([1,3,4,2,2]), 2)
    test(solution.findDuplicate([3,1,3,4,2]), 3)
    test(solution.findDuplicate([2,5,9,6,9,3,8,9,7,1]), 9)
