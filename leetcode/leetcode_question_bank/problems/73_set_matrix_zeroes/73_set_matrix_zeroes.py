class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        result = []
        rows = len(matrix)
        columns = len(matrix[0])

        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == 0:
                    result.append([i,j])

        for i in range(len(result)):
            r, c = result[i][0], result[i][1]

            for j in range(columns):
                matrix[r][j] = 0
            for k in range(rows):
                matrix[k][c] = 0
