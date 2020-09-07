"""
Title:  Image Overlap

Two images A and B are given, represented as binary, square matrices of the
same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down
any number of units), and place it on top of the other image.  After, the overlap
of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3

Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes:
1) 1 <= A.length = A[0].length = B.length = B[0].length <= 30
2) 0 <= A[i][j], B[i][j] <= 1

"""


from typing import List


class Solution:

    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        def find_overlap_count(matrix_a, matrix_b):
            n, overlap_count = len(matrix_a), 0
            for x in range(n):
                for y in range(n):
                    temp = 0
                    for i in range(y, n):
                        for j in range(x, n):
                            if matrix_a[i][j] == 1 and matrix_b[i - y][j - x] == 1:
                                temp += 1
                    overlap_count = max(overlap_count, temp)
            return overlap_count

        return max(find_overlap_count(A, B), find_overlap_count(B, A))


def get_test_case_1_input() -> (List[List[int]], List[List[int]]):
    A = [[1, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]

    B = [[0, 0, 0],
         [0, 1, 1],
         [0, 0, 1]]

    return A, B


def get_test_case_1_output() -> int:
    return 3


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.largestOverlap(get_test_case_1_input()[0], get_test_case_1_input()[1]), get_test_case_1_output())
