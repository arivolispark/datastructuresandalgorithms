"""
Title:  131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.



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
        length = len(s)
        result = []

        def construct(index, current):
            if index == length:
                result.append(current[:])
                return

            for end in range(index, length):
                if s[index:end + 1] == s[index:end + 1][::-1]:
                    current.append(s[index:end + 1])
                    construct(end + 1, current)
                    current.pop()

        construct(0, [])
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.partition("aab"), [["a","a","b"],["aa","b"]])
    test(solution.partition("a"), [["a"]])
