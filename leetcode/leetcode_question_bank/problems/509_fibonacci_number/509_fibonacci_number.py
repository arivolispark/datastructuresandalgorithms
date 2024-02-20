"""
Title: 509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such
that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).



Example 1:
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.


Example 2:
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.


Example 3:
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.


Constraints:
1) 0 <= n <= 30

"""


class Solution:

    def fib(self, n: int) -> int:

        map = {
            0: 0,
            1: 1
        }

        for i in range(2, n + 1):
            map[i] = map[i - 2] + map[i - 1]

        return map[n]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.fib(0), 0)
    test(solution.fib(1), 1)
    test(solution.fib(2), 1)
    test(solution.fib(3), 2)
    test(solution.fib(4), 3)
    test(solution.fib(5), 5)
    test(solution.fib(6), 8)
    test(solution.fib(7), 13)
    test(solution.fib(8), 21)
    test(solution.fib(9), 34)
    test(solution.fib(10), 55)
    test(solution.fib(11), 89)
    test(solution.fib(12), 144)
    test(solution.fib(13), 233)
    test(solution.fib(14), 377)
    test(solution.fib(15), 610)
    test(solution.fib(16), 987)
    test(solution.fib(17), 1597)
    test(solution.fib(18), 2584)
    test(solution.fib(19), 4181)
    test(solution.fib(20), 6765)
    test(solution.fib(21), 10946)
    test(solution.fib(22), 17711)
    test(solution.fib(23), 28657)
    test(solution.fib(24), 46368)
    test(solution.fib(25), 75025)
    test(solution.fib(26), 121393)
    test(solution.fib(27), 196418)
    test(solution.fib(28), 317811)
    test(solution.fib(29), 514229)
    test(solution.fib(30), 832040)
    test(solution.fib(31), 1346269)
    test(solution.fib(32), 2178309)
    test(solution.fib(33), 3524578)
    test(solution.fib(34), 5702887)
    test(solution.fib(35), 9227465)
    test(solution.fib(36), 14930352)
    test(solution.fib(37), 24157817)
