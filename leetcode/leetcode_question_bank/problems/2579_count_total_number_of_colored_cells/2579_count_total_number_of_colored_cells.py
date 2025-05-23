"""
Title:  2579. Count Total Number of Colored Cells

There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given
a positive integer n, indicating that you must do the following routine for n minutes:

1) At the first minute, color any arbitrary unit cell blue.
2) Every minute thereafter, color blue every uncolored cell that touches a blue cell.

Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.


Return the number of colored cells at the end of n minutes.



Example 1:
Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:


Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5.


Constraints:
1) 1 <= n <= 10^5

"""

from typing import List


class Solution:

    def coloredCells(self, n: int) -> int:
        map = {}

        map[1] = 1

        for i in range(2, n + 1):
            map[i] = map[i - 1] + ((i - 1) * 4)

        return map[n]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.coloredCells(1), 1)
    test(solution.coloredCells(2), 5)
    test(solution.coloredCells(3), 13)
