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


class Solution:

    def isPalindrome(self, s: str) -> bool:
        if s:
            s_len = len(s)
            modified_str = []
            for i in range(s_len):
                if 48 <= ord(s[i]) <= 57:
                    modified_str.append(ord(s[i]))
                elif 65 <= ord(s[i]) <= 90:
                    modified_str.append(ord(s[i]) + 32)
                elif 97 <= ord(s[i]) <= 122:
                    modified_str.append(ord(s[i]))

            #print(" modified_str: ", modified_str)
            start, end = 0, len(modified_str) - 1
            while start <= end:
                if modified_str[start] != modified_str[end]:
                    return False
                start += 1
                end -= 1
            return True
        else:
            return True


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

