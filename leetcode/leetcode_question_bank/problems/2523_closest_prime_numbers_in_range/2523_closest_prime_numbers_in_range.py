"""
Title:  2523. Closest Prime Numbers in Range

Given two positive integers left and right, find the two integers num1 and num2 such that:

left <= num1 < num2 <= right .
Both num1 and num2 are prime numbers.
num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
Return the positive integer array ans = [num1, num2]. If there are multiple
pairs satisfying these conditions, return the one with the smallest num1 value.
If no such numbers exist, return [-1, -1].



Example 1:
Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.


Example 2:
Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.



Constraints:
1) 1 <= left <= right <= 10^6

"""

from typing import List
import math


class Solution:

    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = self._sieveEratosthenes(right + 1)
        primes = [i for i in range(left, right + 1) if isPrime[i]]

        min_diff = math.inf
        start, end = 0, 1

        if len(primes) < 2:
            return [-1, -1]

        for i in range(len(primes) - 1):
            if (primes[i + 1] - primes[i]) < min_diff:
                start, end = i, i + 1
                min_diff = primes[i + 1] - primes[i]

        return [primes[start], primes[end]]

    def _sieveEratosthenes(self, n: int) -> list[bool]:
        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        return isPrime


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.closestPrimes(10, 19), [11, 13])
    test(solution.closestPrimes(4, 6), [-1, -1])
    test(solution.closestPrimes(1852, 2063), [1871,1873])
