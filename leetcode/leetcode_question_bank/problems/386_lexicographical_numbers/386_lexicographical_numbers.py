class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1

        while len(result) < n:
            result.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr == n:
                    curr //= 10
                curr += 1

        return result
