"""
Title:  1404. Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s, return the number of steps to
reduce it to 1 under the following rules:
1) If the current number is even, you have to divide it by 2.
2) If the current number is odd, you have to add 1 to it.

It is guaranteed that you can always reach one for all test cases.



Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14.
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.
Step 5) 4 is even, divide by 2 and obtain 2.
Step 6) 2 is even, divide by 2 and obtain 1.


Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.


Example 3:
Input: s = "1"
Output: 0


Constraints:
1) 1 <= s.length <= 500
2) s consists of characters '0' or '1'
3) s[0] == '1'

"""


class Solution:

    def numSteps(self, s: str) -> int:
        count = 0
        str_val = int(s)

        val = 0
        i = 0
        while str_val > 0:
            val += (2 ** i) * (str_val % 10)
            str_val //= 10
            i += 1

        while val > 1:
            if val % 2 == 1:
                val += 1
            else:
                val //= 2
            count += 1
        return count


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.numSteps("1101"), 6)
    test(solution.numSteps("10"), 1)
    test(solution.numSteps("1"), 0)
