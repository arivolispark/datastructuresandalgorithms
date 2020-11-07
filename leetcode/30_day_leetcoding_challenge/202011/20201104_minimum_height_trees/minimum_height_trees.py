"""
Title:  Minimum Height Trees

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.


Example 2:
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]



Example 3:
Input: n = 1, edges = []
Output: [0]



Example 4:
Input: n = 2, edges = [[0,1]]
Output: [0,1]
 

Constraints:
1) 1 <= n <= 2 * 104
2) edges.length == n - 1
3) 0 <= ai, bi < n
4) ai != bi
5) All the pairs (ai, bi) are distinct.
6) The given input is guaranteed to be a tree and there will be no repeated edges.

"""

from typing import List
 

class Solution:

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: 
            return [0]
        
        leaves = collections.defaultdict(set)
        
        for u, v in edges:
            leaves[u].add(v)
            leaves[v].add(u)
        
        que = collections.deque()
        
        for u, vs in leaves.items():
            if len(vs) == 1:
                que.append(u)
        
        while n > 2:
            _len = len(que)
            n -= _len
            for _ in range(_len):
                u = que.popleft()
                for v in leaves[u]:
                    leaves[v].remove(u)
                    if len(leaves[v]) == 1:
                        que.append(v)
        return list(que)        

