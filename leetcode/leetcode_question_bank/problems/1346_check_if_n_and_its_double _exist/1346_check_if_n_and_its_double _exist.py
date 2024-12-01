"""
Title:  1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :

1) i != j
2) 0 <= i, j < arr.length
3) arr[i] == 2 * arr[j]


Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]


Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.


Constraints:
1) 2 <= arr.length <= 500
2) -10^3 <= arr[i] <= 10^3

"""

from typing import List


class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        map = {}

        for i in range(len(arr)):
            map[arr[i]] = i

        for i in range(len(arr)):
            double_num = 2 * arr[i]
            if double_num in map and i != map[double_num]:
                return True

        return False


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.checkIfExist([10,2,5,3]), True)
    test(solution.checkIfExist([3,1,7,11]), False)
    test(solution.checkIfExist([-2,0,10,-19,4,6,-8]), False)
    test(solution.checkIfExist([0,0]), True)
