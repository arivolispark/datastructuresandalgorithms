"""
Title:  Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count
the number of islands. An island is surrounded by water
and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid
are all surrounded by water.


Example 1:
Input:
11110
11010
11000
00000

Output: 1


Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        if grid:
            rows = len(grid)
            columns = len(grid[0])

            visited = [[False for _ in range(columns)] for _ in range(rows)]

            for row in range(rows):
                for column in range(columns):
                    if visited[row][column] is False and grid[row][column] == "1":
                        dfs(grid, rows, row, columns, column, visited)
                        number_of_islands += 1
        return number_of_islands


def dfs(grid: List[List[str]], rows: int, row: int, columns: int, column: int, visited: List[List[bool]]):
    neigbhor_row_cells = [-1, 0, 0, 1]
    neigbhor_column_cells = [0, -1, 1, 0]

    visited[row][column] = True

    for k in range(4):
        if is_safe(grid, rows, row + neigbhor_row_cells[k], columns, column + neigbhor_column_cells[k], visited):
            dfs(grid, rows, row + neigbhor_row_cells[k], columns, column + neigbhor_column_cells[k], visited)


def is_safe(grid: List[List[str]], rows: int, row: int, columns: int, column: int, visited: List[List[bool]]) -> bool:
    return row >= 0 and row < rows and column >= 0 and column < columns and not visited[row][column] and grid[row][column] == "1"


def display_grid(grid: List[List[str]]) -> None:
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


def display_visited(visited: List[List[bool]]) -> None:
    if visited:
        rows = len(visited)
        columns = len(visited[0])
        print("\n rows: ", rows)
        print(" columns: ", columns)

        print()
        for row in range(rows):
            for column in range(columns):
                print(visited[row][column], end=" ")
                if column == columns - 1:
                    print()


def get_test_case_1() -> List[List[str]]:
    return None


def get_test_case_2() -> List[List[str]]:
    return [[]]


def get_test_case_3() -> List[List[str]]:
    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    return grid


def get_test_case_4() -> List[List[str]]:
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    return grid


def get_test_case_5() -> List[List[str]]:
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    return grid


def get_test_case_6() -> List[List[str]]:
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    return grid


if __name__ == "__main__":
    solution = Solution()

    #grid = get_test_case_1()
    #grid = get_test_case_2()
    #grid = get_test_case_3()
    #grid = get_test_case_4()
    #grid = get_test_case_5()
    grid = get_test_case_6()

    print("\n grid: ", grid)
    display_grid(grid)

    number_of_islands = solution.numIslands(grid)
    print("\n number_of_islands: ", number_of_islands)
