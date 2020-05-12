"""
Title:  Flood Fill

An image is represented by a 2-D array of integers, each integer
representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row
and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels
connected 4-directionally to the starting pixel of the same color as the
starting pixel, plus any pixels connected 4-directionally to those
pixels (also with the same color as the starting pixel), and so on.
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.


Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.



Note:
1) The length of image and image[0] will be in the range [1, 50].
2) The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
3) The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

"""

from typing import List


class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image:
            rows = len(image)
            if rows > 0:
                columns = len(image[0])
                original_color = image[sr][sc]
                visited = [[False for _ in range(columns)] for _ in range(rows)]

                neighbor_row_cells = [-1, 0, 1, 0]
                neighbor_column_cells = [0, 1, 0, -1]

                dfs(rows, columns, image, sr, sc, newColor, original_color, visited, neighbor_row_cells, neighbor_column_cells)
        return image


def dfs(rows: int, columns: int, image: List[List[int]], sr: int, sc: int, new_color: int, original_color: int, visited: List[List[bool]], neighbor_row_cells: List[int], neighbor_column_cells: List[int]):
    if 0 <= sr < rows and 0 <= sc < columns:
        if image[sr][sc] == original_color and visited[sr][sc] is False:
            image[sr][sc] = new_color
            visited[sr][sc] = True

            for i in range(len(neighbor_row_cells)):
                dfs(rows, columns, image, sr + neighbor_row_cells[i], sc + neighbor_column_cells[i], new_color, original_color, visited, neighbor_row_cells, neighbor_column_cells)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
    test(solution.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2), [[2, 2, 2], [2, 2, 2]])
