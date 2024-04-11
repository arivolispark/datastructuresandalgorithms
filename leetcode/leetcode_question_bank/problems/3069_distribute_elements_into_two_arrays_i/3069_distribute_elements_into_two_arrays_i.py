class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1, arr2, result = [], [], []

        if nums:
            arr1.append(nums[0])
            arr2.append(nums[1])

            for i in range(2, len(nums)):
                if arr1[-1] > arr2[-1]:
                    arr1.append(nums[i])
                else:
                    arr2.append(nums[i])

            for i in range(len(arr1)):
                result.append(arr1[i])

            for i in range(len(arr2)):
                result.append(arr2[i])

        return result
