class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        columns = len(colSum)
        result = [[0] * columns for _ in range(rows)]

        for i in range(rows):
            for j in range(columns):
                result[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= result[i][j]
                colSum[j] -= result[i][j]

        return result
