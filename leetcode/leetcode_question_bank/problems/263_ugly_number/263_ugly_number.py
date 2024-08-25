class Solution:
    def isUgly(self, n: int) -> bool:
        prime_factor = [2, 3, 5]

        if n == 0:
            return False

        for a in prime_factor:
            while n % a == 0:
                n //= a

        return n == 1
