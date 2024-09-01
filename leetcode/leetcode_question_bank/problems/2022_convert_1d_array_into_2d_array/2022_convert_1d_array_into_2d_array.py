class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return [[]]

        answer = []
        i, j = 0, 0

        while i < m:
            row = []
            while j < n:
                row.append(original[j])
                j += 1
                if j == n:
                    answer.append(row)
                    j = 0
                    break
            i += 1
        return answer
