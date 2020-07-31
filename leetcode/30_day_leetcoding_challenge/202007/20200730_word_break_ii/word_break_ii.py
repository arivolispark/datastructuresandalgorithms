"""
Title:  Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word
is a valid dictionary word. Return all such possible sentences.

Note:
1) The same word in the dictionary may be reused multiple times in the segmentation.
2) You may assume the dictionary does not contain duplicate words.



Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]



Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.



Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""

from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}

        def word_break(s):
            if s in dp:
                return dp[s]

            result = []
            for w in wordDict:
                if s[:len(w)] == w:
                    if len(w) == len(s):
                        result.append(w)
                    else:
                        tmp = word_break(s[len(w):])
                        for t in tmp:
                            result.append(w + " " + t)
            dp[s] = result
            return result
        return word_break(s)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"])
    test(solution.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]), ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    test(solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), [])



