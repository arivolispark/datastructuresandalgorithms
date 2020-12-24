
"""
Title:  Smallest Range II

Given an array A of integers, for each integer A[i] we need to choose 
either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value 
of B and the minimum value of B.

 

Example 1:
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]



Example 2:
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]



Example 3:
Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
 

Note:

1) 1 <= A.length <= 10000
2) 0 <= A[i] <= 10000
3) 0 <= K <= 10000

"""

from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        result = A[-1] - A[0]
        for i in range(len(A) - 1):
            result = min(result,
                         max(A[-1] - K, A[i] + K) - min(A[0] + K, A[i + 1] - K))
        return result 


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.smallestRangeII([1], 0), 0)
    test(solution.smallestRangeII([0,10], 2), 6)
    test(solution.smallestRangeII([1,3,6], 3), 3)

