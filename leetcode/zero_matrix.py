"""
Zero matrix
You are given a 2D matrix (m x n) with integers in it. You have to modify this
matrix in place such that if any item (i,j) is 0 then entire row and column
containing that element should be set to 0.
__


Example 1:

Input:
[[1, 1, 1],
 [1, 0, 1],
 [1, 1, 1]]

Output:
[[1, 0, 1],
 [0, 0, 0],
 [1, 0, 1]]
__


Example 2:

Input
[[1, 0, 0],
 [1, 1, 1],
 [1, 1, 0]]

Output
[[0, 0, 0],
 [1, 0, 0],
 [0, 0, 0]]

Write an algorithm to solve this problem and describe the time complexity for
your code.
"""


from typing import List


class Solution:

    def zero_matrix(self, matrix: List[List[int]]):
        if matrix:
            rows = len(matrix)
            if matrix[0]:
                columns = len(matrix[0])

            updated = [[False for _ in range(columns)] for _ in range(rows)]

            for i in range(rows):
                for j in range(columns):
                    if matrix[i][j] == 0 and updated[i][j] is False:
                        for k in range(rows):
                            if updated[k][j] is False:
                                matrix[k][j] = 0
                                updated[k][j] = True
                        for k in range(columns):
                            if updated[i][k] is False:
                                matrix[i][k] = 0
                                updated[i][k] = True

        return matrix


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1_input():
    return [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]


def get_test_case_1_output():
    return [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]


def get_test_case_2_input():
    return [
        [1, 0, 0],
        [1, 1, 1],
        [1, 1, 0]
    ]


def get_test_case_2_output():
    return [
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]


if __name__ == "__main__":
    solution = Solution()

    test(solution.zero_matrix(get_test_case_1_input()), get_test_case_1_output())
    test(solution.zero_matrix(get_test_case_2_input()), get_test_case_2_output())
