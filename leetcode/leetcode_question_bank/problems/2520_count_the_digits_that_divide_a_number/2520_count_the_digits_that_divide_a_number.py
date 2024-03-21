class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        digits = get_digits(num)
        for i in range(len(digits)):
            if num % digits[i] == 0:
                count += 1
        return count


def get_digits(num: int) -> List[int]:
    digits = []

    while num > 0:
        digit = num % 10
        if digit != 0:
            digits.append(num % 10)
        num //= 10

    return digits
