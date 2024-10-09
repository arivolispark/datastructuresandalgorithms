"""
Title:  921. Minimum Add to Make Parentheses Valid

A parentheses string is valid if and only if:

1) It is the empty string,
2) It can be written as AB (A concatenated with B), where A and B are valid strings, or
3) It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at
any position of the string.
1) For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or
a closing parenthesis to be "())))".

Return the minimum number of moves required to make s valid.



Example 1:
Input: s = "())"
Output: 1


Example 2:
Input: s = "((("
Output: 3


Constraints:
1) 1 <= s.length <= 1000
2) s[i] is either '(' or ')'.

"""


class Solution:

    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for c in s:
            if c == ")" and stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(c)
        return len(stack)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.minAddToMakeValid("())"), 1)
    test(solution.minAddToMakeValid("((("), 3)
    test(solution.minAddToMakeValid("()))(("), 4)
