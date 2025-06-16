"""
Title:  1432. Max Difference You Can Get From Changing an Integer

You are given an integer num. You will apply the following steps to num two separate times:

1) Pick a digit x (0 <= x <= 9).
2) Pick another digit y (0 <= y <= 9). Note y can be equal to x.
3) Replace all the occurrences of x in the decimal representation of num by y.

Let a and b be the two results from applying the operation to num independently.

Return the max difference between a and b.

Note that neither a nor b may have any leading zeros, and must not be 0.



Example 1:
Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888



Example 2:
Input: num = 9
Output: 8
Explanation: The first time pick x = 9 and y = 9 and store the new integer in a.
The second time pick x = 9 and y = 1 and store the new integer in b.
We have now a = 9 and b = 1 and max difference = 8


Constraints:
1) 1 <= num <= 10^8

"""

from typing import List


class Solution:

    def maxDiff(self, num: int) -> int:
        s = str(num)

        def firstNot(s: str, t: str) -> int:
            for i, c in enumerate(s):
                if all(c != d for d in t):
                    return i
            return 0

        firstNot9 = firstNot(s, '9')
        firstNot01 = firstNot(s, '01')
        a = s.replace(s[firstNot9], '9')
        b = s.replace(s[firstNot01], '1' if firstNot01 == 0 else '0')
        return int(a) - int(b)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.maxDiff(555), 888)
    test(solution.maxDiff(9), 8)
    test(solution.maxDiff(123), 820)
    test(solution.maxDiff(123456), 820000)
    test(solution.maxDiff(9288), 8700)
