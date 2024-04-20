import math

class Solution:
    def convertToBase7(self, num: int) -> str:
        result = []
        base = 7
        flag = 1

        if num == 0:
            return "0"

        if num < 0:
            flag = -1
            num = abs(num)

        while num > 0:
            result.append(str(num % base))
            num //= base

        if flag == -1:
            result.append("-")

        result = result[::-1]
        return ''.join(result)
