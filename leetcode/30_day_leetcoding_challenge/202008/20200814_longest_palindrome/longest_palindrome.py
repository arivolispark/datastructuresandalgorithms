"""
Title:  Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the
length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""


class Solution:

    def longestPalindrome(self, s: str) -> int:
        result = 0
        char_frequency_map = {}
        has_odd_length = False

        if s:
            for i in range(len(s)):
                char_frequency_map[s[i]] = char_frequency_map.get(s[i], 0) + 1

            for k, v in char_frequency_map.items():
                if v % 2 == 0:
                    result += v
                else:
                    has_odd_length = True
                    result += v - 1

            if has_odd_length:
                result += 1
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.longestPalindrome("abccccdd"), 7)
