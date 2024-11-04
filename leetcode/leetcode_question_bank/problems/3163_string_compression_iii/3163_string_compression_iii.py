"""
Title:  3163. String Compression III

Given a string word, compress it using the following algorithm:

Begin with an empty string comp. While word is not empty, use the following operation:
Remove a maximum length prefix of word made of a single character c repeating at most 9 times.
Append the length of the prefix followed by c to comp.
Return the string comp.



Example 1:
Input: word = "abcde"
Output: "1a1b1c1d1e"
Explanation:
Initially, comp = "". Apply the operation 5 times, choosing "a", "b", "c", "d", and "e" as the prefix in each operation.
For each prefix, append "1" followed by the character to comp.


Example 2:
Input: word = "aaaaaaaaaaaaaabb"
Output: "9a5a2b"
Explanation:
Initially, comp = "". Apply the operation 3 times, choosing "aaaaaaaaa", "aaaaa", and "bb" as the prefix in each operation.
For prefix "aaaaaaaaa", append "9" followed by "a" to comp.
For prefix "aaaaa", append "5" followed by "a" to comp.
For prefix "bb", append "2" followed by "b" to comp.


Constraints:
1) 1 <= word.length <= 2 * 10^5
2) word consists only of lowercase English letters.

"""

class Solution:

    def compressedString(self, word: str) -> str:
        result = ""
        current_char = word[0]
        current_char_count = 1

        for i in range(1, len(word)):
            if word[i] != current_char:
                result += str(current_char_count) + current_char
                current_char = word[i]
                current_char_count = 1
            else:
                current_char_count += 1
                if current_char_count == 10:
                    current_char_count -= 1
                    result += str(current_char_count) + current_char
                    current_char_count = 1
        result += str(current_char_count) + current_char
        return result

    def compressedString_1(self, word: str) -> str:
        result = []
        current_char = word[0]
        current_char_count = 1

        for i in range(1, len(word)):
            if word[i] != current_char:
                result.append(str(current_char_count))
                result.append(current_char)

                current_char = word[i]
                current_char_count = 1
            else:
                current_char_count += 1
                if current_char_count == 10:
                    current_char_count -= 1
                    result.append(str(current_char_count))
                    result.append(current_char)
                    current_char_count = 1

        result.append(str(current_char_count))
        result.append(current_char)

        return ''.join(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test((solution.compressedString("abcde")), "1a1b1c1d1e")
    test((solution.compressedString("aaaaaaaaaaaaaabb")), "9a5a2b")
    test((solution.compressedString("mrm")), "1m1r1m")
