"""
Title:  Perform String Shifts

You are given a string s containing lowercase English letters, and
a matrix shift, where shift[i] = [direction, amount]:

1) direction can be 0 (for left shift) or 1 (for right shift).
2) amount is the amount by which string s is to be shifted.
3) A left shift by 1 means remove the first character of s and append it to the end.
4) Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.


Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

Example 2:
Input: s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
Output: "efgabcd"
Explanation:
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"


Constraints:
1) 1 <= s.length <= 100
2) s only contains lower case English letters.
3) 1 <= shift.length <= 100
4) shift[i].length == 2
5) 0 <= shift[i][0] <= 1
6) 0 <= shift[i][1] <= 100
"""

from typing import List


class Solution:

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(shift)
        amount_sum = 0
        for i in range(n):
            direction, amount = shift[i]
            if direction == 0:
                amount_sum -= amount
            elif direction == 1:
                amount_sum += amount

        if amount_sum > 0:
            amount_sum %= len(s)
        elif amount_sum < 0:
            amount_sum = -(abs(amount_sum) % len(s))
        print("\n amount_sum: ", amount_sum)

        if amount_sum > 0:
            first_part = s[:len(s) - amount_sum]
            second_part = s[len(s) - amount_sum:]

            return second_part + first_part
        elif amount_sum < 0:
            first_part = s[:abs(amount_sum)]
            second_part = s[abs(amount_sum):]

            return second_part + first_part
        return s


def get_test_case_1():
    s = "abc"
    shift = [[0, 1], [1, 2]]
    return s, shift


def get_test_case_2():
    s = "abcdefg"
    shift = [[1, 1], [1, 1], [0, 2], [1, 3]]
    return s, shift


def get_test_case_3():
    s = "abcdefg"
    shift = [[1, 1], [1, 1], [0, 2], [0, 2]]
    return s, shift


def get_test_case_4() -> List[int]:
    s = "wpdhhcj"
    shift = [[0, 7], [1, 7], [1, 0], [1, 3], [0, 3], [0, 6], [1, 2]]
    return s, shift


def get_test_case_5() -> List[int]:
    s = "xqgwkiqpif"
    shift = [[1, 4], [0, 7], [0, 8], [0, 7], [0, 6], [1, 3], [0, 1], [1, 7], [0, 5], [0, 6]]
    return s, shift


if __name__ == "__main__":
    solution = Solution()

    #s, shift = get_test_case_1()
    #s, shift = get_test_case_2()
    #s, shift = get_test_case_3()
    #s, shift = get_test_case_4()
    s, shift = get_test_case_5()

    print("\n s: ", s)
    print(" shift: ", shift)

    shifted_string = solution.stringShift(s, shift)
    print("\n shifted_string: ", shifted_string)
