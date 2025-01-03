"""
Title:  1422. Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into
two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number
of ones in the right substring.



Example 1:
Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3


Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5


Example 3:
Input: s = "1111"
Output: 3


Constraints:
1) 2 <= s.length <= 500
2) The string s consists of characters '0' and '1' only.

"""

import math


class Solution:

    def maxScore(self, s: str) -> int:
        result = -math.inf
        zeros_map, ones_map = {}, {}
        length = len(s)

        if s[0] == "0":
            zeros_map[0] = 1
        else:
            zeros_map[0] = 0

        for i in range(1, length - 1):
            if s[i] == "0":
                zeros_map[i] = zeros_map[i - 1] + 1
            else:
                zeros_map[i] = zeros_map[i - 1]
        #print(" zeros_map: ", zeros_map)

        if s[length - 1] == "1":
            ones_map[length - 1] = 1
        else:
            ones_map[length - 1] = 0

        for i in range(length - 2, 0, -1):
            if s[i] == "1":
                ones_map[i] = ones_map[i + 1] + 1
            else:
                ones_map[i] = ones_map[i + 1]
        #print(" ones_map: ", ones_map)

        for i in range(length - 1):
            result = max(result, zeros_map[i] + ones_map[i + 1])

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxScore("011101"), 5)
    test(solution.maxScore("00111"), 5)
    test(solution.maxScore("1111"), 3)
