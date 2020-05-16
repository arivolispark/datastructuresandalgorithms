"""
Title:  Maximum Sum Circular Subarray

Given a circular array C of integers represented by A,
find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects
to the beginning of the array.  (Formally, C[i] = A[i]
when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed
buffer A at most once.  (Formally, for a
subarray C[i], C[i+1], ..., C[j], there does not
exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)


Example 1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3


Example 2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10


Example 3:
Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4


Example 4:
Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3


Example 5:
Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Note:
1) -30000 <= A[i] <= 30000
2) 1 <= A.length <= 30000

"""

from typing import List


class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        # Part 1:  Find max_subarray_sum for original_array using Kadane's algorithm
        original_array_kadane = kadane(A)

        # Part 2:  Find array sum of original array
        array_sum = 0
        for i in range(len(A)):
            array_sum += A[i]

        # Part 3:  Find array sum of modified array
        for i in range(len(A)):
            A[i] = -A[i]

        # Part 4:  Find max_subarray_sum for modified_array using Kadane's algorithm
        modified_array_kadane = kadane(A)

        # Part 5:  Find max_subarray_sum for modified_array using Kadane's algorithm
        circular_sum = array_sum + modified_array_kadane

        if circular_sum > original_array_kadane and circular_sum != 0:
            return circular_sum
        else:
            return original_array_kadane


def kadane(nums: List[int]) -> int:
    current_sum, max_sum = nums[0], nums[0]
    for n in nums[1:]:
        current_sum = max(n, current_sum + n)
        max_sum = max(current_sum, max_sum)
    return max_sum


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxSubarraySumCircular([1,-2,3,-2]), 3)
    test(solution.maxSubarraySumCircular([5,-3,5]), 10)
    test(solution.maxSubarraySumCircular([3,-1,2,-1]), 4)
    test(solution.maxSubarraySumCircular([3,-2,2,-3]), 3)
    test(solution.maxSubarraySumCircular([-2,-3,-1]), -1)
