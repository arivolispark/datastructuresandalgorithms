"""
Title:  H-Index II

Given an array of citations sorted in ascending order
(each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist
has index h if h of his/her N papers have at least h citations each,
and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had
             received 0, 1, 3, 5, 6 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.


Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed
to be sorted in ascending order.  Could you solve it in logarithmic time complexity?

"""

from typing import List


class Solution:

    def h_index(self, citations: List[int]) -> int:
        if citations:
            size = len(citations)
            start, end = 0, size - 1
            while start <= end:
                mid = start + (end - start) // 2
                if citations[mid] == size - mid:
                    return citations[mid]
                elif citations[mid] < size - mid:
                    start = mid + 1
                else:
                    end = mid - 1
            return size - end - 1
        return 0


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.h_index([]), 0)
    test(solution.h_index([0,1,3,5,6]), 3)
    test(solution.h_index([2,2,2,2,2]), 2)
    test(solution.h_index([0,0,0,9,9,9]), 3)
