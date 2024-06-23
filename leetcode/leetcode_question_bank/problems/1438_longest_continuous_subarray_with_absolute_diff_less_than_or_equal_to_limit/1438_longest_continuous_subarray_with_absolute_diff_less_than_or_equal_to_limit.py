"""
Title:  1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

Given an array of integers nums and an integer limit, return the size of
the longest non-empty subarray such that the absolute difference between any
two elements of this subarray is less than or equal to limit.



Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.


Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.


Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:
1) 1 <= nums.length <= 10^5
2) 1 <= nums[i] <= 10^9
3) 0 <= limit <= 10^9

"""

from typing import List
from sortedcontainers import SortedList


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        result = 0
        sl = SortedList()

        left = 0
        for right in range(len(nums)):
            sl.add(nums[right])

            while sl[-1] - sl[0] > limit:
                sl.remove(nums[left])
                left += 1
            result = max(right - left + 1, result)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.longestSubarray([8,2,4,7], 4), 2)
    test(solution.longestSubarray([10,1,2,4,7,2], 5), 4)
    test(solution.longestSubarray([4,2,2,2,4,4,2,2], 0), 3)
