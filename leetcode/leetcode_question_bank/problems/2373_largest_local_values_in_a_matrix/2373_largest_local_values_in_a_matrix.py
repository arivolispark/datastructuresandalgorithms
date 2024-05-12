"""
Title:  2373. Largest Local Values in a Matrix

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered
around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix
in grid.

Return the generated matrix.



Example 1:
Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value
of a contiguous 3 x 3 matrix in grid.


Example 2:
Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.


Constraints:
1) n == grid.length == grid[i].length
2) 3 <= n <= 100
3) 1 <= grid[i][j] <= 100

"""

import math
from typing import List

class Solution:

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows, columns = len(grid), len(grid[0])

        result = [[0] * (columns - 2) for _ in range(rows - 2)]

        for i in range(1, rows - 1):
            for j in range(1, columns - 1):
                for local_i in [-1, 0, 1]:
                    for local_j in [-1, 0, 1]:
                        result[i - 1][j - 1] = max(result[i - 1][j - 1], grid[i + local_i][j + local_j])

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]), [[9,9],[8,6]])
    test(solution.largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]), [[2,2,2],[2,2,2],[2,2,2]])
