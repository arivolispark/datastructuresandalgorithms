"""
Title: Single Number


Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

from typing import List


class Solution:

    def single_number(self, nums: List[int]) -> int:
        if nums is None or type(nums) is not list or len(nums) <= 0 or (len(nums) % 2 == 0):
            raise Exception("Invalid nums supplied.  Please supply valid nums")

        number_without_a_pair = 0
        for num in nums:
            number_without_a_pair ^= num
        return number_without_a_pair


if __name__ == "__main__":
    #nums = [2, 2, 1]
    nums = [4, 1, 2, 1, 2]
    print("\n nums: ", nums)

    solution = Solution()
    number_without_a_pair = solution.single_number(nums)
    print("\n number_without_a_pair: ", number_without_a_pair)
