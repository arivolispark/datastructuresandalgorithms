"""
Title:  Unique Paths

A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point
in time. The robot is trying to reach the bottom-right corner
of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?



Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right


Example 2:
Input: m = 7, n = 3
Output: 28


Constraints:
1) 1 <= m, n <= 100
2) It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.

"""


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        if m == n == 1:
            return 1

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m - 1):
            dp[i][n - 1] = 1
        for j in range(n - 1):
            dp[m - 1][j] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        #print("\n dp: ", dp)

        return dp[0][0]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.uniquePaths(1, 1), 1)
    test(solution.uniquePaths(2, 1), 1)
    test(solution.uniquePaths(1, 2), 1)
    test(solution.uniquePaths(2, 2), 2)
    test(solution.uniquePaths(2, 3), 3)
    test(solution.uniquePaths(3, 2), 3)
    test(solution.uniquePaths(3, 3), 6)
    test(solution.uniquePaths(2, 4), 4)
    test(solution.uniquePaths(4, 2), 4)
    test(solution.uniquePaths(3, 4), 10)
    test(solution.uniquePaths(4, 3), 10)
    test(solution.uniquePaths(4, 4), 20)
    test(solution.uniquePaths(7, 3), 28)
