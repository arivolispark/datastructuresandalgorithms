"""
Title:  861. Score After Flipping Matrix

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that
row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the
matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).



Example 1:
Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


Example 2:
Input: grid = [[0]]
Output: 1


Constraints:
1) m == grid.length
2) n == grid[i].length
3) 1 <= m, n <= 20
4) grid[i][j] is either 0 or 1.

"""

from typing import List

class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        result = 0
        rows = len(grid)
        columns = len(grid[0])

        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(columns):
                    grid[i][j] = 1 - grid[i][j]

        col = [0] * columns

        for i in range(rows):
            for j in range(columns):
                col[j] += grid[i][j]

        for j in range(columns):
            if col[j] < rows - col[j]:
                col[j] = rows - col[j]

        for j in range(columns):
            result *= 2
            result += col[j]

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]), 39)
    test(solution.matrixScore([[0]]), 1)
