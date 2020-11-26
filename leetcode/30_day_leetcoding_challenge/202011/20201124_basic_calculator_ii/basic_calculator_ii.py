"""
Title:  Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and 
empty spaces . The integer division should truncate toward zero.



Example 1:
Input: "3+2*2"
Output: 7



Example 2:
Input: " 3/2 "
Output: 1



Example 3:
Input: " 3+5 / 2 "
Output: 5


Note:

1) You may assume that the given expression is always valid.
2) Do not use the eval built-in library function.

"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        num = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num*10+int(c)
            if i + 1 == len(s) or (c == '+' or c == '-' or c == '*' or c == '/'):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1]*num
                elif sign == '/':
                    stack[-1] = int(stack[-1]/float(num))
                sign = c
                num = 0
        return sum(stack)
        
