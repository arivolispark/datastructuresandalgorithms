"""
Title:  624. Maximum Distance in Arrays

You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks
one) and calculate the distance. We define the distance between two integers
a and b to be their absolute difference |a - b|.

Return the maximum distance.



Example 1:
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or
third array and pick 5 in the second array.


Example 2:
Input: arrays = [[1],[1]]
Output: 0


Constraints:
1) m == arrays.length
2) 2 <= m <= 105
3) 1 <= arrays[i].length <= 500
4) -10^4 <= arrays[i][j] <= 10^4
5) arrays[i] is sorted in ascending order.
6) There will be at most 10^5 integers in all the arrays.

"""
from typing import List
import math


class Solution:

    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        length = len(arrays)
        current_min, current_max = arrays[0][0], arrays[0][-1]

        for i in range(1, length):
            result = max(result, abs(arrays[i][-1] - current_min), abs(arrays[i][0] - current_max))
            current_min = min(current_min, arrays[i][0])
            current_max = max(current_max, arrays[i][-1])
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxDistance([[1,2,3],[4,5],[1,2,3]]), 4)
    test(solution.maxDistance([[1],[1]]), 0)
    test(solution.maxDistance([[1], [0]]), 1)
