import math

inf = math.inf

graph1 = [[inf, inf, 9],
          [inf, inf, 12],
          [-2, -1, inf]]

D1 = [[7, 8, 9],
      [10, 13, -1],
      [-2, -1, -7]]

graph2 = [[0,   5,  inf, 10],
          [inf,  0,  3,  inf],
          [inf, inf, 0,   1],
          [inf, inf, inf, 0]]

D2 = [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, inf, inf, 0]]

labels = {0: 'Z', 1: 'X1', 2: 'X2'}
labelsF = {'Z': 0, 'X1': 1, 'X2': 2}


def relax(Xi, dij, Xj, djk, Xk, graph):
    dik = dij + djk
    if graph[Xi][Xk] == math.inf:
        graph[Xi][Xk] = dik
    elif dik < graph[Xi][Xk]:
        graph[Xi][Xk] = dik


def floyd(graph):
    n = len(graph)
    for j in range(n):
        for i in range(n):
            for k in range(n):
                relax(i, graph[i][j],
                      j, graph[j][k],
                      k, graph)


floyd(graph1)
floyd(graph2)

assert(graph1 == D1)
assert(graph2 == D2)
