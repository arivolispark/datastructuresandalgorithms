"""
Title:  3 Sum

Given an array nums of n integers, are there elements a, b, c in nums such
that a + b + c = 0? Find all unique triplets in the array which gives the sum
of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

from typing import List


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        three_sum_list = list()
        if nums:
            #print(" nums: ", nums)
            nums.sort()
            #print(" nums: ", nums)

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                helper(nums, -nums[i], i + 1, three_sum_list)
        return three_sum_list


def helper(nums: List[int], target: int, left, three_sum_list: List[List[int]]) -> None:
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            three_sum_list.append([-target, nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
            while left < right and nums[right] == nums[right + 1]:
                right -= 1
        elif current_sum > target:
            right -= 1
        else:
            left += 1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1],[-1, -1, 2]])
    test(solution.threeSum([-3, 0, 1, 2, -1, 1, -2]), [[-3, 1, 2],[-2, 0, 2],[-2, 1, 1],[-1, 0, 1]])
    test(solution.threeSum([-5, 2, -1, -2, 3]), [[-5, 2, 3], [-2, -1, 3]])
