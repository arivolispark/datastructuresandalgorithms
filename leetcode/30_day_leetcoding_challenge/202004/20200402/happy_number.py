"""
Title: Happy Number


Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Example 1:

Input: 19
Output: true

Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

"""


class Solution:

    def is_happy_number(self, n: int) -> bool:
        slow, fast = n, n
        while True:
            fast = calculate_digit_square_sum(calculate_digit_square_sum(fast))
            slow = calculate_digit_square_sum(slow)

            if fast == slow:
                break

        return fast == 1


def calculate_digit_square_sum(n):
    digit_square_sum = 0
    while n > 0:
        digit = n % 10
        digit_square_sum += digit ** 2
        n //= 10
    return digit_square_sum


if __name__ == "__main__":
    """
    Examples of Happy numbers = [19, 23 ] 
    Examples of non-Happy numbers = [12] 
    """
    solution = Solution()
    print("\n solution.is_happy_number(19): ", solution.is_happy_number(19))
    print(" solution.is_happy_number(23): ", solution.is_happy_number(23))
    print(" solution.is_happy_number(12): ", solution.is_happy_number(12))
