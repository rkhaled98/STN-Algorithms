import math

inf = math.inf

# graph2 = [[999, 8, 9],
#           [10, 999, 12],
#           [-2, -1, 999]]
graph = [[math.inf, math.inf, 9],
         [math.inf, math.inf, 12],
         [-2, -1, math.inf]]
D = [[7, 8, 9],
     [10, 13, -1],
     [-2, -1, -7]]
labels = {0: 'Z', 1: 'X1', 2: 'X2'}
labelsF = {'Z': 0, 'X1': 1, 'X2': 2}


def relax(Xi, dij, Xj, djk, Xk, graph):
    dik = dij + djk
    if graph[Xi][Xk] == math.inf:
        graph[Xi][Xk] = dik
    else:
        if dik < graph[Xi][Xk]:
            graph[Xi][Xk] = dik


def floyd(graph):
    n = len(graph)
    for j in range(n):
        for i in range(n):
            for k in range(n):
                relax(i, graph[i][j],
                      j, graph[j][k],
                      k, graph)


print(graph)
floyd(graph)
print(graph)
