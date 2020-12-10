"""
Title:  Populating Next Right Pointers in Each Node II

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]



Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1) 1 <= n <= 20

"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []

        number = 1
        matrix = [[0]*n for i in range(n)]

        for cycle in range((n + 1) // 2):
            
            # for elements in top row
            for column in range(cycle, n - cycle):
                matrix[cycle][column] = number
                number += 1

            # for elements in right column
            for row in range(cycle + 1, n - 1 - cycle):
                matrix[row][n - 1 - cycle] = number
                number += 1

            # for elements in bottom row
            if n-1-cycle != cycle: # in case of single row left in a cycle
                for column in range(n - 1 - cycle, cycle - 1 , -1):
                    matrix[n - 1 - cycle][column] = number
                    number += 1

            # for elements in left column
            if n-1-cycle != cycle: # in case of single column left in a cycle
                for row in range(n - 2 - cycle, cycle, -1):
                    matrix[row][cycle] = number
                    number += 1
        return matrix 


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))



if __name__ == "__main__":
    solution = Solution()

    test(solution.generateMatrix(3), [[1,2,3],[8,9,4],[7,6,5]])
    test(solution.generateMatrix(1), [[1]])

