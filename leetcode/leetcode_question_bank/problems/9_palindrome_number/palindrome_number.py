"""
Problem #: 9
Title:  Palindrome Number

Determine whether an integer is a palindrome. An integer is a
palindrome when it reads the same backward as forward.


Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Follow up:
Coud you solve it without converting the integer to a string?

"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10
        #print(" digits: ", digits)

        start, end = 0, len(digits) - 1

        while start < end:
            if digits[start] != digits[end]:
                return False
            else:
                start += 1
                end -= 1
        return True


if __name__ == "__main__":
    solution = Solution()

    #x = 0
    x = 6
    #x = 121
    #x = -121
    #x = 10
    #x = 12345

    print("\n x: ", x)

    palindrome_flag = solution.isPalindrome(x)
    print("\n palindrome_flag: ", palindrome_flag)
