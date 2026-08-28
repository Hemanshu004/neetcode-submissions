class DSU:
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA == rootB:
            return False

        if self.rank[rootA] < self.rank[rootB]:
            rootA, rootB = rootB, rootA

        self.parents[rootB] = rootA

        if self.rank[rootA] == self.rank[rootB]:
            self.rank[rootA] += 1

        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n, edges):

        new_edges = []

        for i, (u, v, w) in enumerate(edges):
            new_edges.append([u, v, w, i])

        new_edges.sort(key=lambda x: x[2])

        def kruskal(skip=-1, force=-1):

            dsu = DSU(n)
            total = 0
            edges_used = 0

            # Force an edge
            if force != -1:
                u, v, w, idx = new_edges[force]

                if dsu.union(u, v):
                    total += w
                    edges_used += 1

            # Normal Kruskal
            for i, (u, v, w, idx) in enumerate(new_edges):

                if i == skip:
                    continue

                if i == force:
                    continue

                if dsu.union(u, v):
                    total += w
                    edges_used += 1

                    if edges_used == n - 1:
                        break

            if edges_used != n - 1:
                return float("inf")

            return total

        original = kruskal()

        critical = []
        pseudo = []

        for i, edge in enumerate(new_edges):

            # Remove edge
            without_edge = kruskal(skip=i)

            if without_edge > original:
                critical.append(edge[3])

            else:
                # Force edge
                with_edge = kruskal(force=i)

                if with_edge == original:
                    pseudo.append(edge[3])

        return [critical, pseudo]