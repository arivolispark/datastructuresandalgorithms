"""
Title:  Numbers With Same Consecutive Differences

Return all non-negative integers of length N such that the absolute difference
between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the
number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:
Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.



Example 2:
Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:
1) 1 <= N <= 9
2) 0 <= K <= 9

"""


from typing import List


class Solution:

    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        result = []

        if N == 1:
            result.append(0)

        def dfs(num, N):
            if N == 0:
                result.append(num)
                return

            last_digit = num % 10
            if last_digit >= K:
                dfs(num * 10 + last_digit - K, N - 1)
            if K > 0 and last_digit + K < 10:
                dfs(num * 10 + last_digit + K, N - 1)

        for d in range(1, 10):
            dfs(d, N - 1)

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.numsSameConsecDiff(3, 7), [181,292,707,818,929])
    test(solution.numsSameConsecDiff(2, 1), [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98])
