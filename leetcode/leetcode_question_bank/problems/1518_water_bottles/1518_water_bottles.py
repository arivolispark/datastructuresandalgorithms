"""
Title:  1518. Water Bottles

There are numBottles water bottles that are initially full of water. You can
exchange numExchange empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers numBottles and numExchange, return the maximum number of water
bottles you can drink.



Example 1:
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.


Example 2:
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 15 + 3 + 1 = 19.


Constraints:
1) 1 <= numBottles <= 100
2) 2 <= numExchange <= 100

"""

from typing import List


class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = 0

        total += numBottles
        empty = numBottles

        while empty >= numExchange:
            empty, remainder = (empty // numExchange), (empty % numExchange)
            total += empty
            empty += remainder

        return total


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.numWaterBottles(9, 3), 13)
    test(solution.numWaterBottles(15, 4), 19)
    test(solution.numWaterBottles(15, 8), 17)
