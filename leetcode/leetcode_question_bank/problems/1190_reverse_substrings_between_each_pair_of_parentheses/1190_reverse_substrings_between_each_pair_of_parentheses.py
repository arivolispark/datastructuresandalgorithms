"""
Title:  1190. Reverse Substrings Between Each Pair of Parentheses

You are given a string s that consists of lower case English letters and brackets.
Reverse the strings in each pair of matching parentheses, starting from the innermost one.
Your result should not contain any brackets.



Example 1:
Input: s = "(abcd)"
Output: "dcba"


Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.


Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


Constraints:
1) 1 <= s.length <= 2000
2) s only contains lower case English characters and parentheses.
3) It is guaranteed that all parentheses are balanced.

"""

from typing import List
from collections import Counter
import math

class Solution:

    def reverseParentheses(self, s: str) -> str:
        result = []

        for i in range(len(s)):
            if s[i] == ")":
                temp = []
                while True:
                    val = result.pop()
                    if val != "(":
                        temp.append(val)
                    else:
                        for j in range(len(temp)):
                            result.append(temp[j])
                        break
            else:
                result.append(s[i])

        return "".join(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.reverseParentheses("(abcd)"), "dcba")
    test(solution.reverseParentheses("(u(love)i)"), "iloveu")
    test(solution.reverseParentheses("(ed(et(oc))el)"), "leetcode")
