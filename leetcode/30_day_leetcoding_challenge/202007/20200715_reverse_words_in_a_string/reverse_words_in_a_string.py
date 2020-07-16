"""
Title:  Reverse Words in a String

Given an input string, reverse the string word by word.


Example 1:
Input: "the sky is blue"
Output: "blue is sky the"


Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.


Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:
1) A word is defined as a sequence of non-space characters.
2) Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
3) You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:
For C programmers, try to solve it in-place in O(1) extra space.

"""


class Solution:

    def reverseWords(self, s: str) -> str:
        result = ""
        if s:
            word_list = s.split(" ")

            reversed_word_list = []
            for i in range(len(word_list) - 1, - 1, -1):
                if word_list[i] is not "":
                    reversed_word_list.append(word_list[i])

            if len(reversed_word_list) > 0:
                result = " ".join(reversed_word_list)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.reverseWords(None), "")
    test(solution.reverseWords(""), "")
    test(solution.reverseWords(" "), "")
    test(solution.reverseWords("     !?    "), "!?")
    test(solution.reverseWords("     !?   ?!   "), "?! !?")
    test(solution.reverseWords("the sky is blue"), "blue is sky the")
    test(solution.reverseWords("  hello world!  "), "world! hello")
    test(solution.reverseWords("a good   example"), "example good a")

