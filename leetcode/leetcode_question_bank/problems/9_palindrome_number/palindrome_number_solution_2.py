class Solution:
    def isPalindrome(self, x: int) -> bool:
        input_str = str(x)
        start, end = 0, len(input_str) - 1

        while start < end:
            if input_str[start] != input_str[end]:
                return False
            start += 1
            end -= 1
        return True
