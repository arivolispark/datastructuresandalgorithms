"""
Title:  1219. Path with Maximum Gold

In a gold mine grid of size m x n, each cell in this mine has an integer representing
the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.


Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:
1) m == grid.length
2) n == grid[i].length
3) 1 <= m, n <= 15
4) 0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.

"""

from typing import List
import math

class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        answer = 0
        rows = len(grid)
        columns = len(grid[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def visit(x1, y1, current):
            if grid[x1][y1] == 0:
                return

            nonlocal answer
            answer = max(answer, current)

            previous = grid[x1][y1]
            grid[x1][y1] = 0

            for dx, dy in directions:
                x2 = x1 + dx
                y2 = y1 + dy
                if 0 <= x2 < rows and 0 <= y2 < columns and grid[x2][y2] > 0:
                    visit(x2, y2, current + grid[x2][y2])

            grid[x1][y1] = previous

        for i in range(rows):
            for j in range(columns):
                visit(i, j, grid[i][j])

        return answer


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]), 24)
    test(solution.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]), 28)
