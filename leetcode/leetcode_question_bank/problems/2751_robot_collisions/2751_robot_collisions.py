class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        stack = []
        
        for _, i in sorted((p, i) for i, p in enumerate(positions)):
            if directions[i] == 'R':
                stack.append(i)
            else:
                while stack and healths[i]:
                    if healths[i] > healths[stack[-1]]:
                        healths[stack.pop()] = 0
                        healths[i] -= 1
                    elif healths[i] == healths[stack[-1]]:
                        healths[stack.pop()] = 0
                        healths[i] = 0
                    else:
                        healths[i] = 0
                        healths[stack[-1]] -= 1
        return [health for health in healths if health > 0]
