"""
Title:  Design HashSet

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

1) add(value): Insert a value into the HashSet.
2) contains(value) : Return whether the value exists in the HashSet or not.
3) remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.



Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)


Note:
1) All values will be in the range of [0, 1000000].
2) The number of operations will be in the range of [1, 10000].
3) Please do not use the built-in HashSet library.

"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_buckets = 15000
        self.buckets = [[] for i in range(self.num_buckets)]

    def hash_function(self, key):
        return key % self.num_buckets

    def add(self, key: int) -> None:
        i = self.hash_function(key)
        if not key in self.buckets[i]:
            self.buckets[i].append(key)

    def remove(self, key: int) -> None:
        i = self.hash_function(key)
        if key in self.buckets[i]:
            self.buckets[i].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        i = self.hash_function(key)
        if key in self.buckets[i]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


def get_test_case_1():
    my_hashset = MyHashSet()
    my_hashset.add(1)
    my_hashset.add(2)
    my_hashset.contains(1)
    my_hashset.contains(3)
    my_hashset.add(2)
    my_hashset.contains(2)
    my_hashset.remove(2)
    my_hashset.contains(2)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    get_test_case_1()
