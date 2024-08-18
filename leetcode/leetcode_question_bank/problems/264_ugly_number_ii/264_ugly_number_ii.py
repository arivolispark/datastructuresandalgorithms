"""
Title:  264. Ugly Number II

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.


Example 2:
Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


Constraints:
1) 1 <= n <= 1690

"""
from heapq import *

class Solution:

    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        min_heap = []
        s = set()
        count = 0

        if 1 not in s:
            heappush(min_heap, 1)
            s.add(1)

        while min_heap:
            count += 1
            val = heappop(min_heap)

            if count == n:
                return val

            val_mul_2 = val * 2
            val_mul_3 = val * 3
            val_mul_5 = val * 5

            if val_mul_2 not in s:
                heappush(min_heap, val * 2)
                s.add(val_mul_2)

            if val_mul_3 not in s:
                heappush(min_heap, val * 3)
                s.add(val_mul_3)

            if val_mul_5 not in s:
                heappush(min_heap, val * 5)
                s.add(val_mul_5)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.nthUglyNumber(10), 12)
    test(solution.nthUglyNumber(1), 1)
