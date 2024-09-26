"""
Title:  729. My Calendar I

You are implementing a program to use as your calendar. We can add a new event if adding the
event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment
is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on
the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully
without causing a double booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]

Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.


Constraints:
1) 0 <= start < end <= 109
2) At most 1000 calls will be made to book.

"""

from typing import List


class MyCalendar:

    def __init__(self):
        self.timeline = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.timeline:
            if max(start, s) < min(end, e):
                return False

        self.timeline.append((start, end))
        return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def test_case_1() -> List[bool]:
    myCalendar = MyCalendar()
    result = []

    result.append(myCalendar.book(10, 20))
    result.append(myCalendar.book(15, 25))
    result.append(myCalendar.book(20, 30))

    return result


def test_case_2() -> List[bool]:
    myCalendar = MyCalendar()
    result = []

    result.append(myCalendar.book(48, 50))
    result.append(myCalendar.book(0, 6))
    result.append(myCalendar.book(6, 13))
    result.append(myCalendar.book(8, 13))
    result.append(myCalendar.book(15, 23))
    result.append(myCalendar.book(49, 50))
    result.append(myCalendar.book(45, 50))
    result.append(myCalendar.book(29, 34))
    result.append(myCalendar.book(3, 12))
    result.append(myCalendar.book(38, 44))

    return result


if __name__ == "__main__":
    myCalendar = MyCalendar()

    test(test_case_1(), [True, False, True])
    test(test_case_2(), [True, True, True, False, True, False, False, True, False, True])
