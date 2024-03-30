class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        total_liters = 0

        while mainTank >= 5:
            mainTank -= 5
            total_liters += 5

            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1

        total_liters += mainTank

        return total_liters * 10
