"""
Title:  Logger Rate Limiter

Design a logger system that receive stream of messages along with its timestamps, each
message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message
should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true;

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;

"""


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map0_10, self.map10_20 = {}, {}
        self.t = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        if timestamp >= self.t + 10:
            self.map10_20 = self.map0_10
            self.map0_10 = {}
            self.t = timestamp

        if message in self.map0_10:
            return False
        if message in self.map10_20 and timestamp < self.map10_20[message] + 10:
            return False
        self.map0_10[message] = timestamp
        return True


def get_test_case_1():
    logger = Logger()

    logger.shouldPrintMessage(1, "foo")
    logger.shouldPrintMessage(2, "bar")
    logger.shouldPrintMessage(3, "foo")
    logger.shouldPrintMessage(8, "bar")
    logger.shouldPrintMessage(10, "foo")
    logger.shouldPrintMessage(11, "foo")


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    get_test_case_1()
