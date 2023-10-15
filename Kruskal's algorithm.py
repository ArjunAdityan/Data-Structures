class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, src, dest, weight):
        self.graph.append([src, dest, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_mst(self):
        result = []

        # sort edges in ascending order of weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # initialize parent and rank arrays for each vertex
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        i = 0
        e = 0

        # iterate over all edges
        while e < self.V - 1:
            src, dest, weight = self.graph[i]
            i += 1
            x = self.find(parent, src)
            y = self.find(parent, dest)

            # if including this edge does not form a cycle, add it to the MST
            if x != y:
                e += 1
                result.append([src, dest, weight])
                self.union(parent, rank, x, y)

        return result
g = Kruskal(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print(g.kruskal_mst())  # Output: [[2, 3, 4], [0, 3, 5], [0, 1, 10]]
