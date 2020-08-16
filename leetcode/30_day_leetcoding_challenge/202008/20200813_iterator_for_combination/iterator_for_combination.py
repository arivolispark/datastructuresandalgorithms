"""
Title:  Iterator for Combination

Design an Iterator class, which has:

1) A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
2) A function next() that returns the next combination of length combinationLength in lexicographical order.
3) A function hasNext() that returns True if and only if there exists a next combination.


Example:

CombinationIterator iterator = new CombinationIterator("abc", 2); // creates the iterator.

iterator.next(); // returns "ab"
iterator.hasNext(); // returns true
iterator.next(); // returns "ac"
iterator.hasNext(); // returns true
iterator.next(); // returns "bc"
iterator.hasNext(); // returns false


Constraints:

1) 1 <= combinationLength <= characters.length <= 15
2) There will be at most 10^4 function calls per test.
3) It's guaranteed that all calls of the function next are valid.

"""


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.q = []

        def get_combination(start: int, length: int, text: str):
            if length == 0:
                self.q.append(text)
                return

            for i in range(start, len(characters) - length + 1):
                get_combination(i + 1, length - 1, text + characters[i])

        get_combination(0, combinationLength, "")

    def next(self) -> str:
        str = self.q[0]
        self.q.pop(0)
        return str

    def hasNext(self) -> bool:
        return len(self.q) > 0


def get_test_case_1():
    combinationIterator = CombinationIterator("abc", 2)
    combinationIterator.next() # "ab"
    combinationIterator.hasNext() # True
    combinationIterator.next() # "ac"
    combinationIterator.hasNext() # True
    combinationIterator.next() # "bc"
    combinationIterator.hasNext() # False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    get_test_case_1()
