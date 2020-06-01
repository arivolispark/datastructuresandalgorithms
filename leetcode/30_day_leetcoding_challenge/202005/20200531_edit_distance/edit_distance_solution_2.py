"""
Title:  Edit Distance

Given two words word1 and word2, find the minimum number of
operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

1) Insert a character
2) Delete a character
3) Replace a character


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')


Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)

        dp = [[0 for _ in range(word2_len + 1)] for _ in range(word1_len + 1)]

        for i in range(word1_len + 1):
            for j in range(word2_len + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],
                                       dp[i - 1][j],
                                       dp[i - 1][j - 1])
        #print("\n dp: ", dp)
        return dp[word1_len][word2_len]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.minDistance("abcdef", "abcdef"), 0)
    test(solution.minDistance("", "aeiou"), 5)
    test(solution.minDistance("USA", ""), 3)
    test(solution.minDistance("abcdef", "abcdeg"), 1)
    test(solution.minDistance("ab", "xy"), 2)
    test(solution.minDistance("horse", "ros"), 3)
    test(solution.minDistance("intention", "execution"), 5)
    test(solution.minDistance("dinitrophenylhydrazine", "benzalphenylhydrazone"), 7)
