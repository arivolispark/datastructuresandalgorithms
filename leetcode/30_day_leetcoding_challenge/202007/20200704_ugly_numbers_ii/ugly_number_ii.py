"""
Title:  Ugly Number II

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.


Note:
1) 1 is typically treated as an ugly number.
2) n does not exceed 1690.

"""


class Solution:

    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n

        ugly_numbers[0] = 1

        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        index_of_2_list = 0
        index_of_3_list = 0
        index_of_5_list = 0

        for i in range(1, n):
            ugly_numbers[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

            if ugly_numbers[i] == next_multiple_of_2:
                index_of_2_list += 1
                next_multiple_of_2 = ugly_numbers[index_of_2_list] * 2
            if ugly_numbers[i] == next_multiple_of_3:
                index_of_3_list += 1
                next_multiple_of_3 = ugly_numbers[index_of_3_list] * 3
            if ugly_numbers[i] == next_multiple_of_5:
                index_of_5_list += 1
                next_multiple_of_5 = ugly_numbers[index_of_5_list] * 5

        #print(" ugly_numbers: ", ugly_numbers)
        return ugly_numbers[-1]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.nthUglyNumber(1), 1)
    test(solution.nthUglyNumber(2), 2)
    test(solution.nthUglyNumber(3), 3)
    test(solution.nthUglyNumber(4), 4)
    test(solution.nthUglyNumber(5), 5)
    test(solution.nthUglyNumber(6), 6)
    test(solution.nthUglyNumber(7), 8)
    test(solution.nthUglyNumber(8), 9)
    test(solution.nthUglyNumber(9), 10)
    test(solution.nthUglyNumber(10), 12)
    test(solution.nthUglyNumber(11), 15)
    test(solution.nthUglyNumber(12), 16)
    test(solution.nthUglyNumber(1690), 2123366400)
