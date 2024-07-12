"""
Title:  1717. Maximum Score From Removing Substrings

You are given a string s and two integers x and y. You can perform two types of
operations any number of times.

1) Remove substring "ab" and gain x points.
  -  For example, when removing "ab" from "cabxbae" it becomes "cxbae".
2) Remove substring "ba" and gain y points.
  -  For example, when removing "ba" from "cabxbae" it becomes "cabxe".

Return the maximum points you can gain after applying the above operations on s.



Example 1:
Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.


Example 2:
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20


Constraints:
1) 1 <= s.length <= 10^5
2) 1 <= x, y <= 10^4
3) s consists of lowercase English letters.

"""

from typing import List


class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:
        gain = 0

        stack = []
        if x > y:
            for c in s:
                stack.append(c)

                while len(stack) >= 2:
                    if stack[-2] == "a" and stack[-1] == "b":
                        stack.pop()
                        stack.pop()

                        gain += x
                    else:
                        break
        else:
            for c in s:
                stack.append(c)

                while len(stack) >= 2:
                    if stack[-2] == "b" and stack[-1] == "a":
                        stack.pop()
                        stack.pop()

                        gain += y
                    else:
                        break

        stack2 = []
        for c in stack:
            stack2.append(c)

            while len(stack2) >= 2:
                if stack2[-2] == "a" and stack2[-1] == "b":
                    stack2.pop()
                    stack2.pop()

                    gain += x
                elif stack2[-2] == "b" and stack2[-1] == "a":
                    stack2.pop()
                    stack2.pop()

                    gain += y
                else:
                    break

        return gain


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.maximumGain("cdbcbbaaabab", 4, 5), 19)
    test(solution.maximumGain("aabbaaxybbaabb", 5, 4), 20)
