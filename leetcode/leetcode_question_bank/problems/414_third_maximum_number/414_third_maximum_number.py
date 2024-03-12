"""
Title:  414.  Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.



Example 1:
Input: nums = [3,2,1]
Output: 1

Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.


Example 2:
Input: nums = [1,2]
Output: 2

Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.


Example 3:
Input: nums = [2,2,3,1]
Output: 1

Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.


Constraints:
1) 1 <= nums.length <= 10^4
2) -2^31 <= nums[i] <= 2^31 - 1


Follow up: Can you find an O(n) solution?
"""

from typing import List
from heapq import *
import math


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        min_heap = []
        dict = {}

        if nums:
            for i in range(len(nums)):
                if nums[i] not in dict:
                    dict[nums[i]] = nums[i]
                    heappush(min_heap, nums[i])

            result = -math.inf
            if len(min_heap) >= 3:
                while len(min_heap) >= 3:
                    result = heappop(min_heap)
            else:
                while len(min_heap) >= 1:
                    result = heappop(min_heap)
            return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.thirdMax([3,2,1]), 1)
    test(solution.thirdMax([1,2]), 2)
    test(solution.thirdMax([2,2,3,1]), 1)
    test(solution.thirdMax([5,2,2]), 5)
    test(solution.thirdMax([1, -2147483648, 2]), -2147483648)
