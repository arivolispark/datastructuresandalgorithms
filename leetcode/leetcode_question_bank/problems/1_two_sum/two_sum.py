"""
Problem #: 1
Title:  Two Sum

Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

from typing import List
import math


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums:
            result = []
            sorted_nums = sorted(nums)

            start = 0
            end = len(sorted_nums) - 1

            number_1 = -math.inf
            number_2 = -math.inf
            while start < end:
                if sorted_nums[start] + sorted_nums[end] < target:
                    start += 1
                elif sorted_nums[start] + sorted_nums[end] > target:
                    end -= 1
                elif sorted_nums[start] + sorted_nums[end] == target:
                    number_1 = sorted_nums[start]
                    number_2 = sorted_nums[end]
                    break

            if number_1 > -math.inf and number_2 > -math.inf:
                for i in range(len(nums)):
                    if nums[i] == number_1:
                        result.append(i)
                for i in range(len(nums)):
                    if nums[i] == number_2 and i not in result:
                        result.append(i)

            if len(result) == 2:
                return result
            return [-1, -1]
        return [-1, -1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.twoSum([2, 7, 11, 15], 9), [0, 1])
    test(solution.twoSum([3, 2, 4], 6), [1, 2])
    test(solution.twoSum([3, 3], 6), [0, 1])
    test(solution.twoSum([-3, 4, 3, 90], 0), [0, 2])
