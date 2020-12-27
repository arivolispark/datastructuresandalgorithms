
"""
Title:  Next Greater Element III

Given a positive integer n, find the smallest integer which has exactly the
same digits existing in the integer n and is greater in value than n. If no such
positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid
answer but it does not fit in 32-bit integer, return -1.



Example 1:
Input: n = 12
Output: 21



Example 2:
Input: n = 21
Output: -1



Constraints:

1) 1 <= n <= 2^31 - 1

"""

from typing import List


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        result = -1

        temp_val = n
        digits = list()
        numbers_permutation = set()

        while temp_val > 0:
            digit = temp_val % 10
            digits.append(str(digit))
            temp_val //= 10
        #print(" digits: ", digits)

        digits_len = len(digits)
        permute(n, digits, 0, digits_len - 1, numbers_permutation)
        #print(" numbers_permutation: ", numbers_permutation)

        sorted_numbers_permutation = sorted(numbers_permutation)
        #print(" sorted_numbers_permutation: ", sorted_numbers_permutation)

        for i in range(len(sorted_numbers_permutation)):
            if sorted_numbers_permutation[i] > n:
                result = sorted_numbers_permutation[i]
                break

        return -1 if result > 2147483647 else result


def permute(n: int, input: List[str], start: int, end: int, numbers_permutation):
    if start == end:
        s = "".join(input)
        val = int(s)
        if val > n:
            numbers_permutation.add(val)
    else:
        for i in range(start, end + 1):
            input[start], input[i] = input[i], input[start]
            permute(n, input, start + 1, end, numbers_permutation)
            input[start], input[i] = input[i], input[start]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.nextGreaterElement(12), 21)
    test(solution.nextGreaterElement(21), -1)
    test(solution.nextGreaterElement(1999999999), -1)
