"""
Title:  Word Pattern

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in str.



Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true



Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false



Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false



Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false


Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase
letters that may be separated by a single space.

"""


class Solution:

    def wordPattern(self, pattern: str, str: str) -> bool:
        if pattern and str:
            words = str.split(" ")
            words_len = len(words)

            character_word_map = {}

            if words_len != len(pattern):
                return False

            for i in range(words_len):
                if character_word_map.get(pattern[i]):
                    if character_word_map.get(pattern[i]) != words[i]:
                        return False
                else:
                    if words[i] in character_word_map.values():
                        return False
                    else:
                        character_word_map[pattern[i]] = words[i]

            return True
        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.wordPattern("abba", "dog cat cat dog"), True)
    test(solution.wordPattern("abba", "dog cat cat fish"), False)
    test(solution.wordPattern("aaaa", "dog cat cat dog"), False)
    test(solution.wordPattern("abba", "dog dog dog dog"), False)
