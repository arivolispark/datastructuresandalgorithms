"""
Title:  523. Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums
has a good subarray or false otherwise.


A good subarray is a subarray where:
1) its length is at least two, and
2) the sum of the elements of the subarray is a multiple of k.


Note that:
1) A subarray is a contiguous part of the array.
2) An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.



Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.



Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false



Constraints:
1) 1 <= nums.length <= 10^5
2) 0 <= nums[i] <= 10^9
3) 0 <= sum(nums[i]) <= 2^31 - 1
4) 1 <= k <= 2^31 - 1

"""

from typing import List


class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}
        remainder = 0

        for i in range(len(nums)):
            remainder = (remainder + nums[i]) % k 

            if remainder not in remainder_map:
                remainder_map[remainder] = i
            else:
                if i - remainder_map[remainder] >= 2:
                    return True
        
        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.checkSubarraySum([23,2,4,6,7], 6), True)
    test(solution.checkSubarraySum([23,2,6,4,7], 6), True)
    test(solution.checkSubarraySum([23,2,6,4,7], 13), False)
    test(solution.checkSubarraySum([23,2,4,6,6], 7), True)
