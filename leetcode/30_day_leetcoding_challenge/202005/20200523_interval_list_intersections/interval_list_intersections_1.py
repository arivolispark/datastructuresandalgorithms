"""
Title:  Interval List Intersections

Given two lists of closed intervals, each list of intervals
is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the
set of real numbers x with a <= x <= b.  The intersection of two
closed intervals is a set of real numbers that is either empty, or
can be represented as a closed interval.  For example, the
intersection of [1, 3] and [2, 4] is [2, 3].)



Example 1:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.


Note:
1) 0 <= A.length < 1000
2) 0 <= B.length < 1000
3) 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""

from typing import List


class Solution:

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if A and B:
            result = []
            len_a, len_b = len(A), len(B)
            i, j = 0, 0

            A.sort()
            B.sort()

            while i < len_a and j < len_b:
                if A[i][0] <= B[j][0] <= A[i][1]:
                    if A[i][0] <= B[j][1] <= A[i][1]:
                        result.append(B[j])
                        j += 1
                    else:
                        result.append([B[j][0], A[i][1]])
                        B[j] = [A[i][1], B[j][1]]
                        i += 1
                elif B[j][0] <= A[i][0] <= B[j][1]:
                    if B[j][0] <= A[i][1] <= B[j][1]:
                        result.append(A[i])
                        i += 1
                    else:
                        result.append([A[i][0], B[j][1]])
                        j += 1
                elif B[j][1] < A[i][0]:
                    j += 1
                else:
                    i += 1
            return result
        return None


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.intervalIntersection([], []), None)
    test(solution.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]), [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]])
