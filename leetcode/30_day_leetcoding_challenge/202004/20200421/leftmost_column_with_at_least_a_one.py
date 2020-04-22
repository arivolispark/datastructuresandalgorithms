"""
Title:  Leftmost Column with at Least a One

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the
matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with
at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using
a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the
matrix is n * m.

Submissions making more than 1000 calls to BinaryMatrix.get will be judged
Wrong Answer.  Also, any solutions that attempt to circumvent the judge will
result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the
following four examples. You will not have access the binary matrix directly.



Example 1:

  0  0
  1  1

Input: mat = [[0,0],[1,1]]
Output: 0


Example 2:

  0  0
  0  1

Input: mat = [[0,0],[0,1]]
Output: 1


Example 3:

  0  0
  0  0

Input: mat = [[0,0],[0,0]]
Output: -1


Example 4:

  0  0  0  1
  0  0  1  1
  0  1  1  1

Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1


Constraints:

1) m == mat.length
2) n == mat[i].length
3) 1 <= m, n <= 100
4) mat[i][j] is either 0 or 1.
3) mat[i] is sorted in a non-decreasing way.

"""

from typing import List


"""
This is BinaryMatrix's API interface.
You should not implement it, or speculate about its implementation
"""


class BinaryMatrix(object):

    def __init__(self, matrix: List[List[int]]):
        if matrix and len(matrix) is not None and len(matrix[0]) is not None:
            rows = len(matrix)
            columns = len(matrix[0])

            for i in range(rows):
                for j in range(columns):
                    if matrix[i][j] != 0 and matrix[i][j] != 1:
                        raise Exception("Invalid value in cell [", i, "][", j, "]")

        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])

    def get(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    # def dimensions(self) -> list[]:
    def dimensions(self) -> list:
        return [self.rows, self.columns]


class Solution:

    """
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        x, y = binaryMatrix.dimensions()

        def seems_legit(column):
            return any(binaryMatrix.get(i, column) for i in range(x))

        lo = 0
        hi = y

        while lo < hi:
            mid = (lo + hi) // 2
            if seems_legit(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo if lo < y else -1
    """

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        display_matrix(binaryMatrix)
        rows, columns = binaryMatrix.dimensions()
        print("\n rows: ", rows, "\t columns: ", columns)

        min_left_most_column_index = columns

        for i in range(rows):
            start, end = 0, columns - 1

            while start <= end:
                mid = start + (end - start) // 2
                print("\n row[", i, "] mid: ", mid, end=" ")

                if binaryMatrix.get(i, mid) == 1:
                    end = mid - 1
                else:
                    start = mid + 1
            min_left_most_column_index = min(start, min_left_most_column_index)
        if min_left_most_column_index == columns:
            return -1
        else:
            return min_left_most_column_index


def display_matrix(binary_matrix: BinaryMatrix) -> None:
    print("\n")
    if binary_matrix is not None:
        matrix = binary_matrix.matrix
        if matrix and len(matrix) is not None and len(matrix[0]) is not None:
            rows = len(matrix)
            columns = len(matrix[0])

            for i in range(rows):
                for j in range(columns):
                    print(matrix[i][j], end=" ")
                    if j == columns - 1:
                        print()
    print("\n")


def get_test_case_1() -> BinaryMatrix:
    mat = [[0, 0]]
    binary_matrix = BinaryMatrix(mat)
    return binary_matrix


def get_test_case_2() -> BinaryMatrix:
    mat = [[0, 0], [1, 1]]
    binary_matrix = BinaryMatrix(mat)
    return binary_matrix


def get_test_case_3() -> BinaryMatrix:
    mat = [[0, 0], [0, 1]]
    binary_matrix = BinaryMatrix(mat)
    return binary_matrix


def get_test_case_4() -> BinaryMatrix:
    mat = [[0, 0], [0, 0]]
    binary_matrix = BinaryMatrix(mat)
    return binary_matrix


def get_test_case_5() -> BinaryMatrix:
    mat = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
    binary_matrix = BinaryMatrix(mat)
    return binary_matrix


if __name__ == "__main__":
    solution = Solution()

    #binary_matrix = get_test_case_1()
    #binary_matrix = get_test_case_2()
    #binary_matrix = get_test_case_3()
    #binary_matrix = get_test_case_4()
    binary_matrix = get_test_case_5()
    print("\n binary_matrix: ", binary_matrix)

    left_most_column_with_atleast_one = solution.leftMostColumnWithOne(binary_matrix)
    print("\n\n left_most_column_with_atleast_one: ", left_most_column_with_atleast_one)
