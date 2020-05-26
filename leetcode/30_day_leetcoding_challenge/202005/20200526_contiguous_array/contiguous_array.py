"""
Title:  Contiguous Array

Given a binary array, find the maximum length of
a contiguous subarray with equal number of 0 and 1.


Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.


Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


Note: The length of the given binary array will not exceed 50,000.

"""

from typing import List


class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        max_contiguous_array_length = 0
        if nums:
            n = len(nums)
            sum_index_map = {}
            current_sum = 0

            for i in range(n):
                if nums[i] == 0:
                    nums[i] = -1

            for i in range(n):
                current_sum += nums[i]

                if current_sum == 0:
                    max_contiguous_array_length = i + 1

                if current_sum not in sum_index_map:
                    sum_index_map[current_sum] = i
                else:
                    if max_contiguous_array_length < i - sum_index_map[current_sum]:
                        max_contiguous_array_length = i - sum_index_map[current_sum]

            for i in range(n):
                if nums[i] == -1:
                    nums[i] = 0
        return max_contiguous_array_length


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findMaxLength([]), 0)
    test(solution.findMaxLength([0]), 0)
    test(solution.findMaxLength([1]), 0)
    test(solution.findMaxLength([0, 0]), 0)
    test(solution.findMaxLength([1, 1]), 0)
    test(solution.findMaxLength([0, 1]), 2)
    test(solution.findMaxLength([0, 1, 0]), 2)
    test(solution.findMaxLength([0, 1, 1, 0, 1, 1, 1, 0]), 4)
    test(solution.findMaxLength([0, 0, 1, 0, 0, 0, 1, 1]), 6)
    test(solution.findMaxLength([0, 1, 1, 0, 0, 1, 0, 1, 1, 0]), 10)
