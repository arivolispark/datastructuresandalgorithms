"""
Title:  1122. Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements
in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the
same as in arr2. Elements that do not appear in arr2 should be placed at the end
of arr1 in ascending order.


Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]


Example 2:
Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]


Constraints:
1) 1 <= arr1.length, arr2.length <= 1000
2) 0 <= arr1[i], arr2[i] <= 1000
3) All the elements of arr2 are distinct.
4) Each arr2[i] is in arr1.

"""

from typing import List


class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        map = {}

        for i in range(len(arr1)):
            map[arr1[i]] = map.get(arr1[i], 0) + 1

        for i in range(len(arr2)):
            v = map[arr2[i]]
            for j in range(v):
                result.append(arr2[i])
            del map[arr2[i]]

        li = []
        for k, v in map.items():
            for i in range(v):
                li.append(k)
        li.sort()

        result.extend(li)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]), [2,2,2,1,4,3,3,9,6,7,19])
    test(solution.relativeSortArray([28,6,22,8,44,17], [22,28,8,6]), [22,28,8,6,17,44])
