class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        teamSkill = sum(skill) // (n // 2)
        result = 0
        count = collections.Counter(skill)

        for s, freq in count.items():
            requiredSkill = teamSkill - s
            if count[requiredSkill] != freq:
                return -1
            result += s * requiredSkill * freq

        return result // 2
