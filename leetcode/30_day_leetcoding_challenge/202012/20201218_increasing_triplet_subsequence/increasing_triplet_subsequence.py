
"""
Title:  Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of
indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].  If no
such indices exists, return false.



Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.



Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.



Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1) 1 <= nums.length <= 105
2) -2^31 <= nums[i] <= 2^31 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

"""

from typing import List
import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low = high = math.inf
        for num in nums:
            if num < low:
                low = num
            elif num < high:
                high = num
            else:
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

    test(solution.increasingTriplet([1,2,3,4,5]), True)
    test(solution.increasingTriplet([5,4,3,2,1]), False)
    test(solution.increasingTriplet([2,1,5,0,4,6]), True)
