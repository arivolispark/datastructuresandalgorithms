class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = [[rStart, cStart]]
        
        if rows * cols == 1:
            return result

        k = 1
        while True:
            d_x_y_k = [
                [0, 1, k], 
                [1, 0, k], 
                [0, -1, k + 1], 
                [-1, 0, k + 1]
            ]

            for dr, dc, dk in d_x_y_k:
                for _ in range(dk):
                    rStart += dr
                    cStart += dc

                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        result.append([rStart, cStart])

                        if len(result) == rows * cols:
                            return result
            k += 2
