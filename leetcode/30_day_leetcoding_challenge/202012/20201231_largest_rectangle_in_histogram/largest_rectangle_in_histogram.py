"""
Title:  Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the
width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



Example:
Input: [2,1,5,6,2,3]
Output: 10



Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.



Example 2:


Input: heights = [2,4]
Output: 4



Constraints:

1) 1 <= heights.length <= 10^5
2) 0 <= heights[i] <= 10^4

"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        i = 0
        result = 0

        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                x = stack[-1]
                stack.pop()
                height = heights[x]
                temp = height * (i - stack[-1] - 1) if len(stack) != 0 else height * i
                result = max(result, temp)

        while len(stack) > 0:
            x = stack[-1]
            height = heights[x]
            stack.pop()
            temp = height * (len(heights) - stack[-1] - 1) if len(stack) != 0 else height * len(heights)
            result = max(result, temp)

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.largestRectangleArea([2,1,5,6,2,3]), 10)
    test(solution.largestRectangleArea([2,4]), 4)
