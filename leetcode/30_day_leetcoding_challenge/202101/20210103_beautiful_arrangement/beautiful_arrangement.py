class Solution:
    def countArrangement(self, n: int) -> int:
        all = (1 << n) - 1
        result = [0] * all

        def permutation(tmp, k, answer):
            if tmp == all:
                return 1
            if answer[tmp] > 0:
                return answer[tmp]
            score = 0
            for i in range(1, n + 1):
                if (tmp & (1 << (i - 1))) == 0:
                    if (k % i == 0) or (i % k == 0):
                        score += permutation(tmp + (1 << (i - 1)), k + 1, answer)
            answer[tmp] = score
            return score
        score = permutation(0, 1, result)
        return score

