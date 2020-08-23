"""
Title:  Random Point in Non-overlapping Rectangles

Given a list of non-overlapping axis-aligned rectangles rects, write a function pick
which randomly and uniformily picks an integer point in the space covered by the rectangles.


Note:
1) An integer point is a point that has integer coordinates.
2) A point on the perimeter of a rectangle is included in the space covered by the rectangles.
3) ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left
corner, and [x2, y2] are the integer coordinates of the top-right corner.
4) length and width of each rectangle does not exceed 2000.
5) 1 <= rects.length <= 100
6) pick return a point as an array of integer coordinates [p_x, p_y]
7) pick is called at most 10000 times.



Example 1:
Input:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output:
[null,[4,1],[4,1],[3,3]]



Example 2:
Input:
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output:
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]


Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor
has one argument, the array of rectangles rects. pick has no arguments. Arguments are always
wrapped with a list, even if there aren't any.

"""

from typing import List
import random


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.num_pts = 0
        self.rects = rects
        self.rect_cum_count = []
        for rect in rects:
            self.num_pts += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            self.rect_cum_count.append(self.num_pts)

    def pick(self) -> List[int]:
        pt_idx = random.randint(0, self.num_pts - 1)
        start, end = 0, len(self.rects) - 1

        while start < end:
            mid = start + (end - start) // 2
            if self.rect_cum_count[mid] <= pt_idx:
                start = mid + 1
            else:
                end = mid

        rect = self.rects[start]
        x_pts = rect[2] - rect[0] + 1
        y_pts = rect[3] - rect[1] + 1
        pts_in_rect = x_pts * y_pts
        pt_start = self.rect_cum_count[start] - pts_in_rect
        offset = pt_idx - pt_start
        return [rect[0] + offset % x_pts, rect[1] + offset // x_pts]


    # Your Solution object will be instantiated and called as such:
    # obj = Solution(rects)
    # param_1 = obj.pick()


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1():
    print()
    solution = Solution([[1, 1, 5, 5]])

    print(solution.pick())
    print(solution.pick())
    print(solution.pick())


def get_test_case_2():
    print()
    solution = Solution([[-2, -2, -1, -1], [1, 0, 3, 0]])

    print(solution.pick())
    print(solution.pick())
    print(solution.pick())
    print(solution.pick())
    print(solution.pick())


if __name__ == "__main__":
    get_test_case_1()
    get_test_case_2()
