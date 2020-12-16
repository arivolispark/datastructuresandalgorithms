
"""
Title:  Burst Balloons

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented 
by array nums. You are asked to burst all the balloons. If the you burst balloon i you will 
get nums[left] * nums[i] * nums[right] coins.  Here left and right are adjacent indices of i. After 
the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100



Example:
Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums_len = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for x in range(nums_len + 2)] for y in range(nums_len + 2)]
       
        for length in range(1, nums_len + 1):
            for left in range(1, nums_len - length + 2):
                right = left + length - 1
               
                for last in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], dp[left][last - 1] + nums[left - 1] * nums[last] * nums[right + 1] + dp[last + 1][right])
                   
        return dp[1][nums_len]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxCoins([3,1,5,8]), 167)
