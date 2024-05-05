class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_required = 0
        if tickets:
            while tickets[k] > 0:
                for i in range(len(tickets)):
                    if tickets[i] > 0:
                        tickets[i] -= 1
                        time_required += 1
                    if tickets[k] == 0:
                        break
        return time_required
