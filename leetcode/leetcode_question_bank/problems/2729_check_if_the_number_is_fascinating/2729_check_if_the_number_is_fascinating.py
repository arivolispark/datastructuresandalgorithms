from typing import List

class Solution:
    def isFascinating(self, n: int) -> bool:
        digit_frequency_map = {}

        l1 = get_digits(n)
        l2 = get_digits(2 * n)
        l3 = get_digits(3 * n)

        if l1:
            for i in range(len(l1)):
                if is_zero(l1[i]):
                    return False
                if is_exists(digit_frequency_map, l1[i]):
                    return False
                digit_frequency_map[l1[i]] = 1

        if l2:
            for i in range(len(l2)):
                if is_zero(l2[i]):
                    return False
                if is_exists(digit_frequency_map, l2[i]):
                    return False
                digit_frequency_map[l2[i]] = 1

        if l3:
            for i in range(len(l3)):
                if is_zero(l3[i]):
                    return False
                if is_exists(digit_frequency_map, l3[i]):
                    return False
                digit_frequency_map[l3[i]] = 1

        return True


def is_exists(map: dict, d: int) -> bool:
    if map:
        if d in map:
            return True
        else:
            False

def is_zero(d: int) -> bool:
    return True if d == 0 else False

def get_digits(n: int) -> List[int]:
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits
