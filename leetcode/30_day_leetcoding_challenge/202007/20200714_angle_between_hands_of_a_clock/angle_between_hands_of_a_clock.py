"""
Title:  Angle Between Hands of a Clock

Given two numbers, hour and minutes. Return the smaller
angle (in degrees) formed between the hour and the minute hand.


Example 1:
Input: hour = 12, minutes = 30
Output: 165


Example 2:
Input: hour = 3, minutes = 30
Output: 75


Example 3:
Input: hour = 3, minutes = 15
Output: 7.5


Example 4:
Input: hour = 4, minutes = 50
Output: 155


Example 5:
Input: hour = 12, minutes = 0
Output: 0


Constraints:
1) 1 <= hour <= 12
2) 0 <= minutes <= 59
3) Answers within 10^-5 of the actual value will be accepted as correct.

"""


class Solution:

    def angleClock(self, hour: int, minutes: int) -> float:
        """
        total_number_of_degrees = 360
        total_number_of_minutes = 60
        degrees_per_minute = total_number_of_degrees / total_number_of_minutes

        total_number_of_hours = 12
        degrees_per_hour = total_number_of_degrees / total_number_of_hours
        """

        minutes_degree = minutes * 6
        hours_degree = ((hour * 30) + (minutes/60 * 30)) % 360
        difference_1 = abs(minutes_degree - hours_degree)

        minutes_difference = min(abs(0 - minutes_degree), abs(360 - minutes_degree))
        hours_difference = min(abs(0 - hours_degree), abs(360 - hours_degree))
        difference_2 = minutes_difference + hours_difference

        return min(difference_1, difference_2)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()

    test(solution.angleClock(12, 30), 165)
    test(solution.angleClock(3, 30), 75)
    test(solution.angleClock(3, 15), 7.5)
    test(solution.angleClock(4, 50), 155)
    test(solution.angleClock(12, 0), 0)
    test(solution.angleClock(1, 57), 76.50000)
    test(solution.angleClock(8, 7), 158.50000)
