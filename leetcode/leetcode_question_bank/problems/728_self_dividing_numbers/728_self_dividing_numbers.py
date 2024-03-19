class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right + 1):
            digits = get_digits(i)
            if len(digits) > 0:
                if self_dividing_test(i, digits):
                    result.append(i)
        return result

def self_dividing_test(number: int, digits: List[int]) -> bool: 
    if number > 0 and len(digits) > 0:
        for i in range(len(digits)):
            if number % digits[i] != 0:
                return False
        return True

def get_digits(number: int) -> List[int]:
    digits = []
    while number > 0:
        digit = number % 10
        if digit == 0:
            return []
        else:
            digits.append(digit)
        number //= 10 
    return digits
