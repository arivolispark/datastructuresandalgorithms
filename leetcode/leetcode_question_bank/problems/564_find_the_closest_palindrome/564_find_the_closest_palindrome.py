class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        num_length = len(n)

        candidates = {
            10 ** (num_length - 1) - 1,  
            10 ** num_length + 1          
        }

        prefix = int(n[:(num_length + 1) // 2])

        for i in range(prefix - 1, prefix + 2):
            j = i if num_length % 2 == 0 else i // 10

            palindrome = i
            while j > 0:
                palindrome = palindrome * 10 + j % 10
                j //= 10

            candidates.add(palindrome)

        candidates.discard(num)

        closest_palindrome = -1
        for candidate in candidates:
            if (closest_palindrome == -1 or
                abs(candidate - num) < abs(closest_palindrome - num) or
                (abs(candidate - num) == abs(closest_palindrome - num) and candidate < closest_palindrome)):
                closest_palindrome = candidate

        return str(closest_palindrome)
