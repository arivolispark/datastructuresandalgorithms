class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.set_size = [1] * size
        self.count = size

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1, root2 = self.find(node1 - 1), self.find(node2 - 1)
        if root1 == root2:
            return False
        if self.set_size[root1] > self.set_size[root2]:
            self.parent[root2] = root1
            self.set_size[root1] += self.set_size[root2]
        else:
            self.parent[root1] = root2
            self.set_size[root2] += self.set_size[root1]
        self.count -= 1
        return True


class Solution:
    def maxNumEdgesToRemove(self, num_nodes: int, edges: List[List[int]]) -> int:
        alice_union_find = UnionFind(num_nodes)
        bob_union_find = UnionFind(num_nodes)
        num_edges_removed = 0

        for edge_type, node1, node2 in edges:
            if edge_type == 3:
                if not alice_union_find.union(node1, node2):
                    num_edges_removed += 1
                else:
                    bob_union_find.union(node1, node2)

        for edge_type, node1, node2 in edges:
            if edge_type == 1:
                if not alice_union_find.union(node1, node2):
                    num_edges_removed += 1
            elif edge_type == 2:
                if not bob_union_find.union(node1, node2):
                    num_edges_removed += 1

        if alice_union_find.count == 1 and bob_union_find.count == 1:
            return num_edges_removed
        else:
            return -1
