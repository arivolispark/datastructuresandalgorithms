class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        result = -1
        min_cities_count = n
        distance = floyd_warshall(n, edges, distanceThreshold)

        for i in range(n):
            cities_count = sum(distance[i][j] <= distanceThreshold for j in range(n))
            if cities_count <= min_cities_count:
                result = i
                min_cities_count = cities_count
        return result

def floyd_warshall(n: int, edges: List[List[int]], distanceThreshold: int) -> List[List[int]]:
    distance = [[distanceThreshold + 1] * n for _ in range(n)]

    for i in range(n):
        distance[i][i] = 0

    for source, destination, weight in edges:
        distance[source][destination] = weight
        distance[destination][source] = weight

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    return distance
