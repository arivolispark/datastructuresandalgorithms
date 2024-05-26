class Solution:
    def checkRecord(self, n: int) -> int:
        MODULO = 10 ** 9 + 7

        has_cache = [[[False] * 3 for _ in range(2)] for _ in range(n)]
        cache = [[[None] * 3 for _ in range(2)] for _ in range(n)]

        def count(days, absences, late):
            if days == n:
                return 1

            if has_cache[days][absences][late]:
                return cache[days][absences][late]

            total = 0

            total += count(days + 1, absences, 0)

            if absences + 1 < 2:
                total += count(days + 1, absences + 1, 0)

            if late + 1 < 3:
                total += count(days + 1, absences, late + 1)

            has_cache[days][absences][late] = True
            cache[days][absences][late] = total % MODULO
            return cache[days][absences][late]

        return count(0, 0, 0)
