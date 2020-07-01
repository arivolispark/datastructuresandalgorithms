"""
Title:  Arranging Coins

You have a total of n coins that you want to form in a
staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that
can be formed.

n is a non-negative integer and fits within the range of
a 32-bit signed integer.

Example 1:
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.


Example 2:
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.


"""


class Solution:

    def arrangeCoins(self, n: int) -> int:
        if 0 <= n <= 1:
            return n

        sum, start, end = 0, 1, n

        while start < end:
            mid = start + (end - start) // 2
            sum = get_sum(mid)

            if sum > n:
                end = mid - 1
            elif sum == n:
                return mid
            elif sum < n:
                start = mid + 1
                
        if get_sum(start) > n:
            return start - 1
        if start == end:
            return start

    def arrangeCoins_1(self, n: int) -> int:
        sum, i = 0, 1

        while True:
            sum += i
            if sum > n:
                return i - 1
            elif sum == n:
                return i
            else:
                i += 1


def get_sum(mid: int) -> int:
    return mid * (mid + 1) // 2


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    """
    test(solution.arrangeCoins(0), 0)

    test(solution.arrangeCoins(1), 1)
    """
    test(solution.arrangeCoins(2), 1)

    test(solution.arrangeCoins(3), 2)
    test(solution.arrangeCoins(4), 2)
    test(solution.arrangeCoins(5), 2)

    test(solution.arrangeCoins(6), 3)
    test(solution.arrangeCoins(7), 3)
    test(solution.arrangeCoins(8), 3)
    test(solution.arrangeCoins(9), 3)

    test(solution.arrangeCoins(10), 4)
    test(solution.arrangeCoins(11), 4)
    test(solution.arrangeCoins(12), 4)
    test(solution.arrangeCoins(13), 4)
    test(solution.arrangeCoins(14), 4)

    test(solution.arrangeCoins(15), 5)
    test(solution.arrangeCoins(16), 5)
    test(solution.arrangeCoins(17), 5)
    test(solution.arrangeCoins(18), 5)
    test(solution.arrangeCoins(19), 5)
    test(solution.arrangeCoins(20), 5)

    test(solution.arrangeCoins(21), 6)
    test(solution.arrangeCoins(22), 6)
    test(solution.arrangeCoins(23), 6)
    test(solution.arrangeCoins(24), 6)
    test(solution.arrangeCoins(25), 6)
    test(solution.arrangeCoins(26), 6)
    test(solution.arrangeCoins(27), 6)

    test(solution.arrangeCoins(28), 7)
    test(solution.arrangeCoins(29), 7)
    test(solution.arrangeCoins(30), 7)
    test(solution.arrangeCoins(31), 7)
    test(solution.arrangeCoins(32), 7)
    test(solution.arrangeCoins(33), 7)
    test(solution.arrangeCoins(34), 7)
    test(solution.arrangeCoins(35), 7)

    test(solution.arrangeCoins(36), 8)
    test(solution.arrangeCoins(37), 8)
    test(solution.arrangeCoins(38), 8)
    test(solution.arrangeCoins(39), 8)
    test(solution.arrangeCoins(40), 8)
    test(solution.arrangeCoins(41), 8)
    test(solution.arrangeCoins(42), 8)
    test(solution.arrangeCoins(43), 8)
    test(solution.arrangeCoins(44), 8)

    test(solution.arrangeCoins(45), 9)
    test(solution.arrangeCoins(46), 9)
    test(solution.arrangeCoins(47), 9)
    test(solution.arrangeCoins(48), 9)
    test(solution.arrangeCoins(49), 9)
    test(solution.arrangeCoins(50), 9)
    test(solution.arrangeCoins(51), 9)
    test(solution.arrangeCoins(52), 9)
    test(solution.arrangeCoins(53), 9)
    test(solution.arrangeCoins(54), 9)

    test(solution.arrangeCoins(55), 10)
