class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        n = int(num)

        while n > 0:
            if n % 10 == 0:
                n //= 10
            else:
                return str(n)
