"""
Title:  Largest Component Size by Common Factor

Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.



Example 1:
Input: [4,6,15,35]
Output: 4



Example 2:
Input: [20,50,9,63]
Output: 2



Example 3:
Input: [2,3,6,7,4,12,21,39]
Output: 8



Note:
1) 1 <= A.length <= 20000
2) 1 <= A[i] <= 100000

"""

from typing import List
import math


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parent = [-1] * 100001

        def find_helper(x):
            if parent[x] == -1:
                return x
            parent[x] = find_helper(parent[x])
            return parent[x]

        def union_helper(x, y):
            xp = find_helper(x)
            yp = find_helper(y)
            if xp != yp:
                parent[yp] = xp

        for x in A:
            for i in range(2, int(math.sqrt(x)) + 1):
                if x % i == 0:
                    union_helper(i, x)
                    union_helper(x, x // i)

        count = 0
        largest_component_map = {}

        for x in A:
            xp = find_helper(x)
            count = max(count, 1 + largest_component_map.get(xp, 0))
            largest_component_map[xp] = 1 + largest_component_map.get(xp, 0)
        return count


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.largestComponentSize([4,6,15,35]), 4)
    test(solution.largestComponentSize([20,50,9,63]), 2)
    test(solution.largestComponentSize([2,3,6,7,4,12,21,39]), 8)
