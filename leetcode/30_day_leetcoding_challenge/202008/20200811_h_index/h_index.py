"""
Title:  H-Index

Given an array of citations (each citation is a non-negative integer) of a
researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has
index h if h of his/her N papers have at least h citations each, and the
other N − h papers have no more than h citations each."


Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.


Note: If there are several possible values for h, the maximum one is taken as the h-index.

"""

from typing import List


class Solution:

    def hIndex(self, citations: List[int]) -> int:
        if citations:
            citations_len = len(citations)
            citations.sort()
            i = 1
            while i <= citations_len:
                if citations[citations_len - i] < i:
                    break
                i += 1
            return i - 1
        return 0


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.hIndex(None), 0)
    test(solution.hIndex([]), 0)
    test(solution.hIndex([1]), 1)
    test(solution.hIndex([3, 2, 1]), 2)
    test(solution.hIndex([3, 0, 6, 1, 5]), 3)
    test(solution.hIndex([0, 1, 3, 5, 6]), 3)
    test(solution.hIndex([2, 2, 2, 2, 2]), 2)
    test(solution.hIndex([0, 0, 0, 9, 9, 9]), 3)
    test(solution.hIndex([1, 0]), 1)
