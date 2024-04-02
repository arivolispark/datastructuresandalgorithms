from typing import List

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_of_digits = 0
        digits = get_digits(x)
        if digits:
            for digit in digits:
                sum_of_digits += digit
            
        if x % sum_of_digits == 0:
            return sum_of_digits
        else:
            return -1


def get_digits(x: int) -> List[int]:
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return digits
