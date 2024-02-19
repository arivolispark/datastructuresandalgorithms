"""
Title: 3033. Modify the Matrix

Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer.
Make answer equal to matrix, then replace each element with the value -1 with the maximum
element in its respective column.

Return the matrix answer.


Example 1:
Input: matrix = [[1,2,-1],[4,-1,6],[7,8,9]]
Output: [[1,2,9],[4,8,6],[7,8,9]]
Explanation: The diagram above shows the elements that are changed (in blue).
- We replace the value in the cell [1][1] with the maximum value in the column 1, that is 8.
- We replace the value in the cell [0][2] with the maximum value in the column 2, that is 9.


Example 2:
Input: matrix = [[3,-1],[5,2]]
Output: [[3,2],[5,2]]
Explanation: The diagram above shows the elements that are changed (in blue).


Constraints:
1) m == matrix.length
2) n == matrix[i].length
3) 2 <= m, n <= 50
4) -1 <= matrix[i][j] <= 100
The input is generated such that each column contains at least one non-negative integer.

"""

from typing import List
import math


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        result = matrix
        r, c = len(result), len(result[0])

        for i in range(r):
            for j in range(c):
                if result[i][j] == -1:
                    max_column_value = get_max_column_value(result, j)
                    result[i][j] = max_column_value
        return result


def get_max_column_value(result: List[List[int]], j: int):
    max_column_value = -1

    for i in range(len(result)):
        max_column_value = max(max_column_value, result[i][j])

    return max_column_value


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]), [[1,2,9],[4,8,6],[7,8,9]])
    test(solution.modifiedMatrix([[3,-1],[5,2]]), [[3,2],[5,2]])
