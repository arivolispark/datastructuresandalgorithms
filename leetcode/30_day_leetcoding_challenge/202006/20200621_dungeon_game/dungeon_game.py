"""
Title:  Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner
of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant
knight (K) was initially positioned in the top-left room and must fight his way through
the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point
his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers)
upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that
increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only
rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to
rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if
he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.


===========================
|  -2 (K) | -3	|  3      |
===========================
|  -5	  | -10	|  1      |
===========================
|  10	  | 30	|  -5 (P) |
===========================


Note:
1) The knight's health has no upper bound.
2) Any room can contain threats or power-ups, even the first room the knight enters and the
bottom-right room where the princess is imprisoned.


"""

from typing import List
import math


class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if dungeon:
            rows = len(dungeon)
            if rows:
                columns = len(dungeon[0])
                dp = [[math.inf for _ in range(columns + 1)] for _ in range(rows + 1)]

                dp[rows][columns - 1] = 1
                dp[rows - 1][columns] = 1

                for i in range(rows - 1, -1, -1):
                    for j in range(columns - 1, -1, -1):
                        min_health_point = min(dp[i][j + 1], dp[i + 1][j]) - dungeon[i][j]
                        if min_health_point < 1:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = min_health_point
                return dp[0][0]


def get_test_case_1_input() -> List[List[int]]:
    dungeon = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    return dungeon


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.calculateMinimumHP(get_test_case_1_input()), 7)
