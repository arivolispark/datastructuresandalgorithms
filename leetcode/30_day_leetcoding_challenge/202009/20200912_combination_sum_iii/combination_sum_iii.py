"""
Title:  Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.

Note:
1) All numbers will be positive integers.
2) The solution set must not contain duplicate combinations.


Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]


Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

"""


from typing import List

class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def try_combination(combination, n, start):
            if k == len(combination):
                if n == 0:
                    result.append(combination.copy())
                    return
            for i in range(start, 10):
                combination.append(i)
                try_combination(combination, n - i, i + 1)
                combination.pop()
        try_combination([], n, 1)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.combinationSum3(3, 7), [[1,2,4]])
    test(solution.combinationSum3(3, 9), [[1,2,6], [1,3,5], [2,3,4]])
