class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        count = collections.Counter(digits)

        for a in range(1, 10):
            for b in range(0, 10):
                for c in range(0, 9, 2):
                    if count[a] > 0 and count[b] > (b == a) and count[c] > (c == a) + (c == b):
                        result.append(a * 100 + b * 10 + c)

        return result
