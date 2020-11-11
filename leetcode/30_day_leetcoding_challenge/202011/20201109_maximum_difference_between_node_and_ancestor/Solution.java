/*
Title:  Maximum Difference Between Node and Ancestor

Given the root of a binary tree, find the maximum value V for which there 
exist different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or any child 
of A is an ancestor of B.

 

Example 1:

                   8
                 /   \
               3      10
             /  \      \
           1     6      14
               /  \     /
              4    7   13
 

Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.



Example 2:

     1
       \
         2
          \
            0
          /
        3


Input: root = [1,null,2,null,0,3]
Output: 3
 

Constraints:

1) The number of nodes in the tree is in the range [2, 5000].
2) 0 <= Node.val <= 10^5  

*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int res = 0;

    public int maxAncestorDiff(TreeNode root) {
         if (root == null) {
             return res;
         }
         
         dfs(root, root.val, root.val);
         return res;
    }

     private void dfs(TreeNode root, int min, int max){
         if (root == null) {
             return;
         }
         
         res = Math.max(res, Math.max(Math.abs(root.val - min), Math.abs(max-root.val)));
         min = Math.min(min, root.val);
         max = Math.max(max, root.val);
         dfs(root.left, min, max);
         dfs(root.right, min, max);
     }
}
