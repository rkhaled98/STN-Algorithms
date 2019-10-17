import math

inf = math.inf

# graph1 = [[0, inf, 9],
#           [inf, 0, 12],
#           [-2, -1, 0]]

# D1 = [[7, 8, 9],
#       [10, 13, -1],
#       [-2, -1, -7]]

# from http://cognitive-robotics17.csail.mit.edu/docs/tutorials/Tutorial3_Temporal_Networks_for_Dynamic_Scheduling_Revised.pdf
graph2 = [[0, inf, inf, inf, 250],
          [-4, 0, inf, inf, 168],
          [inf, 0, 0, inf,  inf],
          [inf, inf, -120, 0, 7],
          [inf, inf, inf, 0, 0]]

D2 = [[0, 130, 130, 250, 250],
      [-4, 0, 48, 168, 168],
      [-4, 0, 0, 168, 168],
      [-124, -120, -120, 0, 7],
      [-124, -120, -120, 0, 0]]

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


# floyd(graph1)
floyd(graph2)

# assert(graph1 == D1)
assert(graph2 == D2)
