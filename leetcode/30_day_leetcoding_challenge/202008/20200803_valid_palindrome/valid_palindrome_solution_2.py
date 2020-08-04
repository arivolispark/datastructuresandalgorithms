"""
Title:  Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.


Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true


Example 2:
Input: "race a car"
Output: false


Constraints:
1) s consists only of printable ASCII characters.

"""

import re


class Solution:

    def isPalindrome(self, s: str) -> bool:
        s = "".join(re.findall("[a-zA-Z0-9]", s)).upper()
        return s == s[::-1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.isPalindrome("A man, a plan, a canal: Panama"), True)
    test(solution.isPalindrome("race a car"), False)
    test(solution.isPalindrome(""), True)
    test(solution.isPalindrome("Marge, let's \"[went].\" I await {news} telegram."), True)

