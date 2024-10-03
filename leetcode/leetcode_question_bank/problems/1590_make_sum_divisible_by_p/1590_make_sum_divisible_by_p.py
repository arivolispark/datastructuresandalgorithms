"""
Title:  1590. Make Sum Divisible by P

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the
sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.



Example 1:
Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.


Example 2:
Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.


Example 3:
Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.


Constraints:
1) 1 <= nums.length <= 10^5
2) 1 <= nums[i] <= 10^9
3) 1 <= p <= 10^9

"""

from typing import List


class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p

        if remainder == 0:
            return 0

        result = len(nums)
        prefix = 0
        prefixToIndex = {0: -1}

        for i, num in enumerate(nums):
            prefix += num
            prefix %= p
            target = (prefix - remainder + p) % p
            if target in prefixToIndex:
                result = min(result, i - prefixToIndex[target])
            prefixToIndex[prefix] = i

        return -1 if result == len(nums) else result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.minSubarray([3,1,4,2], 6), 1)
    test(solution.minSubarray([6,3,5,2], 9), 2)
    test(solution.minSubarray([1,2,3], 3), 0)
