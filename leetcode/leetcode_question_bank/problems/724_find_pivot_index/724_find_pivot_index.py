"""
Title:  724. Find Pivot index


Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.



Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0


Constraints:
1) 1 <= nums.length <= 104
2) -1000 <= nums[i] <= 1000


Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Args:
         numbers(list_int32)
        Returns:
         int32
        """
        # Write your code here.

        length = len(nums)

        sum = 0

        for i in range(length):
            sum += nums[i]

        if 0 == sum - nums[0]:
            return 0

        i, j = 0, length - 1
        left_sum, right_sum = 0, sum - nums[0]

        while i < j:
            if left_sum == right_sum:
                return i

            i += 1
            left_sum += nums[i - 1]
            right_sum -= nums[i]

        if 0 == sum - nums[length - 1]:
            return length - 1

        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.pivotIndex([1,7,3,6,5,6]), 3)
    test(solution.pivotIndex([1,2,3]), -1)
    test(solution.pivotIndex([2,1,-1]), 0)
