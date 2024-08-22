class Solution:
    def findComplement(self, num: int) -> int:
        b_length = num.bit_length()
        mask = (1 << b_length) - 1
        return num ^ mask
