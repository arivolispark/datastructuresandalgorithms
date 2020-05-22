"""
Title:  Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how
many square submatrices have all ones.


Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

Output: 15

Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.


Example 2:

Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

Output: 7

Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.


Constraints:
1) 1 <= arr.length <= 300
2) 1 <= arr[0].length <= 300
3) 0 <= arr[i][j] <= 1

"""

from typing import List


class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix:
            rows = len(matrix)
            if rows:
                columns = len(matrix[0])
                if columns:
                    square_matrix = [[0 for _ in range(columns)] for _ in range(rows)]
                    #display(matrix)
                    square_count = 0

                    for i in range(columns):
                        square_matrix[0][i] = matrix[0][i]
                        if square_matrix[0][i] == 1:
                            square_count += square_matrix[0][i]

                    for i in range(1, rows):
                        square_matrix[i][0] = matrix[i][0]
                        if square_matrix[i][0] == 1:
                            square_count += square_matrix[i][0]

                    for i in range(1, rows):
                        for j in range(1, columns):
                            if matrix[i][j] == 1:
                                square_matrix[i][j] = 1 + min(square_matrix[i][j - 1], square_matrix[i - 1][j - 1], square_matrix[i - 1][j])
                                square_count += square_matrix[i][j]
                    #display(matrix)
                    #display(square_matrix)
                    return square_count
                return None
            return None
        return None


def display(matrix: List[List[int]]) -> None:
    print("\n")
    rows = len(matrix)
    if rows:
        columns = len(matrix[0])
        if columns:
            for i in range(rows):
                for j in range(columns):
                    print(matrix[i][j], end=" ")
                    if j == columns - 1:
                        print()


def get_test_case_1() -> List[List[int]]:
    return None


def get_test_case_2() -> List[List[int]]:
    matrix = [
        []
    ]
    return matrix


def get_test_case_3() -> List[List[int]]:
    matrix = [
        [0]
    ]
    return matrix


def get_test_case_4() -> List[List[int]]:
    matrix = [
        [1]
    ]
    return matrix


def get_test_case_5() -> List[List[int]]:
    matrix = [
        [1, 1],
        [1, 1],
    ]
    return matrix


def get_test_case_6() -> List[List[int]]:
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    return matrix


def get_test_case_61() -> List[List[int]]:
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    return matrix


def get_test_case_62() -> List[List[int]]:
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 0]
    ]
    return matrix


def get_test_case_7() -> List[List[int]]:
    matrix = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    return matrix


def get_test_case_8() -> List[List[int]]:
    matrix = [
        [1, 0, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [1, 0, 0, 1]
    ]
    return matrix


def get_test_case_9() -> List[List[int]]:
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    return matrix


def get_test_case_10() -> List[List[int]]:
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 1, 1, 0]
    ]
    return matrix


def get_test_case_11() -> List[List[int]]:
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0]
    ]
    return matrix


def get_test_case_12() -> List[List[int]]:
    matrix = [
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    return matrix


def get_test_case_13() -> List[List[int]]:
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    return matrix


def get_test_case_14() -> List[List[int]]:
    matrix = [
        [0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    return matrix


def get_test_case_15() -> List[List[int]]:
    matrix = [
        [0, 0, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 0]
    ]
    return matrix


def get_test_case_16() -> List[List[int]]:
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    return matrix


def get_test_case_17() -> List[List[int]]:
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    return matrix


def get_test_case_18() -> List[List[int]]:
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [1, 1, 1]
    ]
    return matrix


def get_test_case_19() -> List[List[int]]:
    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    return matrix


def get_test_case_20() -> List[List[int]]:
    matrix = [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ]
    return matrix


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.countSquares(get_test_case_1()), None)
    test(solution.countSquares(get_test_case_2()), None)
    test(solution.countSquares(get_test_case_3()), 0)
    test(solution.countSquares(get_test_case_4()), 1)
    test(solution.countSquares(get_test_case_5()), 5)
    test(solution.countSquares(get_test_case_6()), 14)
    test(solution.countSquares(get_test_case_61()), 8)
    test(solution.countSquares(get_test_case_62()), 11)
    test(solution.countSquares(get_test_case_7()), 30)
    test(solution.countSquares(get_test_case_8()), 7)
    test(solution.countSquares(get_test_case_9()), 15)
    test(solution.countSquares(get_test_case_10()), 17)
    test(solution.countSquares(get_test_case_11()), 37)
    test(solution.countSquares(get_test_case_12()), 3)
    test(solution.countSquares(get_test_case_13()), 15)
    test(solution.countSquares(get_test_case_14()), 1)
    test(solution.countSquares(get_test_case_15()), 31)
    test(solution.countSquares(get_test_case_16()), 15)
    test(solution.countSquares(get_test_case_17()), 15)
    test(solution.countSquares(get_test_case_18()), 3)
    test(solution.countSquares(get_test_case_19()), 15)
    test(solution.countSquares(get_test_case_20()), 7)
