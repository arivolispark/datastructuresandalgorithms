"""
Title:  539. Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the
minimum minutes difference between any two time-points in the list.


Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1


Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0


Constraints:
1) 2 <= timePoints.length <= 2 * 104
2) timePoints[i] is in the format "HH:MM".

"""
from typing import List
import math


class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        time_list = []
        diff = math.inf

        for time_str in timePoints:
            split_str = time_str.split(":")
            hours, minutes = int(split_str[0]), int(split_str[1])
            time_list.append(hours * 60 + minutes)
        time_list.sort()

        for i in range(len(time_list) - 1):
            diff = min(diff, time_list[i + 1] - time_list[i])
            if diff == 0:
                return 0

        diff = min(diff, 24 * 60 + time_list[0] - time_list[-1])

        return diff


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findMinDifference(["23:59","00:00"]), 1)
    test(solution.findMinDifference(["00:00","23:59","00:00"]), 0)
