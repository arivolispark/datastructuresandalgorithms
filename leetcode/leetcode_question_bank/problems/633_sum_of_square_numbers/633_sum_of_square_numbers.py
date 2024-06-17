"""
Title:  633. Sum of Square Numbers

Given a non-negative integer c, decide whether there're two
integers a and b such that a2 + b2 = c.



Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5


Example 2:
Input: c = 3
Output: false


Constraints:
1) 0 <= c <= 2^31 - 1

"""

import math

class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        list_1 = []
        a = math.floor(math.sqrt(c))

        for i in range(a + 1):
            list_1.append(i ** 2)

        i, j = 0, len(list_1) - 1
        while i <= j:
            if list_1[i] + list_1[j] == c:
                return True
            elif list_1[i] + list_1[j] < c:
                i += 1
            elif list_1[i] + list_1[j] > c:
                j -= 1

        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == '__main__':
    solution = Solution()

    test(solution.judgeSquareSum(5), True)
    test(solution.judgeSquareSum(3), False)
    test(solution.judgeSquareSum(2), True)
