"""
Title:  Maximum Distance in Arrays

Given m arrays, and each array is sorted in ascending order. Now you can pick up
two integers from two different arrays (each array picks one) and calculate the
distance. We define the distance between two integers a and b to be their absolute
difference |a-b|. Your task is to find the maximum distance.



Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.


Note:
1) Each given array will have at least 1 number. There will be at least two non-empty arrays.
2) The total number of the integers in all the m arrays will be in the range of [2, 10000].
3) The integers in the m arrays will be in the range of [-10000, 10000].

"""


from typing import List
import math


class Solution:

    def maxDistance(self, arrays: List[List[int]]) -> int:
        if not arrays or len(arrays) < 2:
            return 0

        result = -math.inf
        min_value, max_value = arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            current_distance = max(abs(min_value - current_max), abs(max_value - current_min))
            result = max(result, current_distance)
            min_value = min(min_value, current_min)
            max_value = max(max_value, current_max)

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxDistance([[1,2,3], [4,5], [1,2,3]]), 4)
    test(solution.maxDistance([[1,4],[0,5]]), 4)
