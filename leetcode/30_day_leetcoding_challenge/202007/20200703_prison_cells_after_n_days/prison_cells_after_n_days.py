"""
Title:  Prison Cells After N Days

There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the
following rules:

1) If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
2) Otherwise, it becomes vacant.

(Note that because the prison is a row, the first and the last cells in the
row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if
the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days
(and N such changes described above.)



Example 1:
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]


Example 2:
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]


Note:
1) cells.length == 8
2) cells[i] is in {0, 1}
3) 1 <= N <= 10^9

"""

from typing import List


class Solution:

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N <= 0:
            return cells

        number_of_days = (N - 1) % 14 + 1
        number_of_cells = len(cells)

        while number_of_days > 0:
            temp_list = list()

            for i in range(number_of_cells):
                if i == 0 or i == number_of_cells - 1:
                    temp_list.insert(i, 0)
                else:
                    if cells[i - 1] == cells[i + 1]:
                        temp_list.insert(i, 1)
                    else:
                        temp_list.insert(i, 0)

            cells = temp_list
            number_of_days -= 1
        return cells


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 0), [0,1,0,1,1,0,0,1])
    test(solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 1), [0,1,1,0,0,0,0,0])
    test(solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 2), [0,0,0,0,1,1,1,0])
    test(solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 3), [0,1,1,0,0,1,0,0])
    test(solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 4), [0,0,0,0,0,1,0,0])
    test(solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 5), [0,1,1,1,0,1,0,0])
    test(solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 6), [0,0,1,0,1,1,0,0])
    test(solution.prisonAfterNDays([0,1,0,1,1,0,0,1], 7), [0,0,1,1,0,0,0,0])
    test(solution.prisonAfterNDays([1,0,0,1,0,0,0,1], 826), [0,1,1,0,1,1,1,0])
    test(solution.prisonAfterNDays([1,0,0,1,0,0,1,0], 1000000000), [0,0,1,1,1,1,1,0])
