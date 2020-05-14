"""
Title:  Remove K Digits


Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number is
the smallest possible.


Note:
1) The length of num is less than 10002 and will be ≥ k.
2) The given num does not contain any leading zero.


Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.


Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.


Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

"""


class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removal_count = k
        for current_digit in num:
            while removal_count and stack and stack[-1] > current_digit:
                stack.pop()
                removal_count -= 1
            stack.append(current_digit)

        result = "".join(stack[0:len(num) - k]).lstrip("0")
        if len(result) == 0:
            return "0"
        else:
            return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.removeKdigits("1432219", 3), "1219")
    test(solution.removeKdigits("10200", 1), "200")
    test(solution.removeKdigits("10", 2), "0")
    test(solution.removeKdigits("9", 1), "0")
    test(solution.removeKdigits("112", 1), "11")
    test(solution.removeKdigits("1234567890", 9), "0")
