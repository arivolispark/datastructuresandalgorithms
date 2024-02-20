"""
Title:  345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


Example 1:
Input: s = "hello"
Output: "holle"


Example 2:
Input: s = "leetcode"
Output: "leotcede"


Constraints:
1) 1 <= s.length <= 3 * 105
2) s consist of printable ASCII characters.

"""


class Solution:

    def reverseVowels(self, s: str) -> str:
        char_list, vowel_list = [], []
        for c in s:
            char_list.append(c)
            if is_vowel(c):
                vowel_list.append(c)

        vowel_list = vowel_list[::-1]

        j = 0
        for i in range(len(char_list)):
            if is_vowel(char_list[i]):
                char_list[i] = vowel_list[j]
                j += 1

        return ''.join(char_list)


def is_vowel(c: str):
    return True if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U' else False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.reverseVowels("hello"), "holle")
    test(solution.reverseVowels("leetcode"), "leotcede")
