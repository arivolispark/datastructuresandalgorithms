"""
Title:  2342. Max Sum of a Pair With Equal Sum of Digits

You are given a 0-indexed array nums consisting of positive integers. You can choose two
indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal
to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible
indices i and j that satisfy the conditions. If no such pair of indices exists, return -1.



Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.


Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.


Constraints:
1) 1 <= nums.length <= 105
2) 1 <= nums[i] <= 109

"""

from typing import List
import math
from collections import defaultdict


class Solution:

    def maximumSum_1(self, nums: List[int]) -> int:
        max_sum = -1
        digit_sum_max_num = defaultdict(int)

        for num in nums:
            digit_sum = 0
            temp_num = num
            while temp_num:
                digit_sum += temp_num % 10
                temp_num //= 10

            if digit_sum in digit_sum_max_num:
                max_sum = max(max_sum, digit_sum_max_num[digit_sum] + num)

            digit_sum_max_num[digit_sum] = max(digit_sum_max_num[digit_sum], num)

        return max_sum

    def maximumSum(self, nums: List[int]) -> int:
        result = -math.inf
        map = {}

        for i in range(len(nums)):
            s = sum_of_digits(nums[i])
            if s not in map:
                map[s] = [nums[i]]
            else:
                v = map[s]
                v.append(nums[i])
                map[s] = v

        if len(map) == len(nums):
            return -1

        for k, v in map.items():
            if len(v) > 1:
                if len(v) > 2:
                    v.sort()
                s = v[-1] + v[-2]
                result = max(result, s)

        return result


def sum_of_digits(num: int) -> int:
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maximumSum([18,43,36,13,7]), 54)
    test(solution.maximumSum([10,12,19,14]), -1)
    test(solution.maximumSum([9,2,2,5]), 4)
    test(solution.maximumSum([368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183]), 835)
