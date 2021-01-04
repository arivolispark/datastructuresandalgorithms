"""
Title:  Check Array Formation Through Concatenation

You are given an array of distinct integers arr and an array of integer arrays pieces, where the
integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces
in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.



Example 1:
Input: arr = [85], pieces = [[85]]
Output: true



Example 2:
Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]



Example 3:
Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].



Example 4:
Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]



Example 5:
Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false


Constraints:

1) 1 <= pieces.length <= arr.length <= 100
2) sum(pieces[i].length) == arr.length
3) 1 <= pieces[i].length <= arr.length
4) 1 <= arr[i], pieces[i][j] <= 100
5) The integers in arr are distinct.
6) The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).

"""

from typing import List


class Solution:

    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        if arr and pieces:
            arr_string = ""
            for i in range(len(arr)):
                arr_string = arr_string + str(arr[i]) + "_"

            for i in range(len(pieces)):
                pieces_string = ""
                for j in range(len(pieces[i])):
                    pieces_string = pieces_string + str(pieces[i][j]) + "_"

                if pieces_string not in arr_string:
                    return False

            return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.canFormArray([85], [[85]]), True)
    test(solution.canFormArray([15,88], [[88],[15]]), True)
    test(solution.canFormArray([49,18,16], [[16,18,49]]), False)
    test(solution.canFormArray([91,4,64,78], [[78],[4,64],[91]]), True)
    test(solution.canFormArray([1,3,5,7], [[2,4,6,8]]), False)
