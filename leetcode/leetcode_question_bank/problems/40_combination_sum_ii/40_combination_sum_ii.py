class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # This temp list will store the combination from the current iteration
        combination = []

        candidates.sort()

        # Helper function to perform depth-first search
        def dfs(start_index: int, current_sum: int):
            # If the current sum is 0, we found a valid combination
            if current_sum == 0:
                result.append(combination[:])
                return

            # If the index is out of bounds or the current element is larger than the current_sum, stop recursion
            if start_index >= len(candidates) or current_sum < candidates[start_index]:
                return
          
            for i in range(start_index, len(candidates)):
                # Skip duplicates to avoid repeating the same combination
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue

                # Add the current candidate to the current combination
                combination.append(candidates[i])

                # Recursively call dfs with the next index and the remaining sum
                dfs(i + 1, current_sum - candidates[i])
                
                # Backtrack by removing the last added candidate
                combination.pop()

        dfs(0, target)

        return result
