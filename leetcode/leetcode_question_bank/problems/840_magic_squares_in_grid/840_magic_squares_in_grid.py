"""
Title:  840. Magic Squares In Grid

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that
each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids
are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers
up to 15.



Example 1:
Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.


Example 2:
Input: grid = [[8]]
Output: 0


Constraints:
1) row == grid.length
2) col == grid[i].length
3) 1 <= row, col <= 10
4) 0 <= grid[i][j] <= 15

"""

from typing import List


class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magic_squares_count = 0
        rows, columns = len(grid), len(grid[0])

        def is_magic_square(x: int, y: int) -> bool:
            if x + 3 > rows or y + 3 > columns:
                return False

            unique_values = set()
            row_sums = [0] * 3
            column_sums = [0] * 3
            diagonal_sum_left_to_right = 0
            diagonal_sum_right_to_left = 0

            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    value = grid[i][j]

                    # Check if values are unique and within the range 1-9
                    if value < 1 or value > 9:
                        return False
                    unique_values.add(value)

                    # Update sums of rows and columns
                    row_sums[i - x] += value
                    column_sums[j - y] += value

                    # Update diagonal sums
                    if i - x == j - y:
                        diagonal_sum_left_to_right += value
                    if i - x == 2 - (j - y):
                        diagonal_sum_right_to_left += value

            # Check uniqueness of values (magic square has distinct values 1-9)
            if len(unique_values) != 9:
                return False

            # Check the sums of the diagonals, rows, and columns for equality
            if diagonal_sum_left_to_right != diagonal_sum_right_to_left:
                return False
            if any(row_sum != diagonal_sum_left_to_right for row_sum in row_sums):
                return False
            if any(column_sum != diagonal_sum_left_to_right for column_sum in column_sums):
                return False

            # It's a magic square if all checks passed
            return True

        for i in range(rows):
            for j in range(columns):
                magic_squares_count += is_magic_square(i, j)

        return magic_squares_count


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]), 1)
    test(solution.numMagicSquaresInside([[8]]), 0)
