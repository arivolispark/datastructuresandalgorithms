"""
Title:  Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).


Example 1:
Input: 2.00000, 10
Output: 1024.00000


Example 2:
Input: 2.10000, 3
Output: 9.26100


Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Note:
1) -100.0 < x < 100.0
2) n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""


class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        temp = self.myPow(x, int(n / 2))

        if n % 2 == 0:
            return temp * temp
        else:
            if n > 0:
                return x * temp * temp
            else:
                return (temp * temp) / x


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.myPow(2.00000, 10), 1024.00000)
    test(solution.myPow(2.10000, 3), 9.26100)
    test(solution.myPow(2.00000, -2), 0.25000)
