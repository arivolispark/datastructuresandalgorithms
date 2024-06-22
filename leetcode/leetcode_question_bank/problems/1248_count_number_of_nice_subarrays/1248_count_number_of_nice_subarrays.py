"""
Title:  1248. Count Number of Nice Subarrays

Given an array of integers nums and an integer k. A continuous subarray
is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].


Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.


Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


Constraints:
1) 1 <= nums.length <= 50000
2) 1 <= nums[i] <= 10^5
3) 1 <= k <= nums.length

"""

from typing import List
from collections import deque


class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nice_count = 0
        length = len(nums)
        left = 0
        q = deque()

        for right in range(length):
            if nums[right] % 2 == 1:
                q.append(right)

            while len(q) > k:
                left = q.popleft() + 1

            if len(q) == k:
                degree = q[0] - left + 1
                nice_count += degree

        return nice_count


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.numberOfSubarrays([1,1,2,1,1], 3), 2)
    test(solution.numberOfSubarrays([2,4,6], 1), 0)
    test(solution.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2), 16)
