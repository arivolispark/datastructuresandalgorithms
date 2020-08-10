"""
Title:  Rotting Oranges

In a given grid, each cell can have one of three values:

1) the value 0 representing an empty cell;
2) the value 1 representing a fresh orange;
3) the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh
orange.  If this is impossible, return -1 instead.



Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4



Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.



Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:
1) 1 <= grid.length <= 10
2) 1 <= grid[0].length <= 10
3) grid[i][j] is only 0, 1, or 2.


"""

from typing import List


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_oranges = []
        rows, columns, fresh_oranges, time_in_minutes = len(grid), len(grid[0]), 0, 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    rotten_oranges.append([i, j])
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        while len(rotten_oranges) > 0:
            num = len(rotten_oranges)
            for i in range(num):
                x, y = rotten_oranges[0]
                rotten_oranges.pop(0)
                if x > 0 and grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    fresh_oranges -= 1
                    rotten_oranges.append([x - 1, y])
                if y > 0 and grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    fresh_oranges -= 1
                    rotten_oranges.append([x, y - 1])
                if x < rows - 1 and grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    fresh_oranges -= 1
                    rotten_oranges.append([x + 1, y])
                if y < columns - 1 and grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    fresh_oranges -= 1
                    rotten_oranges.append([x, y + 1])
            if len(rotten_oranges) > 0:
                time_in_minutes += 1
        return time_in_minutes if (fresh_oranges == 0) else -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)
    test(solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)
    test(solution.orangesRotting([[0,2]]), 0)
