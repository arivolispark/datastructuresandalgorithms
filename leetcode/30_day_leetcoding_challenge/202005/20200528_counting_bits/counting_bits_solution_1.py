"""
Title:  Counting Bits

Given a non negative integer number num. For every numbers i in
the range 0 ≤ i ≤ num calculate the number of 1's in their binary
representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]


Example 2:
Input: 5
Output: [0,1,1,2,1,2]


Follow up:

1) It is very easy to come up with a solution with
run time O(n*sizeof(integer)). But can
you do it in linear time O(n) /possibly in a single pass?
2) Space complexity should be O(n).
3) Can you do it like a boss? Do it without using
any builtin function like __builtin_popcount in c++ or
in any other language.

"""

from typing import List


class Solution:

    def countBits(self, num: int) -> List[int]:
        """

        0 = 0000 = 0
        1 = 0001 = 1

        2 = 0010 = 1
        3 = 0011 = 2

        4 = 0100 = 1
        5 = 0101 = 2
        6 = 0110 = 2
        7 = 0111 = 3

        8 = 1000 = 1
        9 = 1001 = 2
        10 = 1010 = 2
        11 = 1011 = 3
        12 = 1100 = 2
        13 = 1101 = 3
        14 = 1110 = 3
        15 = 1111 = 4
        16 = 10000 = 1

        17 = 10001 = 2
        18 = 10010 = 2
        19 = 10011 = 3
        20 = 10100 = 2
        21 = 10101 = 3
        22 = 10110 = 3
        23 = 10111 = 4

        24 = 11000 = 2
        25 = 11001 = 3
        26 = 11010 = 3
        27 = 11011 = 4

        28 = 11100 = 3
        29 = 11101 = 4
        30 = 11110 = 4
        31 = 11111 = 5
        32 = 100000 = 1
        33 = 100001 = 2

        :param num:
        :return:
        """

        result = []

        for i in range(num + 1):
            result.append(count_set_bits(i))

        return result


def count_set_bits(num: int) -> int:
    count = 0
    while num > 0:
        if num & 1 == 1:
            count += 1
        num >>= 1
    return count


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.countBits(2), [0,1,1])
    test(solution.countBits(5), [0,1,1,2,1,2])
    test(solution.countBits(17), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2])
    test(solution.countBits(33), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2])
    test(solution.countBits(257), [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8, 1, 2])
