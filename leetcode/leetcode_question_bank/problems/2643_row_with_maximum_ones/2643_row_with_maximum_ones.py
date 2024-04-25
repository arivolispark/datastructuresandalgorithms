class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index, max_count = 0, 0
        result = []
        if mat:
            for i in range(len(mat)):
                count = 0
                for j in range(len(mat[0])):
                    if mat[i][j] == 1:
                        count += 1
                if count > max_count:
                    index = i
                    max_count = count
            result.append(index)
            result.append(max_count)
        return result
