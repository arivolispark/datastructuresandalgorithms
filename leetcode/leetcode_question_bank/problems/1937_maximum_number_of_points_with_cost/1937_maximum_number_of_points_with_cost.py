class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, columns = len(points), len(points[0])
        row = points[0]

        for i in range(1, rows):
            current_row = points[i].copy()
            left, right = [0] * columns, [0] * columns

            left[0] = row[0]

            for j in range(1, columns):
                left[j] = max(row[j], left[j - 1] - 1)

            right[columns - 1] = row[columns - 1]
            for j in range(columns - 2, -1, -1):
                right[j] = max(row[j], right[j + 1] - 1)

            for j in range(columns):
                current_row[j] += max(left[j], right[j])
            row = current_row

        return max(row)
