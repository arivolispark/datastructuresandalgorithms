"""
Title:  Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

"""


from collections import deque


class MinStack:

    def __init__(self):
        self.stack, self.minimum_stack = deque(), deque()

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            min_value = x
        else:
            if x < self.minimum_stack[-1]:
                min_value = x
            else:
                min_value = self.minimum_stack[-1]

        self.stack.append(x)
        self.minimum_stack.append(min_value)

    def pop(self) -> None:
        self.minimum_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    min_stack = MinStack()

    min_stack.push(-2);
    min_stack.push(0);
    min_stack.push(-3);

    min_param = min_stack.getMin();  #--> Returns - 3
    print("\n min_param: ", min_param)

    min_stack.pop();

    top_param = min_stack.top();  #--> Returns 0
    print("\n top_param: ", top_param)

    min_param = min_stack.getMin();  #--> Returns - 2
    print("\n min_param: ", min_param)

    # TEST CASE 1:
    """    
    
    #[null, null, null, null, 2147483647, null, 2147483646, null, 2147483646, null, null, 2147483647, 2147483647, null,
    # -2147483648, -2147483648, null, 2147483647]

    min_stack.push(2147483646)  # null
    min_stack.push(2147483646)  # null
    min_stack.push(2147483647)  # null
    min_stack.top()  # 2147483647

    min_stack.pop()  # null
    min_stack.getMin()  # 2147483646
    min_stack.pop()  # null
    min_stack.getMin()  # 2147483646

    min_stack.pop()  # null
    min_stack.push(2147483647)  # null
    min_stack.top()  # 2147483647
    min_stack.getMin()  # 2147483647

    min_stack.push(-2147483648)  # null
    min_stack.top()  # -2147483648
    min_stack.getMin()  # -2147483648
    min_stack.pop()  # null

    min_stack.getMin()  # 2147483647
    """

    # TEST CASE 2:

    """
    ["MinStack", "push", "push", "getMin", "getMin", "push", "getMin", "getMin", "top", "getMin", "pop", "push", "push",
     "getMin", "push", "pop", "top", "getMin", "pop"]
    [[], [-10], [14], [], [], [-20], [], [], [], [], [], [10], [-7], [], [-7], [], [], [], []]
    """

    """
    
    min_stack.push(-10)  # null
    min_stack.push(14)  # null
    min_stack.getMin()  # -10
    min_stack.getMin()  # -10

    min_stack.push(-20)  # null
    min_stack.getMin()  # -20
    min_stack.getMin()  # -20
    min_stack.top()  # -20

    min_stack.getMin()  # -20
    min_stack.pop()  # null
    min_stack.push(-10)  # null
    min_stack.push(-7)  # null

    min_stack.getMin()  # -10
    min_stack.push(-10)  # null
    min_stack.pop()  # null
    min_stack.top()  # -7

    min_stack.getMin()  # -10
    min_stack.pop()  # null

    # [null,null,null,-10,-10,null,-20,-20,-20,-20,null,null,null,-10,null,null,-7,-10,null]
    
    """
