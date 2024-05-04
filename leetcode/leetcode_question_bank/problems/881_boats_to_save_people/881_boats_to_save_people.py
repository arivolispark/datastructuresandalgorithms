class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        number_of_boats = 0
        i, j = 0, len(people) - 1

        people.sort()

        while i <= j:
            difference = limit - people[j]
            j -= 1

            if people[i] <= difference:
                i += 1

            number_of_boats += 1

        return number_of_boats
