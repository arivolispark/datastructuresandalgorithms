
"""
Title:  Find Nearest Right Node in Binary Tree

Given the root of a binary tree and a node u in the tree, return the nearest node on the same 
level that is to the right of u, or return null if u is the rightmost node in its level.

 

Example 1:



Input: root = [1,2,3,null,4,5,6], u = 4
Output: 5
Explanation: The nearest node on the same level to the right of node 4 is node 5.



Example 2:



Input: root = [3,null,4,2], u = 2
Output: null
Explanation: There are no nodes to the right of 2.



Example 3:

Input: root = [1], u = 1
Output: null



Example 4:

Input: root = [3,4,2,null,null,null,1], u = 4
Output: 2
 

Constraints:

1) The number of nodes in the tree is in the range [1, 105].
2) 1 <= Node.val <= 105
3) All values in the tree are distinct.
4) u is a node in the binary tree rooted at root.

"""

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if root is None: 
            return 0 
  
        qn =  []
        q1 = []
  
        level = 0
  
        qn.append(root) 
        q1.append(level) 
  
        while (len(qn) > 0): 
            node = qn.pop(0) 
            level = q1.pop(0) 
  
            if node.val == u.val: 
                if (len(q1) == 0 or q1[0] != level): 
                    return None
  
                return qn[0] 
  
            if node.left is not None: 
                qn.append(node.left) 
                q1.append(level + 1) 
  
            if node.right is not None: 
                qn.append(node.right) 
                q1.append(level + 1) 
  
        return None


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))


if __name__ == "__main__":
    solution = Solution()
