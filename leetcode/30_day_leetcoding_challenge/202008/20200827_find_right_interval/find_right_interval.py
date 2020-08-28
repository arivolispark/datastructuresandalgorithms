"""
Title:  Find Right Interval

Given a set of intervals, for each of the interval i, check if there exists an interval j whose
start point is bigger than or equal to the end point of the interval i, which can be called
that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the
interval j has the minimum start point to build the "right" relationship for interval i. If
the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored
value of each interval as an array.


Note:
1) You may assume the interval's end point is always bigger than its start point.
2) You may assume none of these intervals have the same start point.



Example 1:
Input: [ [1,2] ]
Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.



Example 2:
Input: [ [3,4], [2,3], [1,2] ]
Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.



Example 3:
Input: [ [1,4], [2,3], [3,4] ]
Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

NOTE: input types have been changed on April 15, 2019. Please reset to
default code definition to get new method signature.

"""


from typing import List


class Solution:

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = []
        n = len(intervals)
        for i in range(n):
            sorted_intervals.append([intervals[i], i])
        sorted_intervals.sort()

        result = [-1] * n

        def binary_search(x):
            if sorted_intervals[n - 1][0][0] < x:
                return -1

            start, end = 0, n - 1
            while start <= end:
                mid = start + (end - start) // 2
                if sorted_intervals[mid][0][0] >= x:
                    end = mid - 1
                else:
                    start = mid + 1
            return sorted_intervals[start][1]

        for i in range(n):
            result[i] = binary_search(intervals[i][1])

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.findRightInterval([[1,2]]), [-1])
    test(solution.findRightInterval([[3,4], [2,3], [1,2]]), [-1, 0, 1])
    test(solution.findRightInterval([[1,4], [2,3], [3,4]]), [-1, 2, -1])
