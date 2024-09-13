class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        l = len(arr)
        prexor = [0] * (l+1)
        for i in range(1, l+1):
            prexor[i] ^= prexor[i-1] ^ arr[i-1]
        return [prexor[j+1] ^ prexor[i] for i, j in queries]
