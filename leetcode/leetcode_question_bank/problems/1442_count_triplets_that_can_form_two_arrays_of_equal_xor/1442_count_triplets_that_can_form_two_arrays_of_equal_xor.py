"""
Title:  1442. Count Triplets That Can Form Two Arrays of Equal XOR

Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:
1) a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
2) b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.



Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)


Example 2:
Input: arr = [1,1,1,1,1]
Output: 10


Constraints:
1) 1 <= arr.length <= 300
2) 1 <= arr[i] <= 108

"""

from typing import List


class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        result = 0
        length = len(arr)
        prefix = []

        prefix.append(0)

        for i in range(1, length + 1):
            prefix.append(prefix[i - 1] ^ arr[i - 1])
        #print(" prefix: ", prefix)

        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j, length):
                    if prefix[i] ^ prefix[j] == prefix[j] ^ prefix[k + 1]:
                        result += 1

        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.countTriplets([2,3,1,6,7]), 4)
    test(solution.countTriplets([1,1,1,1,1]), 10)
