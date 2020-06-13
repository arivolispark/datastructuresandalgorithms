"""
Title:  Insert Delete GetRandom O(1)

Design a data structure that supports all following operations
in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements.
Each element must have the same probability of being returned.


Example:
// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();

"""


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value_set = set()
        self.values = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.value_set:
            self.value_set.add(val)
            self.values.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.value_set:
            self.value_set.remove(val)
            if val in self.values:
                self.values.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


def get_test_case_1():
    obj = RandomizedSet()

    val = 1

    param_1 = obj.insert(val)
    param_2 = obj.remove(val)
    param_3 = obj.getRandom()


def get_test_case_2():
    obj = RandomizedSet()

    """
["RandomizedSet","insert","remove","insert","getRandom","remove","insert","getRandom"]
[[],[1],[2],[2],[],[1],[2],[]]
    """

    obj.insert(1)
    obj.remove(2)
    obj.insert(2)
    random_value = obj.getRandom()
    print(random_value)

    obj.remove(1)
    obj.insert(2)
    random_value = obj.getRandom()
    print(random_value)


def get_test_case_3():
    """
    Input:  ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    [[], [1], [2], [2], [], [1], [2], []]
    Output:  [null,true,false,true,1,false,false,2]
    Expected:  [null,true,false,true,2,true,false,2]
    """

    obj = RandomizedSet()

    obj.insert(1)
    obj.remove(2)
    obj.insert(2)
    random_value = obj.getRandom()
    print(random_value)

    obj.remove(1)
    obj.insert(2)
    random_value = obj.getRandom()
    print(random_value)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    #get_test_case_1()
    #get_test_case_2()
    get_test_case_3()
