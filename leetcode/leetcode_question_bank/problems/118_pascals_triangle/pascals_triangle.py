"""

Title:  Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""

from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        result = []

        pascals_triangle_map = {}

        pascals_triangle_map[0] = [1]

        if numRows > 0:
            for i in range(1, numRows):
                pascals_triangle_row = pascals_triangle_map.get(i - 1)
                temp = []
                temp.append(1)

                for j in range(1, len(pascals_triangle_row)):
                    temp.append(pascals_triangle_row[j - 1] + pascals_triangle_row[j])
                temp.append(1)

                pascals_triangle_map[i] = temp
        #print(" pascals_triangle_map: ", pascals_triangle_map)

        for i in range(numRows):
            result.append(pascals_triangle_map.get(i))

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.generate(1), [[1]])
    test(solution.generate(2), [[1], [1, 1]])
    test(solution.generate(3), [[1], [1, 1], [1, 2, 1]])
    test(solution.generate(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
    test(solution.generate(5), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]])
