"""
Title:  Implement Rand10() Using Rand7()

Given the API rand7 which generates a uniform random integer in the range 1 to 7, write a
function rand10 which generates a uniform random integer in the range 1 to 10. You can only
call the API rand7 and you shouldn't call any other API. Please don't use the system's Math.random().

Notice that Each test case has one argument n, the number of times that your implemented
function rand10 will be called while testing.


Follow up:
1) What is the expected value for the number of calls to rand7() function?
2) Could you minimize the number of calls to rand7()?



Example 1:
Input: n = 1
Output: [2]


Example 2:
Input: n = 2
Output: [2,8]


Example 3:
Input: n = 3
Output: [3,8,10]


Constraints:
1) 1 <= n <= 10 ^ 5

"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import random


class Solution:

    def rand10(self):
        """
        :rtype: int
        """
        v1, v2 = rand7(), rand7()
        while v1 > 5:
            v1 = rand7()
        while v2 == 7:
            v2 = rand7()
        return v1 if (v2 <= 3) else (v1 + 5)


def rand7() -> int:
    return random.randint(1, 7)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.rand10(), 3)
