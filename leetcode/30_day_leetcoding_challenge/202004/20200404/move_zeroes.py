"""
Title:  Move Zeroes


Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.


Time:  O(N)
Space:  O(1)
"""

from typing import List


class Solution:

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return nums

        zero_pointer = 0

        while True:
            while zero_pointer < len(nums) and nums[zero_pointer] != 0:
                zero_pointer += 1

            non_zero_pointer = zero_pointer + 1

            while non_zero_pointer < len(nums) and nums[non_zero_pointer] == 0:
                non_zero_pointer += 1

            if non_zero_pointer < len(nums):
                nums[zero_pointer], nums[non_zero_pointer] = nums[non_zero_pointer], nums[zero_pointer]
                zero_pointer += 1
            else:
                break

        print("\n After moving zeroes, nums: ", nums)


if __name__ == "__main__":
    #nums = []
    #nums = [0]
    #nums = [12]
    #nums = [0, 0]
    #nums = [1, 4]
    #nums = [0, 41]
    #nums = [24, 0]
    #nums = [3, 0, 0, 0]
    #nums = [0, 0, 0, 3, 2, 4, 1]
    #nums = [5, 7, 0, 0, 0]
    #nums = [5, 0, -7, -6, 0, 0, 0]
    nums = [0, 1, 0, 3, 12]
    print("\n nums: ", nums)

    solution = Solution()
    solution.moveZeroes(nums)
