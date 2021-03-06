"""
Title:  Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you
need to remove to make the rest of the intervals non-overlapping.


Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.


Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.


Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Note:
1) You may assume the interval's end point is always bigger than its start point.
2) Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

"""


from typing import List


class Solution:

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort()
        count, last_included = 0, 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last_included][1]:
                count += 1
                if intervals[i][1] < intervals[last_included][1]:
                    last_included = i
            else:
                last_included = i
        return count


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]), 1)
    test(solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]), 2)
    test(solution.eraseOverlapIntervals([[1,2],[2,3]]), 0)
