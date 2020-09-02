"""
Title:  Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting
from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made,
return an empty string.



Example 1:
Input: [1,2,3,4]
Output: "23:41"



Example 2:
Input: [5,5,5,5]
Output: ""


Note:
1) A.length == 4
2) 0 <= A[i] <= 9

"""


from typing import List
from collections import deque


class Solution:

    def largestTimeFromDigits(self, A: List[int]) -> str:
        result = ""

        for i in range(4):
            for j in range(4):
                for k in range(4):
                    if i == j or j == k or k == i:
                        continue
                    hh = str(A[i]) + str(A[j])
                    mm = str(A[k]) + str(A[6 - i - j - k])
                    temp_time = hh + ":" + mm
                    if hh < "24" and mm < "60" and temp_time > result:
                        result = temp_time
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.largestTimeFromDigits([1,2,3,4]), "23:41")
    test(solution.largestTimeFromDigits([5,5,5,5]), "")
