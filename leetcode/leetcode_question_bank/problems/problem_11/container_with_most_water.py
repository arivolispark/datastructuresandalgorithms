"""
Problem #: 11
Title:  Container With Most Water


Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together
with x-axis forms a container, such that the container contains the
most water.

Note: You may not slant the container and n is at least 2.


Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""


from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                window_area = (right - left) * height[left]
                left += 1
            else:
                window_area = (right - left) * height[right]
                right -= 1
            if window_area > max_area:
                max_area = window_area
        return max_area


if __name__ == "__main__":
    solution = Solution()

    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print("\n height: ", height)

    max_area = solution.maxArea(height)
    print("\n max_area: ", max_area)
