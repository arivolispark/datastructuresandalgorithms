"""
Title:  Arranging Coins

Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.


Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].


Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]


Constraints:
1) 1 <= nums.length <= 1000
2) -10 ^ 6 <= nums[i] <= 10 ^ 6

"""

from typing import List


class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum_list = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            running_sum_list.append(sum)
        return running_sum_list


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.runningSum([1,2,3,4]), [1,3,6,10])
    test(solution.runningSum([1,1,1,1,1]), [1,2,3,4,5])
    test(solution.runningSum([3,1,2,10,1]), [3,4,6,16,17])
