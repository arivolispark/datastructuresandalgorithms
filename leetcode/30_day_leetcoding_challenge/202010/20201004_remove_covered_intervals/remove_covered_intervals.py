"""
Title:  Remove Covered Intervals

Given a list of intervals, remove all intervals that are covered by another interval in the list.

Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.

After doing so, return the number of remaining intervals.



Example 1:
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.



Example 2:
Input: intervals = [[1,4],[2,3]]
Output: 1



Example 3:
Input: intervals = [[0,10],[5,12]]
Output: 2



Example 4:
Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2



Example 5:
Input: intervals = [[1,2],[1,4],[3,4]]
Output: 1


Constraints:
1) 1 <= intervals.length <= 1000
2) intervals[i].length == 2
3) 0 <= intervals[i][0] < intervals[i][1] <= 10^5
4) All the intervals are unique.

"""


from typing import List


class Solution:

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        result = list()
        if intervals:
            intervals.sort(key=lambda x: x[0])

            interval = intervals[0]
            result.append([interval[0], interval[1]])

            for i in range(1, len(intervals)):
                current_interval = intervals[i]
                if current_interval[0] > interval[0]:
                    if current_interval[0] <= interval[1]:
                        if current_interval[1] > interval[1]:
                            result.append([current_interval[0], current_interval[1]])
                            interval = current_interval
                    elif current_interval[0] > interval[1]:
                        result.append([current_interval[0], current_interval[1]])
                        interval = current_interval
                elif current_interval[0] == interval[0]:
                    if current_interval[1] > interval[1]:
                        result.pop(-1)
                        result.append([current_interval[0], current_interval[1]])
                        interval = current_interval
        return len(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.removeCoveredIntervals([[1,4],[3,6],[2,8]]), 2)
    test(solution.removeCoveredIntervals([[1,4],[2,3]]), 1)
    test(solution.removeCoveredIntervals([[0,10],[5,12]]), 2)
    test(solution.removeCoveredIntervals([[3,10],[4,10],[5,11]]), 2)
    test(solution.removeCoveredIntervals([[1,2],[1,4],[3,4]]), 1)
    test(solution.removeCoveredIntervals([[3,4],[1,4],[2,4]]), 1)
