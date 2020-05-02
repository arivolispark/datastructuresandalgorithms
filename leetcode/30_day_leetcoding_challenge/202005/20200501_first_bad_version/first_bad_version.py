"""
Title: First Bad Version

You are a product manager and currently leading a team to
develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is
developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to
find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will
return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls
to the API.


Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

from typing import List


class Solution:

    # The isBadVersion API is already defined for you.
    # @param version, an integer
    # @return a bool
    def isBadVersion(self, version: int) -> bool:
        return version > 50

    def firstBadVersion(self, n) -> int:
        """
        :type n: int
        :rtype: int
        """

        if type(n) is int:
            start, end = 0, n

            while start <= end:
                mid = start + (end - start) // 2
                if self.isBadVersion(mid):
                    end = mid - 1
                else:
                    start = mid + 1
            return start
        return -1


def binary_search(nums: List[int], key: int) -> int:
    if nums and type(key) is int:
        start, end = 0, len(nums)
        if end == 0:
            return -1

        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == key:
                return mid
            elif nums[mid] < key:
                start = mid + 1
            else:
                end = mid
    return -1


def get_test_case_1() -> (List[int], int):
    return None, None


def get_test_case_2() -> (List[int], int):
    return [], None


def get_test_case_3() -> (List[int], int):
    return None, 8


def get_test_case_4() -> (List[int], int):
    return [], 8


def get_test_case_5() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 0
    return nums, key


def get_test_case_6() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 1
    return nums, key


def get_test_case_7() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 2
    return nums, key


def get_test_case_8() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 3
    return nums, key


def get_test_case_9() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 4
    return nums, key


def get_test_case_10() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 5
    return nums, key


def get_test_case_11() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 6
    return nums, key


def get_test_case_12() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 7
    return nums, key


def get_test_case_13() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 8
    return nums, key


def get_test_case_14() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 9
    return nums, key


def get_test_case_15() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = -2
    return nums, key


def get_test_case_16() -> (List[int], int):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    key = 20
    return nums, key


if __name__ == "__main__":
    solution = Solution()
    #version = 10
    #print("\n version: ", version)

    print("\n solution.isBadVersion(100): ", solution.isBadVersion(100))
    print(" solution.isBadVersion(49): ", solution.isBadVersion(49))
    print(" solution.isBadVersion(50): ", solution.isBadVersion(50))
    print(" solution.isBadVersion(51): ", solution.isBadVersion(51))
    print(" solution.isBadVersion(91): ", solution.isBadVersion(91))

    result = solution.firstBadVersion(100)
    print("\n result: ", result)

    """
    #nums, key = get_test_case_1()
    #nums, key = get_test_case_2()
    #nums, key = get_test_case_3()
    #nums, key = get_test_case_4()
    #nums, key = get_test_case_5()
    #nums, key = get_test_case_6()
    #nums, key = get_test_case_7()
    #nums, key = get_test_case_8()
    #nums, key = get_test_case_9()
    #nums, key = get_test_case_10()
    #nums, key = get_test_case_11()
    #nums, key = get_test_case_12()
    #nums, key = get_test_case_13()
    #nums, key = get_test_case_14()
    #nums, key = get_test_case_15()
    nums, key = get_test_case_16()
    print("\n nums: ", nums)
    print(" key: ", key)

    index = binary_search(nums, key)
    print("\n index: ", index)
    """
