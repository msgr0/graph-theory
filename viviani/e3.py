#!/usr/bin/env python
# author: Mattia Sgro
# es3: given an undirected graph, compute the closeness centrality for each node in the graph.
# It is possible to use Python libraries to calculate the distance of a node from other nodes.

# closeness centrality in an undirected graph:
# cc(n) = 1 / (sum ( dist(n, ni in Ni) ) where Ni = N / n
# the graph is undirected and undweighted, dist between n and m nodes
# is given 
# if the graph is weighted, FW
#

### FLOYD-WARSHALL FUNCTIONS from e2
def mymin(a,b):
    if a is None and b is not None:
        return b
    if b is None and a is not None:
        return a
    else:
        return min(a,b)

def fw(mat, n):
    matk = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n+1)]
    matk[-1] = mat
    # print("mat0 is", matk[-1])
    for k in range(len(mat)):
        for (x, y) in zip(range(len(mat)), range(len(mat[0]))):
                matk[k][x][y] = mat[x][y]
                matk[k][k][y] = mat[k][y]
                matk[k][x][k] = mat[x][k]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                matk[k][i][j] = mymin(matk[k-1][i][j], matk[k-1][i][k] + matk[k-1][k][j])

    return matk[n-1]


#### END FLOYD-WARSHALL FUNCTIONS


def ncc(mat, mind, n):
    return cc(mat,mind,n) * float(len(mat) -1 ) 
#### nccc
def cc(mat, mind, n):
    summ = 0
    for x in range(len(mat)):
        summ += mind[n][x]

    return float(1) / float(summ)

###
def main():
    # matrix in the example at slides page 21
    mat = [
        [0, 1, 1, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
        [float('inf'), 0, 1, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
        [1, 1, 0, 1, float('inf'), float('inf'), float('inf'), float('inf'), float('inf')],
        [1, float('inf'), 1, 0, 1, 1, float('inf'), float('inf'), float('inf')],
        [float('inf'), float('inf'), float('inf'), 1, 0, 1, 1, 1, float('inf')],
        [float('inf'), float('inf'), float('inf'), 1, 1, 0, 1, 1, float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), 1, 1, 0, 1, 1],
        [float('inf'), float('inf'), float('inf'), float('inf'), 1, 1, 1, 0, float('inf')],
        [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 1, float('inf'), 0]
    ]
    mind = fw(mat, len(mat))
    print("Matrix of min distances\n", mind)
    print("printing for every node in the graph, cc = closeness centrality and ncc = normalized closeness centrality")
    for node in range(len(mat)):
        print("cc(", node+1, ")=", round(cc(mat, mind, node), 2), " \tncc(", node+1, ")=", round(ncc(mat, mind, node), 2))


if __name__ == "__main__":
    main()
