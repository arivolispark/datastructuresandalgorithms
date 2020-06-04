"""
Title:  Reverse String

Write a function that reverses a string. The input string
is given as an array of characters char[].

Do not allocate extra space for another array, you must do
this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


"""

from typing import List


class Solution:

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        if s:
            start, end = 0, len(s) - 1
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    testcase_inputs = [
        ["h", "e", "l", "l", "o"],
        ["H", "a", "n", "n", "a", "h"]
    ]

    testcase_outputs = [
        ["o", "l", "l", "e", "h"],
        ["h", "a", "n", "n", "a", "H"]
    ]

    for i in range(len(testcase_inputs)):
        solution.reverseString(testcase_inputs[i])
     
    for i in range(len(testcase_inputs)):
        test(testcase_inputs[i], testcase_outputs[i])
