"""
Title: Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the
price  of a given stock on day i.

If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.



Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.



Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""


from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        buying_price, result = 0, 0
        if prices:
            buying_price = prices[0]
            for i in range(1, len(prices)):
                if prices[i] < buying_price:
                    buying_price = prices[i]
                else:
                    result = max(prices[i] - buying_price, result)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxProfit([7,1,5,3,6,4]), 5)
    test(solution.maxProfit([7,6,4,3,1]), 0)
    test(solution.maxProfit([]), 0)
    test(solution.maxProfit([2,4,1]), 2)
