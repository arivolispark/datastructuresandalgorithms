"""
Title:  Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]


Follow up:
Could you optimize your algorithm to use only O(k) extra space?

"""

from typing import List


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        pascals_triangle_map = {}

        pascals_triangle_map[0] = [1]

        if rowIndex > 0:
            for i in range(1, rowIndex + 1):
                pascals_triangle_row = pascals_triangle_map.get(i - 1)
                temp = []
                temp.append(1)

                for j in range(1, len(pascals_triangle_row)):
                    temp.append(pascals_triangle_row[j - 1] + pascals_triangle_row[j])
                temp.append(1)

                pascals_triangle_map[i] = temp
        # print(" pascals_triangle_map: ", pascals_triangle_map)
        return pascals_triangle_map[rowIndex]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.getRow(0), [1])
    test(solution.getRow(1), [1,1])
    test(solution.getRow(2), [1,2,1])
    test(solution.getRow(3), [1,3,3,1])
    test(solution.getRow(4), [1,4,6,4,1])
    test(solution.getRow(5), [1,5,10,10,5,1])
