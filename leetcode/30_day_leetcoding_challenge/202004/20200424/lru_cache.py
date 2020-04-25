"""
Title:  LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should
support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in
the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the
cache reached its capacity, it should invalidate the least recently used item before
inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?


Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.operation_id = 0
        self.cache_map = {}
        self.lru_map = {}

    def get(self, key: int) -> int:
        if key in self.cache_map:
            self.lru_map[key] = self.operation_id
            self.operation_id += 1
            return self.cache_map[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map[key] = value
        else:
            if len(self.cache_map) >= self.capacity:
                least_recently_used_key = min(self.lru_map.keys(), key=lambda k: self.lru_map[k])
                self.cache_map.pop(least_recently_used_key)
                self.lru_map.pop(least_recently_used_key)
            self.cache_map[key] = value
        self.lru_map[key] = self.operation_id
        self.operation_id += 1


def get_test_case_1() -> (int, int):
    lru_cache = LRUCache(None)
    print("\n lru_cache: ", lru_cache)


def get_test_case_2() -> (int, int):
    lru_cache = LRUCache(-1)
    print("\n lru_cache: ", lru_cache)


def get_test_case_3() -> (int, int):
    lru_cache = LRUCache(0)
    print("\n lru_cache: ", lru_cache)


def get_test_case_4() -> (int, int):
    lru_cache = LRUCache(1)
    print("\n lru_cache: ", lru_cache)


def get_test_case_5() -> (int, int):
    lru_cache = LRUCache(6)
    print("\n lru_cache: ", lru_cache)

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    lru_cache.put(3, 3)
    lru_cache.put(4, 4)
    lru_cache.put(5, 5)
    lru_cache.put(6, 6)
    print("\n lru_cache: ", lru_cache)


def get_test_case_6() -> (int, int):
    lru_cache = LRUCache(2)
    print("\n lru_cache: ", lru_cache)

    lru_cache.put(1, 1)
    lru_cache.put(2, 2)

    value = lru_cache.get(1)
    print("\n lru_cache.get(1): ", value)

    lru_cache.put(3, 3)

    value = lru_cache.get(2)
    print("\n lru_cache.get(2): ", value)

    lru_cache.put(4, 4)

    value = lru_cache.get(1)
    print("\n lru_cache.get(1): ", value)

    value = lru_cache.get(3)
    print("\n lru_cache.get(3): ", value)

    value = lru_cache.get(4)
    print("\n lru_cache.get(4): ", value)


def get_test_case_7() -> (int, int):
    lru_cache = LRUCache(1)
    print(" null")

    lru_cache.put(2, 1)
    print(" null")
    value = lru_cache.get(2)
    print(" lru_cache.get(2): ", value)

    lru_cache.put(3, 2)
    print(" null")

    value = lru_cache.get(2)
    print(" lru_cache.get(2): ", value)

    value = lru_cache.get(3)
    print(" lru_cache.get(3): ", value)


'''
["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
'''

def get_test_case_8() -> (int, int):
    lru_cache = LRUCache(2)
    print(" null")

    value = lru_cache.get(2)
    print(" lru_cache.get(2): ", value)

    lru_cache.put(2, 6)
    print(" null")

    value = lru_cache.get(1)
    print(" lru_cache.get(1): ", value)

    lru_cache.put(1, 5)
    print(" null")

    lru_cache.put(1, 2)
    print(" null")

    value = lru_cache.get(1)
    print(" lru_cache.get(1): ", value)

    value = lru_cache.get(2)
    print(" lru_cache.get(2): ", value)


'''
["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
'''


if __name__ == "__main__":
    #get_test_case_1()
    #get_test_case_2()
    #get_test_case_3()
    #get_test_case_4()
    #get_test_case_5()
    #get_test_case_6()
    get_test_case_7()
    #get_test_case_8()

    """
    lru_cache = LRUCache(2);

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1); // returns 1
    cache.put(3, 3); // evicts key 2
    cache.get(2); // returns - 1(not found)
    cache.put(4, 4); // evicts key 1
    cache.get(1); // returns - 1(not found)
    cache.get(3); // returns 3
    cache.get(4); // returns 4

    result = solution.rangeBitwiseAnd(m, n)
    print("\n result: ", result)
    """
