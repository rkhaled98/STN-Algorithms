import math

inf = math.inf


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph += ([u, v, w]),

    def BellmanFord(self, S):

        dist = [inf] * self.V
        dist[S] = 0

        for i in range(self.V - 1):
            for u, v, w in self.graph:
                dist[v] = min([dist[v], dist[u]+w])

        for u, v, w in self.graph:
            if dist[u] + w < dist[v]:
                return False

        for i in range(self.V):
            print((i, dist[i]))


g = Graph(3)

v = {'z': 0, '1': 1, '2': 2}
g.addEdge(v['z'], v['2'], 12)
g.addEdge(v['1'], v['z'], -4)
g.addEdge(v['2'], v['1'], -3)
g.addEdge(v['1'], v['2'], 6)

g.BellmanFord(0)
