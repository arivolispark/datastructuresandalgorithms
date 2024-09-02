"""
Title:  1894. Find the Student that Will Replace the Chalk

There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem
starting with the student number 0, then the student number 1, and so on until the teacher reaches the
student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.

You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When
the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that
problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student
number i will be asked to replace the chalk.

Return the index of the student that will replace the chalk pieces.



Example 1:
Input: chalk = [5,1,5], k = 22
Output: 0
Explanation: The students go in turns as follows:
- Student number 0 uses 5 chalk, so k = 17.
- Student number 1 uses 1 chalk, so k = 16.
- Student number 2 uses 5 chalk, so k = 11.
- Student number 0 uses 5 chalk, so k = 6.
- Student number 1 uses 1 chalk, so k = 5.
- Student number 2 uses 5 chalk, so k = 0.
Student number 0 does not have enough chalk, so they will have to replace it.


Example 2:
Input: chalk = [3,4,1,2], k = 25
Output: 1
Explanation: The students go in turns as follows:
- Student number 0 uses 3 chalk so k = 22.
- Student number 1 uses 4 chalk so k = 18.
- Student number 2 uses 1 chalk so k = 17.
- Student number 3 uses 2 chalk so k = 15.
- Student number 0 uses 3 chalk so k = 12.
- Student number 1 uses 4 chalk so k = 8.
- Student number 2 uses 1 chalk so k = 7.
- Student number 3 uses 2 chalk so k = 5.
- Student number 0 uses 3 chalk so k = 2.
Student number 1 does not have enough chalk, so they will have to replace it.


Constraints:
1) chalk.length == n
2) 1 <= n <= 10^5
3) 1 <= chalk[i] <= 10^5
4) 1 <= k <= 10^9

"""

from typing import List


class Solution:

    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total

        if k == 0:
            return 0

        for i in range(len(chalk)):
            k -= chalk[i]
            if k < 0:
                return i


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.chalkReplacer([5,1,5], 22), 0)
    test(solution.chalkReplacer([3,4,1,2], 25), 1)
    test(solution.chalkReplacer([78,29,2,52,7,85,48,43,6,83,39,79,21,52,90,22,37,20,30,40,64,70,10,48,75,28,97,42,68,20,30,54,5,7,69,61,89,77,60,88,10,85,47,100,64,56,80,61,76,95,66,59,85,43,46,40,57,22,64,3,47,79,2,81,48,18,67,82,75,3,45,18,22,56,46,93,34,75,55,51,83,76,39,65,16,97,25,91,61,37,10,12,8,54,43,9,71,22,50,58,65,25,15,100,22,47,69,11,93,52,64,15,90,52,44,95,69], 480962772), 83)
