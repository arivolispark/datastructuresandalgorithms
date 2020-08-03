"""
Title:  Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1) All letters in this word are capitals, like "USA".
2) All letters in this word are not capitals, like "leetcode".
3) Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.



Example 1:
Input: "USA"
Output: True


Example 2:
Input: "FlaG"
Output: False


Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

"""


class Solution:

    def detectCapitalUse(self, word: str) -> bool:
        if word:
            word_len = len(word)
            if word_len == 1:
                return True

            uppercase_letters_set = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
            lowercase_letters_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

            if word_len == 2:
                if word[0] in lowercase_letters_set:
                    if word[1] in uppercase_letters_set:
                        return False
                    elif word[1] in lowercase_letters_set:
                        return True
                else:
                    return True

            if word[0] in lowercase_letters_set:
                for i in range(1, word_len):
                    if word[i] in uppercase_letters_set:
                        return False
                return True
            elif word[0] in uppercase_letters_set:
                if word[1] in uppercase_letters_set:
                    for i in range(2, word_len):
                        if word[i] in lowercase_letters_set:
                            return False
                    return True
                elif word[1] in lowercase_letters_set:
                    for i in range(2, word_len):
                        if word[i] in uppercase_letters_set:
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

    test(solution.detectCapitalUse("USA"), True)
    test(solution.detectCapitalUse("FlaG"), False)
    test(solution.detectCapitalUse("leetcode"), True)
    test(solution.detectCapitalUse("Google"), True)
    test(solution.detectCapitalUse("G"), True)
    test(solution.detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"), False)
