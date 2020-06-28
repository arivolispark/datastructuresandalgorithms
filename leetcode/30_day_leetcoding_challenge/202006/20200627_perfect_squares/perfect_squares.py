"""
Title:  Perfect Squares

Given a positive integer n, find the least number of perfect
square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.


Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""


class Solution:

    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            min_val = i
            temp, sq = 1, 1

            while sq <= i:
                min_val = min(min_val, 1 + dp[i - sq])
                temp += 1
                sq = temp * temp
            dp[i] = min_val
        return dp[n]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.numSquares(6), 3)
    test(solution.numSquares(12), 3)
    test(solution.numSquares(13), 2)
    test(solution.numSquares(100), 1)
