"""
Title:  Palindrome Permutation

Given a string, determine if a permutation of the string could form a palindrome.



Example 1:
Input: "code"
Output: false



Example 2:
Input: "aab"
Output: true



Example 3:
Input: "carerac"
Output: true

"""


class Solution:

    def canPermutePalindrome(self, s: str) -> bool:
        if s:
            char_freq_map = {}
            number_of_odd_chars = 0
            for i in range(len(s)):
                char_freq_map[s[i]] = char_freq_map.get(s[i], 0) + 1

            for k, v in char_freq_map.items():
                if v % 2 == 1:
                    number_of_odd_chars += 1
                    if number_of_odd_chars > 1:
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

    test(solution.canPermutePalindrome("code"), False)
    test(solution.canPermutePalindrome("aab"), True)
    test(solution.canPermutePalindrome("carerac"), True)
