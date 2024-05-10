class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        map = {}
        result = []

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                result.append(arr[i] / arr[j])
                map[arr[i] / arr[j]] = [arr[i], arr[j]]

        result.sort()
        return map[result[k-1]]
