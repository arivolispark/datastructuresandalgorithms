"""
Title:  Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent
cell, where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once.


Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.


Constraints:

1) board and word consists only of lowercase and uppercase English letters.
2) 1 <= board.length <= 200
3) 1 <= board[i].length <= 200
4) 1 <= word.length <= 10^3

"""

from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        if board and word:
            rows = len(board)
            if rows:
                columns = len(board[0])

                word_len = len(word)

                if word_len > rows * columns:
                    return False

                for i in range(rows):
                    for j in range(columns):
                        if board[i][j] == word[0]:
                            if dfs(board, word, i, j, rows, columns, 0):
                                return True
        return False


def dfs(board, word, x, y, rows, columns, level):
    if level == len(word):
        return True

    if x < 0 or y < 0 or x >= rows or y >= columns:
        return False

    if board[x][y] == word[level]:
        temp = board[x][y]
        board[x][y] = "@"

        result = dfs(board, word, x - 1, y, rows, columns, level + 1) or \
                 dfs(board, word, x + 1, y, rows, columns, level + 1) or \
                 dfs(board, word, x, y - 1, rows, columns, level + 1) or \
                 dfs(board, word, x, y + 1, rows, columns, level + 1)

        board[x][y] = temp
        return result
    else:
        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1() -> (List[List[str]], str):
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = "ABCCED"

    return board, word


def get_test_case_2() -> (List[List[str]], str):
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = "SEE"

    return board, word


def get_test_case_3() -> (List[List[str]], str):
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    word = "ABCB"

    return board, word


if __name__ == "__main__":
    solution = Solution()

    test(solution.exist(get_test_case_1()[0], get_test_case_1()[1]), True)
    test(solution.exist(get_test_case_2()[0], get_test_case_2()[1]), True)
    test(solution.exist(get_test_case_3()[0], get_test_case_3()[1]), False)
