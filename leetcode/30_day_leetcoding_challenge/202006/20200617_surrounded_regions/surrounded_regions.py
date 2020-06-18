"""
Title:  Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O),
capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in
that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X


After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X


Explanation:

Surrounded regions shouldn’t be on the border, which means
that any 'O' on the border of the board are not flipped
to 'X'. Any 'O' that is not on the border and it is not
connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected
horizontally or vertically.

"""

from typing import List


class Solution:

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board

        if not self.board:
            return self.board

        rows = len(self.board)
        columns = len(self.board[0])

        self.rows = rows
        self.columns = columns

        for i in range(self.rows):
            if self.board[i][0] == 'O':
                self.dfs(i, 0)
            if self.board[i][self.columns - 1] == 'O':
                self.dfs(i, self.columns - 1)

        for i in range(self.columns):
            if self.board[0][i] == 'O':
                self.dfs(0, i)
            if self.board[len(self.board) - 1][i] == 'O':
                self.dfs(rows - 1, i)

        for i in range(self.rows):
            for j in range(self.columns):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                elif self.board[i][j] == '*':
                    self.board[i][j] = 'O'

    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= self.rows or j >= self.columns or self.board[i][j] == 'X' or self.board[i][j] == '*':
            return
        self.board[i][j] = '*'
        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)


def get_test_case_1_input():
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', '0', '0', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', '0', 'X', 'X']
    ]
    return board


def get_test_case_1_output():
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', 'X', 'X', 'X'],
        ['X', '0', 'X', 'X']
    ]
    return board


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test_case_inputs = [
        get_test_case_1_input()
    ]

    test_case_outputs = [
        get_test_case_1_output()
    ]

    for i in range(len(test_case_inputs)):
        solution.solve(test_case_inputs[i])

    for i in range(len(test_case_inputs)):
        test(test_case_inputs[i], test_case_outputs[i])
