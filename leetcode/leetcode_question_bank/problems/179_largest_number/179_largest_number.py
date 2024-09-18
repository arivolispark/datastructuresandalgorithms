class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_as_str = [str(num) for num in nums]
      
        nums_as_str.sort(key=cmp_to_key(self._compare_numbers))
      
        # Special case: if the highest number is "0", the result is "0"
        # (happens when all numbers are zeros)
        if nums_as_str[0] == "0":
            return "0"
      
        return "".join(nums_as_str)

    def _compare_numbers(self, a: str, b: str) -> int:
        if a + b < b + a:
            return 1
        else:
            return -1
