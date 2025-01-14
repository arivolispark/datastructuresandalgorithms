class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result = []
        map_1, map_2 = {}, {}

        for i in range(len(A)):
            map_1[A[i]] = A[i]
            map_2[B[i]] = B[i]

            match = 0
            for k, v in map_1.items():
                if k in map_2:
                    match += 1
            result.append(match)

        return result
