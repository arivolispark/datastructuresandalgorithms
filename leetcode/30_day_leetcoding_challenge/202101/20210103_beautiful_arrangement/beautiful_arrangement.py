"""
Title:  Beautiful Arrangement

Suppose you have n integers labeled 1 through n. A permutation of those n integers
perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either
of the following is true:

1) perm[i] is divisible by i.
2) i is divisible by perm[i].

Given an integer n, return the number of the beautiful arrangements that you can construct.



Example 1:
Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1



Example 2:
Input: n = 1
Output: 1



Constraints:

1) 1 <= n <= 15

"""


class Solution:
    def countArrangement(self, n: int) -> int:
        all = (1 << n) - 1
        result = [0] * all

        def permutation(tmp, k, answer):
            if tmp == all:
                return 1
            if answer[tmp] > 0:
                return answer[tmp]

            score = 0
            for i in range(1, n + 1):
                if (tmp & (1 << (i - 1))) == 0:
                    if (k % i == 0) or (i % k == 0):
                        score += permutation(tmp + (1 << (i - 1)), k + 1, answer)
            answer[tmp] = score
            return score

        score = permutation(0, 1, result)
        return score


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.countArrangement(2), 2)
    test(solution.countArrangement(1), 1)
