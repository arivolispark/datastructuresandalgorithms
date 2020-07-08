"""
Title:  Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents
land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or more
connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water
around the island). One cell is a square with side length 1. The grid is rectangular,
width and height don't exceed 100. Determine the perimeter of the island.

Example 1:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""

from typing import List


class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        if grid:
            rows = len(grid)
            if rows:
                columns = len(grid[0])
                perimeter_grid = [[0 for _ in range(columns)] for _ in range(rows)]

                if grid[0][0] == 1:
                    perimeter_grid[0][0] = 4

                for i in range(1, rows):
                    if grid[i][0] == 1:
                        perimeter_grid[i][0] = 4
                        if grid[i - 1][0] == 1:
                            perimeter_grid[i - 1][0] -= 1
                            perimeter_grid[i][0] -= 1

                for j in range(1, columns):
                    if grid[0][j] == 1:
                        perimeter_grid[0][j] = 4
                        if grid[0][j - 1] == 1:
                            perimeter_grid[0][j - 1] -= 1
                            perimeter_grid[0][j] -= 1

                for i in range(1, rows):
                    for j in range(1, columns):
                        if grid[i][j] == 1:
                            perimeter_grid[i][j] = 4
                            if grid[i - 1][j] == 1:
                                perimeter_grid[i - 1][j] -= 1
                                perimeter_grid[i][j] -= 1
                            if grid[i][j - 1] == 1:
                                perimeter_grid[i][j - 1] -= 1
                                perimeter_grid[i][j] -= 1

                #print(" perimeter_grid: ", perimeter_grid)

                for i in range(rows):
                    for j in range(columns):
                        perimeter += perimeter_grid[i][j]
        return perimeter


def get_test_case_1():
    return [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]


def get_test_case_2():
    return [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ]


def get_test_case_3():
    return [
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]
    ]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.islandPerimeter(get_test_case_1()), 0)
    test(solution.islandPerimeter(get_test_case_2()), 16)
    test(solution.islandPerimeter(get_test_case_3()), 16)
