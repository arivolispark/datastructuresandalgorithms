"""
Title:  Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the
largest square containing only 1's and return its area.


Example 1:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4

"""

from typing import List


class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix:
            rows = len(matrix)
            if rows == 0:
                return 0
            columns = len(matrix[0])

            side = 0
            dp = [[0] * (columns + 1) for _ in range(rows + 1)]
            for i in range(1, rows + 1):
                for j in range(1, columns + 1):
                    if matrix[i - 1][j - 1] == "1":
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                        side = max(side, dp[i][j])
            return side ** 2
        return 0


def display_matrix(matrix: List[List[str]]) -> None:
    if matrix:
        rows = len(matrix)
        if rows == 0:
            return
        columns = len(matrix[0])

        if rows and columns:
            for i in range(rows):
                print()
                for j in range(columns):
                    print(matrix[i][j], end=" ")


def get_test_case_1() -> List[List[str]]:
    return None


def get_test_case_2() -> List[List[str]]:
    matrix = [
        []
    ]
    return matrix


def get_test_case_3() -> List[List[str]]:
    matrix = [
        ["0"]
    ]
    return matrix


def get_test_case_4() -> List[List[str]]:
    matrix = [
        ["1"]
    ]
    return matrix


def get_test_case_5() -> List[List[str]]:
    matrix = [
        ["1", "1"],
        ["1", "1"],
    ]
    return matrix


def get_test_case_6() -> List[List[str]]:
    matrix = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    return matrix


def get_test_case_61() -> List[List[str]]:
    matrix = [
        ["1", "1", "1"],
        ["1", "0", "1"],
        ["1", "1", "1"]
    ]
    return matrix


def get_test_case_62() -> List[List[str]]:
    matrix = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "0"]
    ]
    return matrix


def get_test_case_7() -> List[List[str]]:
    matrix = [
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"],
        ["1", "1", "1", "1"]
    ]
    return matrix


def get_test_case_8() -> List[List[str]]:
    matrix = [
        ["1", "0", "0", "0"],
        ["0", "0", "1", "1"],
        ["1", "0", "1", "0"],
        ["1", "0", "0", "1"]
    ]
    return matrix


def get_test_case_9() -> List[List[str]]:
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    return matrix


def get_test_case_10() -> List[List[str]]:
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "1", "1", "0"]
    ]
    return matrix


def get_test_case_11() -> List[List[str]]:
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
        ["1", "0", "0", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "1", "0"]
    ]
    return matrix


def get_test_case_12() -> List[List[str]]:
    matrix = [
        ["0", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "0"]
    ]
    return matrix


def get_test_case_13() -> List[List[str]]:
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    return matrix


def get_test_case_14() -> List[List[str]]:
    matrix = [
        ["0", "0", "0", "0", "0"],
        ["1", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    return matrix


def get_test_case_15() -> List[List[str]]:
    matrix = [
        ["0","0","1","0"],
        ["1","1","1","1"],
        ["1","1","1","1"],
        ["1","1","1","0"],
        ["1","1","0","0"],
        ["1","1","1","1"],
        ["1","1","1","0"]
    ]
    return matrix


def get_test_case_16() -> List[List[str]]:
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    return matrix


def get_test_case_17() -> List[List[str]]:
    matrix = [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
    return matrix


def get_test_case_18() -> List[List[str]]:
    matrix = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["1", "1", "1"]
    ]
    return matrix

#[["0","0","0"],["0","0","0"],["1","1","1"]]

#[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]


if __name__ == "__main__":
    solution = Solution()

    #matrix = get_test_case_1()
    #matrix = get_test_case_2()
    #matrix = get_test_case_3()
    #matrix = get_test_case_4()
    #matrix = get_test_case_5()
    #matrix = get_test_case_6()
    #matrix = get_test_case_61()
    #matrix = get_test_case_62()
    #matrix = get_test_case_7()
    #matrix = get_test_case_8()
    #matrix = get_test_case_9()
    #matrix = get_test_case_10()
    #matrix = get_test_case_11()
    #matrix = get_test_case_12()
    #matrix = get_test_case_13()
    #matrix = get_test_case_14()
    #matrix = get_test_case_15()
    #matrix = get_test_case_16()
    #matrix = get_test_case_17()
    matrix = get_test_case_18()
    display_matrix(matrix)

    print("\n")
    largest_square_area = solution.maximalSquare(matrix)
    print("\n largest_square_area: ", largest_square_area)
