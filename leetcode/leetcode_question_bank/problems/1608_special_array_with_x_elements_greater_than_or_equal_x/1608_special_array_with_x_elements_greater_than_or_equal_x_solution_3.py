"""
Title:  1608. Special Array With X Elements Greater Than or Equal X

You are given an array nums of non-negative integers. nums is considered special if there
exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is
special, the value for x is unique.



Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.


Example 2:
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.


Example 3:
Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.


Constraints:
1) 1 <= nums.length <= 100
2) 0 <= nums[i] <= 1000

"""

from typing import List


class Solution:

    def specialArray(self, nums: List[int]) -> int:
        length = len(nums)

        nums.sort()

        i = 1
        while i < length:
            if nums[length - i - 1] < i and nums[length - i] >= i:
                return i
            i += 1

        if nums[0] >= i:
            return i

        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.specialArray([3,5]), 2)
    test(solution.specialArray([0,0]), -1)
    test(solution.specialArray([0,4,3,0,4]), 3)
