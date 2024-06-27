class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        length = len(edges)
        map = {}
        for i in range(length):
            u, v = edges[i]
            map[u] = map.get(u, 0) + 1
            map[v] = map.get(v, 0) + 1
        
        for k, v in map.items():
            if v == length:
                return k
