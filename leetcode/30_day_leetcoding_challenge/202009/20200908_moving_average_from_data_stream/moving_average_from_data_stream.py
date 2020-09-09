"""
Title:  Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all
integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

"""

from collections import deque


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.max_size = size
        self.sum = 0.0

    def next(self, val: int) -> float:
        if len(self.q) == self.max_size:
            self.sum -= self.q[0]
            self.q.popleft()
        self.q.append(val)
        self.sum += val

        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


def get_test_case_1():
    moving_average = MovingAverage(3)

    test(moving_average.next(1), 1)
    test(moving_average.next(10), 5.5)
    test(moving_average.next(3), 4.666666666666667)
    test(moving_average.next(5), 6)


if __name__ == "__main__":
    get_test_case_1()
