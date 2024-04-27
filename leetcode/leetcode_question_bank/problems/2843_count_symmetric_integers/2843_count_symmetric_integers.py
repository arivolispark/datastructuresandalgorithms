class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = []
        for i in range(low, high+1, 1):
            digits = get_digits(i)
            if len(digits) % 2 == 0:
                left_half_digits_sum, right_half_digits_sum = 0, 0
                for j in range(len(digits) // 2):
                    left_half_digits_sum += digits[j]
                for j in range(len(digits) // 2, len(digits)):
                    right_half_digits_sum += digits[j]
                if left_half_digits_sum == right_half_digits_sum:
                    result.append(i)
        return len(result)


def get_digits(num: int) -> List[int]:
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    digits = digits[::-1]
    return digits
