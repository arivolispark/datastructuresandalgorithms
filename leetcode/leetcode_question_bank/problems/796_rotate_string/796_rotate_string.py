"""
Title:  796. Rotate String

Given two strings s and goal, return true if and only if s can become goal after
some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.



Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true


Example 2:
Input: s = "abcde", goal = "abced"
Output: false


Constraints:
1) 1 <= s.length, goal.length <= 100
3) s and goal consist of lowercase English letters.

"""

from typing import List


class Solution:

    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        for i in range(len(s)):
            if s[i+1:] + s[:i+1] == goal:
                return True
        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.rotateString("abcde", "cdeab"), True)
    test(solution.rotateString("abcde", "abced"), False)
