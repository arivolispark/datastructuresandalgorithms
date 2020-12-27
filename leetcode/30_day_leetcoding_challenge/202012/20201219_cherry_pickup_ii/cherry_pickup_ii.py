
"""
Title:  Cherry Pickup II

Given a rows x cols matrix grid representing a field of cherries. Each cell in 
grid represents the number of cherries that you can collect.

You have two robots that can collect cherries for you, Robot #1 is located at the 
top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by following the rules below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an 
empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.
 

Example 1:



Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.



Example 2:



Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.



Example 3:

Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
Output: 22



Example 4:

Input: grid = [[1,1],[1,1]]
Output: 4
 

Constraints:

1) rows == grid.length
2) cols == grid[i].length
3) 2 <= rows, cols <= 70
4) 0 <= grid[i][j] <= 100 

"""

from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        cache = [[[None] * (cols + 1) for _ in range(cols + 1)] for _ in range(rows + 1)]
        calculated = [[[False] * (cols + 1) for _ in range(cols + 1)] for _ in range(rows + 1)]

        def maxCherry(row, c1, c2):
            if row == rows:
                return 0

            if calculated[row][c1][c2]:
                return cache[row][c1][c2]

            best = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    nc1, nc2 = c1 + dc1, c2 + dc2

                    if 0 <= nc1 < cols and 0 <= nc2 < cols:
                        cherry = grid[row][c1]
                        if c1 != c2:
                            cherry += grid[row][c2]
                        best = max(best, maxCherry(row + 1, nc1, nc2) + cherry)
            calculated[row][c1][c2] = True
            cache[row][c1][c2] = best
            return best
        return maxCherry(0, 0, cols - 1)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]]), 24)
    test(solution.cherryPickup([[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]), 28)
    test(solution.cherryPickup([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]), 22)
    test(solution.cherryPickup([[1,1],[1,1]]), 4)

