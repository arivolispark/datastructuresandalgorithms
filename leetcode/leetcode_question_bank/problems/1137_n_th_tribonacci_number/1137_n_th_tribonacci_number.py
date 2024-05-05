class Solution:
    def tribonacci(self, n: int) -> int:
        map = {}
        map[0] = 0
        map[1] = 1
        map[2] = 1

        for i in range(3, n+1, 1):
            map[i] = map[i-1] + map[i-2] + map[i-3]
        
        return map[n]
