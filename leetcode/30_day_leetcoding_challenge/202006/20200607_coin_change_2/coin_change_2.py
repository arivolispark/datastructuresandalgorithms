"""
Title:  Coin Change 2

You are given coins of different denominations and a total amount
of money. Write a function to compute the number of combinations
that make up that amount. You may assume that you have infinite
number of each kind of coin.


Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1


Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.


Example 3:
Input: amount = 10, coins = [10]
Output: 1


Note:

You can assume that
1) 0 <= amount <= 5000
2) 1 <= coin <= 5000
3) the number of coins is less than 500
4) the answer is guaranteed to fit into signed 32-bit integer
"""

from typing import List


class Solution:

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        #print("\n dp: ", dp)

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[amount]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.change(5, [1, 2, 5]), 4)
    test(solution.change(3, [2]), 0)
    test(solution.change(10, [10]), 1)
