class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        result = 0
        length = len(position)

        position.sort()

        start, end = 0, position[length - 1]
        
        while start <= end:
            mid = (start + end) // 2
            if is_enough_distance(position, mid, m):
                result = mid
                start = mid + 1
            else:
                end = mid - 1

        return result

    
def is_enough_distance(position, mid, m):
    start = 1
    prev = position[0]

    for i in range(1, len(position)):
        if (position[i] - prev >= mid):
            start += 1
            prev = position[i]

            if start == m:
                return True
    
    if start < m:
        return False
