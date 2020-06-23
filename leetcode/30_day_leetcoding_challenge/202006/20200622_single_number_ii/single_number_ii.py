"""
Title:  Single Number II

Given a non-empty array of integers, every element appears three times
except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?


Example 1:
Input: [2,2,3,2]
Output: 3


Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99

"""

from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        if nums:
            once, twice, thrice = 0, 0, 0

            for i in range(len(nums)):
                twice = twice | (once & nums[i])
                once = once ^ nums[i]
                thrice = once & twice
                once &= ~thrice
                twice &= ~thrice
            return once


def get_test_case_1_input() -> List[List[int]]:
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    return dungeon


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.singleNumber([2,2,3,2]), 3)
    test(solution.singleNumber([0,1,0,1,0,1,99]), 99)
