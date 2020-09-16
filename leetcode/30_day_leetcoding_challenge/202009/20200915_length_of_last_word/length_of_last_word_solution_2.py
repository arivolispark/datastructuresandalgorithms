"""
Title:  Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word (last word means the last
appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters
only.


Example:
Input: "Hello World"
Output: 5

"""


class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(" ")[-1])


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.lengthOfLastWord("Hello World"), 5)
    test(solution.lengthOfLastWord("a "), 1)
    test(solution.lengthOfLastWord(" a"), 1)
    test(solution.lengthOfLastWord(" a "), 1)
