"""
Title:  Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price
of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete
as many transactions as you like (ie, buy one and sell one share
of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day.
(ie, cooldown 1 day)


Example:
Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

"""

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        state_a, state_b, state_c = 0, -prices[0], 0
        for i in range(1, len(prices)):
            temp = state_a
            state_a = max(state_a, state_c)
            state_c = state_b + prices[i]
            state_b = max(state_b, temp - prices[i])

        return max(state_a, state_c)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxProfit([1,2,3,0,2]), 3)
