"""
Problem #: 121
Title:  Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one
share of the stock), design an algorithm to find the maximum profit.

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
from collections import deque


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        stock_prices = deque()
        max_profit = 0

        for price in prices:
            if len(stock_prices) == 0:
                stock_prices.append(price)
            else:
                if price < stock_prices[-1]:
                    stock_prices.pop()
                    stock_prices.append(price)
                else:
                    profit = price - stock_prices[-1]
                    if profit > max_profit:
                        max_profit = profit
        return max_profit


if __name__ == "__main__":
    solution = Solution()

    #prices = [7, 1, 5, 3, 6, 4]
    prices = [2, 1, 2, 1, 0, 1, 2]
    print("\n prices: ", prices)

    max_profit = solution.maxProfit(prices)
    print("\n max_profit: ", max_profit)
