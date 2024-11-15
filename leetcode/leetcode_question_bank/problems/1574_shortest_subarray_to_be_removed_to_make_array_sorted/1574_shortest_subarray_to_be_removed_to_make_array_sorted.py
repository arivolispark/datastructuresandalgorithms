class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1

        while l < n - 1 and arr[l] <= arr[l+1]:
            l += 1
        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        result = min(n - 1 - l, r)

        i = l
        j = n - 1
        while i >= 0 and j >= r and j > i:
            if arr[i] <= arr[j]:
                j -= 1
            else:
                i -= 1
            result = min(result, j - i)

        return result
