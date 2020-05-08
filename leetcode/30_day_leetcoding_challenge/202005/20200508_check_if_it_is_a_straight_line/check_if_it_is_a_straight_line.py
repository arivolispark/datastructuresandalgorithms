"""
Title:  Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y],
where [x, y] represents the coordinate of a point. Check if
these points make a straight line in the XY plane.


Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true


Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

1) 2 <= coordinates.length <= 1000
2) coordinates[i].length == 2
3) -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
4) coordinates contains no duplicate point.

"""

from typing import List


class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if coordinates:
            n = len(coordinates)
            slope = None

            for i in range(n - 1):
                coordinate_1 = coordinates[i]
                coordinate_2 = coordinates[i + 1]

                if (coordinate_2[0] - coordinate_1[0]) == 0:
                    current_slope = 2
                else:
                    current_slope = (coordinate_2[1] - coordinate_1[1]) // (coordinate_2[0] - coordinate_1[0])  # calculate slope

                if slope is None:
                    slope = current_slope
                else:
                    if current_slope != slope:
                        return False
            return True
        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]), True)
    test(solution.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]), False)
