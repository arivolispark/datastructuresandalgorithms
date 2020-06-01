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
        return helper(word1, word2, word1_len, word2_len)


def helper(word1: str, word2: str, word1_len: int, word2_len: int) -> int:
    # If first string is empty, insert all characters of second string into first
    if word1_len == 0:
        return word2_len

    # If second string is empty, remove all characters of first string
    if word2_len == 0:
        return word1_len

    # If last characters of two strings are same, nothing
    # much to do. Ignore last characters and get count for
    # remaining strings.
    if word1[word1_len - 1] == word2[word2_len - 1]:
        return helper(word1, word2, word1_len - 1, word2_len - 1)

    # If last characters are not same, consider all three
    # operations on last character of first string, recursively
    # compute minimum cost for all three operations and take
    # minimum of three values.
    return 1 + min(helper(word1, word2, word1_len, word2_len - 1),  # Insert
                   helper(word1, word2, word1_len - 1, word2_len),  # Remove
                   helper(word1, word2, word1_len - 1, word2_len - 1)  # Replace
                   )


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
    test(solution.minDistance("horse", "ros"), 3)
    test(solution.minDistance("intention", "execution"), 5)
    #test(solution.minDistance("dinitrophenylhydrazine", "benzalphenylhydrazone"), 5)
