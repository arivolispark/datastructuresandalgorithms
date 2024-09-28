"""
Title:  641. Design Circular Deque

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if
the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the
operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true
 if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if
the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque
is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.


Example 1:

Input
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear",
"isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 2, true, true, true, 4]

Explanation
MyCircularDeque myCircularDeque = new MyCircularDeque(3);
myCircularDeque.insertLast(1);  // return True
myCircularDeque.insertLast(2);  // return True
myCircularDeque.insertFront(3); // return True
myCircularDeque.insertFront(4); // return False, the queue is full.
myCircularDeque.getRear();      // return 2
myCircularDeque.isFull();       // return True
myCircularDeque.deleteLast();   // return True
myCircularDeque.insertFront(4); // return True
myCircularDeque.getFront();     // return 4


Constraints:
1) 1 <= k <= 1000
2) 0 <= value <= 1000
3) At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.

"""

class MyCircularDeque:

    def __init__(self, k: int):
        self.max_size = k
        self.q = []

    def insertFront(self, value: int) -> bool:
        if len(self.q) < self.max_size:
            self.q.insert(0, value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.q) < self.max_size:
            self.q.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q.pop(0)
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q.pop()
            return True

    def getFront(self) -> int:
        return self.q[0] if len(self.q) > 0 else -1

    def getRear(self) -> int:
        return self.q[-1] if len(self.q) > 0 else -1

    def isEmpty(self) -> bool:
        return True if len(self.q) == 0 else False

    def isFull(self) -> bool:
        return True if len(self.q) == self.max_size else False


def test_case_1():
    myCircularDeque = MyCircularDeque(3)
    result = []

    result.append(myCircularDeque.insertLast(1))  # return True
    result.append(myCircularDeque.insertLast(2))  # return True
    result.append(myCircularDeque.insertFront(3))  # return True
    result.append(myCircularDeque.insertFront(4))  # return False, the queue is full.
    result.append(myCircularDeque.getRear())  # return 2
    result.append(myCircularDeque.isFull())  # return True
    result.append(myCircularDeque.deleteLast())  # return True
    result.append(myCircularDeque.insertFront(4))  # return True
    result.append(myCircularDeque.getFront())  # return 4

    return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    myCircularDeque = MyCircularDeque(3)

    test(test_case_1(), [True, True, True, False, 2, True, True, True, 4])
