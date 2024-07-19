"""
Title:

Given an m x n matrix of distinct numbers, return all lucky numbers in the
matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in
its row and maximum in its column.



Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.


Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.


Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.


Constraints:
1) m == mat.length
2) n == mat[i].length
3) 1 <= n, m <= 50
4) 1 <= matrix[i][j] <= 105.
5) All elements in the matrix are distinct.

"""

import math
from typing import List


class Solution:

    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []
        map = {}

        rows = len(matrix)
        columns = len(matrix[0])

        position_i, position_j = 0, 0
        for i in range(rows):
            row_min = math.inf
            for j in range(columns):
                if matrix[i][j] < row_min:
                    row_min = matrix[i][j]
                    position_i, position_j = i, j
                if j == columns - 1:
                    map[row_min] = [position_i, position_j]

        position_k, position_l = 0, 0
        for k in range(columns):
            column_max = -math.inf
            for l in range(rows):
                if matrix[l][k] > column_max:
                    column_max = matrix[l][k]
                    position_k, position_l = k, l
                if l == rows - 1:
                    if column_max in map:
                        pos_i, pos_j = map[column_max]
                        if pos_i == position_l and pos_j == position_k:
                            result.append(column_max)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]), [15])
    test(solution.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]), [12])
    test(solution.luckyNumbers([[7,8],[1,2]]), [7])
