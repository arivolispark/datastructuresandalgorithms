"""
Title:  Sort Array By Parity

Given an array A of non-negative integers, return an array consisting
of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.


Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:
1) 1 <= A.length <= 5000
2) 0 <= A[i] <= 5000

"""

from typing import List


class Solution:

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = []
        if A:
            even_list = []
            odd_list = []
            for i in range(len(A)):
                if A[i] % 2 == 0:
                    even_list.append(A[i])
                else:
                    odd_list.append(A[i])
            result = list(even_list + odd_list)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.sortArrayByParity([3,1,2,4]), [2,4,3,1])
