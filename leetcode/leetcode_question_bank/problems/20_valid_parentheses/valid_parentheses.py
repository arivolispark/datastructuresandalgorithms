"""
Problem #: 20
Title:  Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1) Open brackets must be closed by the same type of brackets.
2) Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true


Example 2:
Input: "()[]{}"
Output: true


Example 3:
Input: "(]"
Output: false


Example 4:
Input: "([)]"
Output: false


Example 5:
Input: "{[]}"
Output: true
"""


from collections import deque


class Solution:

    def isValid(self, s: str) -> bool:
        if s:
            q = deque()

            for i in range(len(s)):
                if s[i] == "(" or s[i] == "{" or s[i] == "[":
                    q.append(s[i])
                elif s[i] == ")":
                    #print(len(q))
                    if len(q) == 0:
                        return False
                    elif q[-1] == "(":
                        q.pop()
                    else:
                        q.append(s[i])
                elif s[i] == "}":
                    #print(len(q))
                    if len(q) == 0:
                        return False
                    elif q[-1] == "{":
                        q.pop()
                    else:
                        q.append(s[i])
                elif s[i] == "]":
                    #print(len(q))
                    if len(q) == 0:
                        return False
                    elif q[-1] == "[":
                        q.pop()
                    else:
                        q.append(s[i])

            if len(q) == 0:
                return True
            else:
                return False
        return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isValid("()"), True)
    test(solution.isValid("()[]{}"), True)
    test(solution.isValid("(]"), False)
    test(solution.isValid("([)]"), False)
    test(solution.isValid("{[]}"), True)
    test(solution.isValid("]"), False)
    test(solution.isValid("(])"), False)
