"""
Title:  The kth Factor of n

Given two positive integers n and k.

A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor
in this list or return -1 if n has less than k factors.



Example 1:
Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.



Example 2:
Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.



Example 3:
Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.



Example 4:
Input: n = 1, k = 1
Output: 1
Explanation: Factors list is [1], the 1st factor is 1.



Example 5:
Input: n = 1000, k = 3
Output: 4
Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].



Constraints:

1) 1 <= k <= n <= 1000

"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = [1]
        if len(factors) == k:
            return factors[k - 1]

        for i in range(2, ((n + 1) // 2) + 1):
            if n % i == 0:
                factors.append(i)
                if len(factors) == k:
                    return i

        factors.append(n)

        if len(factors) == k:
            return n

        return -1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.kthFactor(12, 3), 3)
    test(solution.kthFactor(7, 2), 7)
    test(solution.kthFactor(4, 4), -1)
    test(solution.kthFactor(1, 1), 1)
    test(solution.kthFactor(1000, 3), 4)
    test(solution.kthFactor(4, 1), 1)
