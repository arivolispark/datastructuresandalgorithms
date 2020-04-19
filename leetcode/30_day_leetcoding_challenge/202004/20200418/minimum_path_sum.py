"""
Title:  Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find
a path from top left to bottom right which minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
    Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from typing import List


class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid:
            rows = len(grid)
            columns = len(grid[0])

            if rows > 0 and columns > 0:
                dp = [[0 for _ in range(columns)] for _ in range(rows)]

                for i in range(rows):
                    for j in range(columns):
                        dp[i][j] += grid[i][j]
                        if i > 0 and j > 0:
                            dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
                        elif i > 0:
                            dp[i][j] += dp[i - 1][j]
                        elif j > 0:
                            dp[i][j] += dp[i][j - 1]

                display_grid(dp)
                return dp[rows - 1][columns - 1]
            else:
                return 0
        else:
            return 0


def display_grid(grid: List[List[int]]) -> None:
    if grid:
        rows = len(grid)
        columns = len(grid[0])
        print("\n rows: ", rows)
        print(" columns: ", columns)

        print()
        for row in range(rows):
            for column in range(columns):
                print(grid[row][column], end=" ")
                if column == columns - 1:
                    print()
    print("\n\n")


def get_test_case_1() -> List[List[int]]:
    return None


def get_test_case_2() -> List[List[int]]:
    return [[]]


def get_test_case_3() -> List[List[int]]:
    grid = [
        [11],
    ]
    return grid


def get_test_case_4() -> List[List[int]]:
    grid = [
        [1, 3]
    ]
    return grid


def get_test_case_5() -> List[List[int]]:
    grid = [
        [3],
        [8]
    ]
    return grid


def get_test_case_6() -> List[List[int]]:
    grid = [
        [1, 3],
        [7, 5]
    ]
    return grid


def get_test_case_7() -> List[List[int]]:
    grid = [
        [1, 3, 2],
        [7, 5, 1]
    ]
    return grid


def get_test_case_8() -> List[List[int]]:
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    return grid


def get_test_case_9() -> List[List[int]]:
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    return grid


def get_test_case_10() -> List[List[int]]:
    grid = [
        [1, 1],
        [1, 3,],
        [1, 6],
        [1, 1]
    ]
    return grid


def get_test_case_11() -> List[List[int]]:
    grid = [
        [10, 4, 6, 7],
        [2, 1, 4, 8],
        [3, 1, 8, 10],
        [10, 1, 1, 6],
        [4, 6, 1, 8]
    ]
    return grid


def get_test_case_12():
    grid = [
        [1, 4, 8, 6, 2, 2, 1, 7],
        [4, 7, 3, 1, 4, 5, 5, 1],
        [8, 8, 2, 1, 1, 8, 0, 1],
        [8, 9, 2, 9, 8, 0, 8, 9],
        [5, 7, 5, 7, 1, 8, 5, 5],
        [7, 0, 9, 4, 5, 6, 5, 6],
        [4, 9, 9, 7, 9, 1, 9, 0]
    ]
    return grid


if __name__ == "__main__":
    solution = Solution()

    #grid = get_test_case_1()
    #grid = get_test_case_2()
    #grid = get_test_case_3()
    #grid = get_test_case_4()
    #grid = get_test_case_5()
    #grid = get_test_case_6()
    #grid = get_test_case_7()
    #grid = get_test_case_8()
    #grid = get_test_case_9()
    #grid = get_test_case_10()
    #grid = get_test_case_11()
    grid = get_test_case_12()

    print("\n grid: ", grid)
    display_grid(grid)

    minimum_path_sum = solution.minPathSum(grid)
    print("\n minimum_path_sum: ", minimum_path_sum)
