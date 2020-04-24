"""
Title:  Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return
the bitwise AND of all numbers in this range, inclusive.


Example 1:
Input: [5,7]
Output: 4


Example 2:
Input: [0,1]
Output: 0

"""


class Solution:

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        result = 0

        while m > 0 and n > 0:
            msb_p1 = most_significant_bit_position(m)
            msb_p2 = most_significant_bit_position(n)

            if msb_p1 != msb_p2:
                break

            # Add 2^msb_p1 to result
            msb_val = (1 << msb_p1)
            result += msb_val

            # subtract 2^msb_p1 from m and n.
            m -= msb_val
            n -= msb_val

        return result


def most_significant_bit_position(n: int):
    msb_p = -1
    while n > 0:
        n = n >> 1
        msb_p += 1
    return msb_p


def get_test_case_1() -> (int, int):
    m, n = 0, 1
    return m, n


def get_test_case_2() -> (int, int):
    m, n = 5, 7
    return m, n


def get_test_case_3() -> (int, int):
    m, n = 1, 10
    return m, n


def get_test_case_4() -> (int, int):
    m, n = 1, 1
    return m, n


def get_test_case_5() -> (int, int):
    m, n = 2, 2
    return m, n


def get_test_case_6() -> (int, int):
    m, n = 3, 3
    return m, n


def get_test_case_7() -> (int, int):
    m, n = 0, 2147483647
    return m, n


def get_test_case_8() -> (int, int):
    m, n = 20000, 2147483647
    return m, n


if __name__ == "__main__":
    solution = Solution()

    #m, n = get_test_case_1()
    #m, n = get_test_case_2()
    #m, n = get_test_case_3()
    #m, n = get_test_case_4()
    #m, n = get_test_case_5()
    #m, n = get_test_case_6()
    #m, n = get_test_case_7()
    m, n = get_test_case_8()
    print("\n m: ", m)
    print(" n: ", n)

    result = solution.rangeBitwiseAnd(m, n)
    print("\n result: ", result)
