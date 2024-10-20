"""
Title: 1106. Parsing A Boolean Expression

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:

1) 't' that evaluates to true.
2) 'f' that evaluates to false.
3) '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
4) '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1,
subExpr2, ..., subExprn where n >= 1.
5) '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1,
subExpr2, ..., subExprn where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.

It is guaranteed that the given expression is valid and follows the given rules.



Example 1:
Input: expression = "&(|(f))"
Output: false
Explanation:
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.


Example 2:
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.


Example 3:
Input: expression = "!(&(f,t))"
Output: true
Explanation:
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.


Constraints:
1) 1 <= expression.length <= 2 * 104
2) expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

"""

from typing import List
import functools
import operator


class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        def dfs(s: int, e: int) -> list[str]:
            if s == e:
                return True if expression[s] == 't' else False

            exps = []
            layer = 0

            for i in range(s, e + 1):
                c = expression[i]
                if layer == 0 and c in '!&|':
                    op = c
                elif c == '(':
                    layer += 1
                    if layer == 1:
                        left = i + 1
                elif c == ')':
                    layer -= 1
                    if layer == 0:
                        exps.append(dfs(left, i - 1))
                elif c == ',' and layer == 1:
                    exps.append(dfs(left, i - 1))
                    left = i + 1

            if op == '|':
                return functools.reduce(operator.or_, exps)
            if op == '&':
                return functools.reduce(operator.and_, exps)
            if op == '!':
                return not exps[0]

        return dfs(0, len(expression) - 1)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.parseBoolExpr("&(|(f))"), False)
    test(solution.parseBoolExpr("|(f,f,f,t)"), True)
    test(solution.parseBoolExpr("!(&(f,t))"), True)
