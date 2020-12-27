
"""
Title:  Diagonal Traverse

Given a matrix of M x N elements (M rows, N columns), return all elements of the
matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:



Note:

1) The total number of elements of the given matrix will not exceed 10,000.

"""

from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        columns = len(matrix[0]) if rows > 0 else 0
        if columns == 0:
            return []

        result = [0 for i in range(rows * columns)]
        up = True
        row = col = 0

        for i in range(rows * columns):
            result[i] = matrix[row][col]

            if up:
                if col == columns - 1:
                    row = row + 1
                    up = not up
                elif row == 0:
                    col = col + 1
                    up = not up
                else:
                    row = row - 1
                    col = col + 1

            else:
                if row == rows - 1:
                    col = col + 1
                    up = not up
                elif col == 0:
                    row = row + 1
                    up = not up
                else:
                    row = row + 1
                    col = col - 1

        return result


def get_test_case_1_input():
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findDiagonalOrder(get_test_case_1_input()), [1,2,4,7,5,3,6,8,9])

