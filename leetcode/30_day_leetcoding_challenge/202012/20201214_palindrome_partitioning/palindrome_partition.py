
"""
Title:  Palindrome Partition

Given a string s, partition s such that every substring of the partition is 
a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]



Example 2:
Input: s = "a"
Output: [["a"]]

 

Constraints:

1) 1 <= s.length <= 16
2) s contains only lowercase English letters.

"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
       
        result = []
        for i in range(len(s)):
            if self.is_palindrome(s[:i + 1]):
                for r in self.partition(s[i + 1:]):
                    result.append([s[:i + 1]] + r)
        return result

    def is_palindrome(self, s):
        return s == s[::-1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.partition("aab"), [["a","a","b"],["aa","b"]])
