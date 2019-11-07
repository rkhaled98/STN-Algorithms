import math

inf = math.inf


class Edge:
    def __init__(self, fromNode, weight, toNode, outgoing, incoming):
        self.fromNode = fromNode
        self.weight = weight
        self.toNode = toNode
        self.outgoing = outgoing
        self.incoming = incoming


class graph:
    def __init__(self, edges):
        self.incoming = [[0 for x in range(edges)] for y in range(edges)]
        self.outgoing = [[0 for x in range(edges)] for y in range(edges)]
        self.incomingHowMany = [0 for x in range(edges)]
        self.outgoingHowMany = [0 for x in range(edges)]
        self.shape = edges

    def addEdge(self, fromNode, weight, toNode):
        incomingLen = self.incomingHowMany[toNode]
        outgoingLen = self.outgoingHowMany[fromNode]

        edge = Edge(fromNode, weight, toNode, outgoingLen, incomingLen)

        self.incoming[toNode][incomingLen] = edge
        self.outgoing[fromNode][outgoingLen] = edge

        self.incomingHowMany[toNode] += 1
        self.outgoingHowMany[fromNode] += 1

    def checkNegativeCycle(self, parent):
        if parent[0] != 0:
            return True
        n = len(parent)
        visitLevel = [0]*n

        level = n
        for i in range(n-1,-1,-1):
            if visitLevel[i] > level:
                continue
            visitLevel[i] = level
            p = parent[i]
            while p != 0:
                if visitLevel[p] == level:
                    return True
                if visitLevel[p] > level:
                    break
                visitLevel[p] = level
                p = parent[p]
            level-=1
        return False

    def Yen(self, S):
        e_plus = graph(self.shape)
        e_minus = graph(self.shape)

        for i in range(self.shape):
            for j in range(self.incomingHowMany[i]):
                edge = self.incoming[i][j]
                if edge.fromNode < edge.toNode:
                    e_plus.addEdge(edge.fromNode, edge.weight, edge.toNode)
                else:
                    e_plus.addEdge(edge.fromNode, edge.weight, edge.toNode)

        C = set([S])
        P = [None] * self.shape
        d = {}

        for i in range(self.shape):
            d[i] = inf

        d[S] = 0
        flip = 1

        while C:
            Cp = set()
            e_star = e_plus if flip % 2 != 0 else e_minus
            for i in range(self.shape):
                j = i if flip % 2 != 0 else n - i - 1
                if j in C.union(Cp):
                    for outgoingIdx in range(e_star.outgoingHowMany[j]):
                        edge = e_star.outgoing[j][outgoingIdx]
                        Y = edge.toNode
                        if d[Y] > d[j] + edge.weight:
                            d[Y] = d[j] + edge.weight
                            P[Y] = j
                            Cp.add(Y)
            if self.checkNegativeCycle(P):
                return False
            C = Cp
            flip += 1
        return d


v = {'z': 0, '1': 1, '2': 2}

g = graph(3)

g.addEdge(v['z'], 12, v['2'])
g.addEdge(v['1'], -4, v['z'])
g.addEdge(v['2'], -3, v['1'])
g.addEdge(v['1'], 6, v['2'])

print(g.Yen(0))
