import sys
sys.set_int_max_str_digits(0)

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        n1 = int(num1)
        n2 = int(num2)
        addition = n1 + n2
        result = get_digits(addition)
        return ''.join(result)


def get_digits(num: int) -> List[int]:
    result = []
    if num == 0:
        return "0"
    while num > 0:
        digit = num % 10
        result.append(str(digit))
        num //= 10
    result = result[::-1]
    return result
