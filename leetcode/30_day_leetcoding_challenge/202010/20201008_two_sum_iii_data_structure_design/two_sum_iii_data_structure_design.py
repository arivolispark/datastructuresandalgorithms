"""
Title:  Two Sum III - Data structure design

Design a data structure that accepts a stream of integers and checks
if it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers
whose sum is equal to value, otherwise, it returns false.


Example 1:
Input:
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]
Output:
[null, null, null, null, true, false]



Explanation
TwoSum twoSum = new TwoSum();
twoSum.add(1);   // [] --> [1]
twoSum.add(3);   // [1] --> [1,3]
twoSum.add(5);   // [1,3] --> [1,3,5]
twoSum.find(4);  // 1 + 3 = 4, return true
twoSum.find(7);  // No two integers sum up to 7, return false


Constraints:
1) -105 <= number <= 105
2) -231 <= value <= 231 - 1
3) At most 5 * 104 calls will be made to add and find.

"""


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input_array = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.input_array.append(number)
        self.input_array.sort()

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        if self.input_array:
            low, high = 0, len(self.input_array) - 1

            while low < high:
                two_sum = self.input_array[low] + self.input_array[high]

                if two_sum == value:
                    return True
                elif two_sum < value:
                    low += 1
                elif two_sum > value:
                    high -= 1
            return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


def get_test_case_1():
    twoSum = TwoSum()
    twoSum.add(1)
    twoSum.add(3)
    twoSum.add(5)
    twoSum.find(4)
    test(twoSum.find(4), True)
    test(twoSum.find(7), False)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    get_test_case_1()
