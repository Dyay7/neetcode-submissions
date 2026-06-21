class DSU:
    def __init__(self, n):
        # Each node starts as its own parent (self-parent),
        # meaning every node is initially in its own separate set.
        self.parent = list(range(n))

        # Rank stores the *size* of each set (or tree).
        # We use it to always attach the smaller tree under the bigger one.
        self.rank = [1] * n

    def find(self, node):
        # Find the root (representative) of the set that 'node' belongs to.
        # We climb parent pointers until we reach a root (parent[root] == root).
        cur = node
        while cur != self.parent[cur]:
            # Path compression:
            # Make each visited node point to its grandparent.
            # This flattens the tree and makes future finds much faster.
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, u, v):
        # Find the roots of the sets containing u and v.
        pu = self.find(u)
        pv = self.find(v)

        # If both nodes already share the same root,
        # they are already in the same set → merging would create a cycle.
        if pu == pv:
            return False

        # Union by rank (size):
        # Always attach the smaller tree under the bigger tree.
        if self.rank[pv] > self.rank[pu]:
            # Swap so that pu is always the root of the larger tree.
            pu, pv = pv, pu

        # Attach the smaller tree (pv) under the larger tree (pu).
        self.parent[pv] = pu

        # Update the size of the resulting tree.
        self.rank[pu] += self.rank[pv]

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res