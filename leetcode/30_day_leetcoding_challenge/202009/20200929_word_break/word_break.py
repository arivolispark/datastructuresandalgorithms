"""
Title:  Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine
if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
1) The same word in the dictionary may be reused multiple times in the segmentation.
2) You may assume the dictionary does not contain duplicate words.



Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".



Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.



Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""


class Solution:

    ### DP? O(n^2)
    # cut(i) = s[:i] can be splitted
    # cut(i+1) = OR{cut(j) and s[j:i] is a word for 0 <= j < i}
    def wordBreak(self, s, words):
        words = set(words)
        cut = {0: True}
        for i in range(1, len(s) + 1):
            cut[i] = False
            for j in range(i):
                if cut[j] and s[j:i] in words:
                    cut[i] = True
                    break
        return cut[len(s)]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    # test(solution.wordBreak("leetcode", ["leet", "code"]), True)
    # test(solution.wordBreak("applepenapple", ["apple", "pen"]), True)
    # test(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)

    test(solution.wordBreak("leetcode", ["leet", "code"]), True)
    test(solution.wordBreak("applepenapple", ["apple", "pen"]), True)
    test(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), False)
