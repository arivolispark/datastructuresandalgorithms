"""
Title:  First Unique Number

You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

1) FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
2) int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
3) void add(int value) insert value to the queue.



Example 1:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output:
[null,2,null,2,null,3,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1


Example 2:

Input:
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output:
[null,-1,null,null,null,null,null,17]

Explanation:
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17


Example 3:

Input:
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output:
[null,809,null,-1]

Explanation:
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1


Constraints:

1) 1 <= nums.length <= 10^5
2) 1 <= nums[i] <= 10^8
3) 1 <= value <= 10^8
4) At most 50000 calls will be made to showFirstUnique and add.
"""

from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.number_frequency_map = {}

        if nums:
            for num in nums:
                self.add(num)

    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.number_frequency_map[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def add(self, value: int) -> None:
        if value not in self.number_frequency_map:
            self.number_frequency_map[value] = 1
            self.q.append(value)
        else:
            self.number_frequency_map[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


def get_test_case_1() -> List[int]:
    return [0, 1, 2]


def get_test_case_2() -> List[int]:
    return [0, 1, 2, 0]


def get_test_case_3() -> List[int]:
    return [0, 1, 2, 0, 2]


def get_test_case_4():
    nums = [2, 3, 5]
    firstUnique = FirstUnique(nums)
    firstUnique.showFirstUnique()
    firstUnique.add(5)
    firstUnique.showFirstUnique()
    firstUnique.add(2)
    firstUnique.showFirstUnique()
    firstUnique.add(3)
    firstUnique.showFirstUnique()


def get_test_case_5():
    nums = [7,7,7,7,7,7]
    firstUnique = FirstUnique(nums)
    firstUnique.showFirstUnique()
    firstUnique.add(7)
    firstUnique.add(3)
    firstUnique.add(3)
    firstUnique.add(7)
    firstUnique.add(17)
    firstUnique.showFirstUnique()


def get_test_case_6():
    nums = [809]
    firstUnique = FirstUnique(nums)
    firstUnique.showFirstUnique()
    firstUnique.add(809)
    firstUnique.showFirstUnique()


def get_test_case_7():
    #["FirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique"]
    #[[[7, 7, 7, 7, 7, 7]], [], [7], [3], [3], [7], [17], []]

    nums = [7, 7, 7, 7, 7, 7]
    firstUnique = FirstUnique(nums)
    firstUnique.showFirstUnique()
    firstUnique.add(7)
    firstUnique.add(3)
    firstUnique.add(3)
    firstUnique.add(7)
    firstUnique.add(17)
    firstUnique.showFirstUnique()


def get_test_case_8():
    """
    ["FirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "showFirstUnique", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "showFirstUnique",
     "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "showFirstUnique", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "showFirstUnique", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "showFirstUnique", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add",
     "add", "add", "add", "showFirstUnique", "showFirstUnique", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "showFirstUnique", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "showFirstUnique", "showFirstUnique", "add",
     "add", "showFirstUnique", "add", "add", "showFirstUnique", "showFirstUnique", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add",
     "showFirstUnique", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add",
     "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique",
     "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique", "add",
     "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "add", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "showFirstUnique", "showFirstUnique",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "showFirstUnique",
     "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "showFirstUnique", "add", "showFirstUnique",
     "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "showFirstUnique", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "add", "add", "showFirstUnique", "showFirstUnique", "add", "add", "add", "add", "add", "add", "add",
     "add", "add", "showFirstU... 980846 more chars
    """


if __name__ == "__main__":
    #get_test_case_1()
    #get_test_case_2()
    #get_test_case_3()
    #get_test_case_4()
    #get_test_case_5()
    #get_test_case_6()
    get_test_case_7()
    #get_test_case_8()
