"""
Title: Insert Interval

Given a set of non-overlapping intervals, insert a new interval
into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according
to their start times.


Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]


Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

"""


from typing import List
from collections import deque


class Interval:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        temp_result = []
        merged = []
        i, start, end = 0, 0, 1

        # skip (and add to output) all intervals that come before the 'new_interval'
        while i < len(intervals) - 1 and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1

        # merge all intervals that overlap with 'new_interval'
        while i < len(intervals) - 1 and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = max(intervals[i][end], newInterval[end])
            i += 1

        # insert the new_interval
        merged.append(newInterval)

        # add all the remaining intervals to the output
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        for i in range(len(merged)):
            if len(merged[i]) > 0:
                temp_result.append(merged[i])

        temp_result.sort(key=lambda x: x[0])

        temp_result = helper(temp_result)

        interval_list = []
        for i in range(len(temp_result)):
            interval = Interval(temp_result[i][0], temp_result[i][1])
            interval_list.append(interval)

        result = merge(interval_list)
        result_list = []

        for i in range(len(result)):
            start = result[i].start
            end = result[i].end
            result_list.append([result[i].start, result[i].end])
            #print(" start: ", start, "\t end: ", end)

        return result_list


def helper(intervals: List[List[int]]) -> List[List[int]]:
    result = []
    intervals_to_be_merged = []
    intervals_not_to_be_merged = []
    if intervals:
        first_interval = intervals[0]
        for i in range(1, len(intervals)):
            #print(intervals[i], "\t type(intervals[i]): ", type(intervals[i]))

            if intervals[i][0] <= first_interval[0] <= intervals[i][1]:
                intervals_to_be_merged.append(intervals[i])
            elif intervals[i][0] > first_interval[0] and intervals[i][1] <= first_interval[1]:
                intervals_to_be_merged.append(intervals[i])
            elif intervals[i][0] <= first_interval[1] <= intervals[i][1]:
                intervals_to_be_merged.append(intervals[i])
            else:
                intervals_not_to_be_merged.append(intervals[i])

        #print(" intervals: ", intervals)
        #print(" intervals_to_be_merged: ", intervals_to_be_merged)
        #print(" intervals_not_to_be_merged: ", intervals_not_to_be_merged)

        q = deque()
        q.append(first_interval)
        for i in range(len(intervals_to_be_merged)):
            q.append(intervals_to_be_merged[i])
        #print(" q: ", q)

        while len(q) > 1:
            interval_1 = q.popleft()
            interval_2 = q.popleft()
            start = min(interval_1[0], interval_2[0])
            end = max(interval_1[1], interval_2[1])
            q.append([start, end])

            if len(q) == 1:
                break
        #print(" q: ", q)

        for i in range(len(intervals_not_to_be_merged)):
            result.append(intervals_not_to_be_merged[i])
        result.append(q[0])

        result.sort(key=lambda x: x[0])

    return result


def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals on the start time
    intervals.sort(key=lambda x: x.start)

    mergedIntervals = []
    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:  # overlapping intervals, adjust the 'end'
            end = max(interval.end, end)
        else:  # non-overlapping interval, add the previous internval and reset
            mergedIntervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    mergedIntervals.append(Interval(start, end))
    return mergedIntervals


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.insert([[1,3],[6,9]], [2,5]), [[1,5],[6,9]])
    test(solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]), [[1,2],[3,10],[12,16]])
    test(solution.insert([[]], [5,7]), [[5,7]])
    test(solution.insert([[1,5]], [2,3]), [[1,5]])
    test(solution.insert([[1,5]], [2,7]), [[1,7]])
    test(solution.insert([[0,2],[3,9]], [6,8]), [[0,2],[3,9]])
