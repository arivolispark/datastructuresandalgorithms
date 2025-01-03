"""
Title:  3254. Find the Power of K-Size Subarrays I

You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

1) Its maximum element if all of its elements are consecutive and sorted in ascending order.
2) -1 otherwise.

You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power
of nums[i..(i + k - 1)].



Example 1:
Input: nums = [1,2,3,4,3,2,5], k = 3
Output: [3,4,-1,-1,-1]
Explanation:
There are 5 subarrays of nums of size 3:
[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.


Example 2:
Input: nums = [2,2,2,2,2], k = 4
Output: [-1,-1]


Example 3:
Input: nums = [3,2,3,2,3,2], k = 2
Output: [-1,3,-1,3,-1]



Constraints:
1) 1 <= n == nums.length <= 500
2) 1 <= nums[i] <= 10^5
3) 1 <= k <= n

"""

from typing import List


class Solution:

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        f = [1] * length
        for i in range(1, length):
            if nums[i] == nums[i - 1] + 1:
                f[i] = f[i - 1] + 1
        return [nums[i] if f[i] >= k else -1 for i in range(k - 1, length)]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test((solution.resultsArray([1,2,3,4,3,2,5], 3)), [3,4,-1,-1,-1])
    test((solution.resultsArray([2,2,2,2,2], 4)), [-1,-1])
    test((solution.resultsArray([3,2,3,2,3,2], 2)), [-1,3,-1,3,-1])
    test((solution.resultsArray([1,4], 1)), [1,4])
