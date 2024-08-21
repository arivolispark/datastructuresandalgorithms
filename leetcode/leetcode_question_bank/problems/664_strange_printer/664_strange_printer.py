"""
Title:  664. Strange Printer

There is a strange printer with the following two special properties:

1) The printer can only print a sequence of the same character each time.
2) At each turn, the printer can print new characters starting from and ending at any place and will
cover the original existing characters.

Given a string s, return the minimum number of turns the printer needed to print it.



Example 1:
Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".


Example 2:
Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover
the existing character 'a'.


Constraints:
1) 1 <= s.length <= 100
2) s consists of lowercase English letters.

"""
import sys


class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)

        dp = [[sys.maxsize] * length for _ in range(length)]

        for i in range(length):
            dp[i][i] = 1

        for l in range(2, length + 1):
            for i in range(length - l + 1):
                j = i + l - 1

                # print ith letter separately
                dp[i][j] = dp[i + 1][j] + 1

                for k in range(i + 1, j + 1):
                    if s[i] == s[k]:
                        if j > k:
                            dp[i][j] = min(dp[i][j], dp[i][k - 1] + dp[k + 1][j])
                        else:
                            dp[i][j] = min(dp[i][j], dp[i][k - 1])

        return dp[0][length - 1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.strangePrinter("aaabbb"), 2)
    test(solution.strangePrinter("aba"), 2)
    test(solution.strangePrinter(""), 0)
