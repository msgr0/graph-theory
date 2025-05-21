# /usr/bin/env python
# author: Mattia Sgro
# lecture 1
# implementation of Dijkstra and Floyd-Warshall algorithms for graph-theory course
import heapq

### FLOYD-WARSHALL FUNCTIONS
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

    print("Last matrix at n:", n, " is ", matk[n-1])
    return matk


#### END FLOYD-WARSHALL FUNCTIONS


### DIJKSTRA FUNCTIONS
def min_dist(d: dict(), q: set()): # NAIVE min_dist, quadratic
    min = float("inf")
    min_n = None
    for x in d.keys():
        # print("x is ", x)
        if x in q:
            if d[x] < min:
                min = d[x]
                min_n = x
    return min_n

    
def remove(g, u):
    g.pop(u)
    for x in g.copy().keys():
        for y in g[x].copy().keys():
            g[x].pop(y)


def length(a, b, g):
    # by definition a and b are neighbours, hence (ab) length is either in g[a] or g[b]
    for x in g[a].keys():
        if x == b:
            return g[a].get(b)
    for x in g[b].keys():
        if x == a:
            return g[b].get(a)
    print("check error here, a:", a, " and b:", b, " are not connected")
    assert False  # should never reach this point


def neig(g, q, u):
    ret = set()
    for x in g[u].keys():
        if x in q:
            ret.add(x)
    for x in g.keys():
        if x in q:
            for y in g[x].keys():
                if y is u:
                    ret.add(x)
    # print("ret:", ret, " are neig of u:", u)
    return ret

PRIO = True
NAIVE = False

def djk(g: dict(), s):
    q = set()  # set of verices
    qp = [(0, s)]
    for n in g:
        q.add(n)
    # here I used dictionaries to be able to access nodes by label instead of indexes
    d = {n: float("inf") for n in g}  # dictionary of distances
    d[s] = float(0)
    p = {n: None for n in g}  # dictionary of predecessors

    if (NAIVE):
        while q != set(): # naive
            u = min_dist(d, q)
            # print("popped u:", u, " from q set")
            q.remove(u)

            for v in neig(g, q, u):
                alt = d[u] + length(u, v, g)
                if alt < d[v]:
                    d[v] = alt
                    p[v] = u
        return d, p
    elif (PRIO):
        while qp: # with priority queue
            udist, u = heapq.heappop(qp)
            if udist > d[u]:
                continue
            for v in neig(g, q, u):
                alt = udist + length(u, v, g)
                if alt < d[v]:
                    d[v] = alt
                    p[v] = u
                    heapq.heappush(qp, (alt, v))
        return d, p

#### END DIJKSTRA FUNCTIONS


def main():
    # graph = {"A": {"B": 2, "C": 5}, "B": {"C": 1, "D": 7}, "C": {"D": 3}, "D": {}}
    graph_ex = {
        "A": {"B": 6, "D": 1},
        "B": {"C": 5, "D": 2, "E": 2},
        "C": {"E": 5},
        "D": {"E": 1},
        "E": {},
    }
    print("Runnin dijkstra on graph:", graph_ex)
    d, p = djk(graph_ex, "A")
    print("prev", p)
    print("distances", d)

    graph_ex2 = [
        [0.0, 3.0, float("inf"), 7.0],
        [8.0, 0.0, 2.0, float("inf")],
        [5.0, float("inf"), 0.0, 1.0],
        [2.0, float("inf"), float("inf"), 0.0],
    ]
    
    print("\n ---------------")
    print("Runnin Floyd-Warshall on graph:", graph_ex2)
    res = fw(graph_ex2, len(graph_ex2))
    print("\n ---------------")
    
    graph_ex3 = [
        [0, 4, float('inf'), 5, float('inf')],
        [float('inf'), 0, 1, float('inf'), 6],
        [2, float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 1, 0, 2],
        [1, float('inf'), float('inf'), 4, 0]
    ]

    print("Runnin Floyd-Warshall on graph:", graph_ex3)
    res = fw(graph_ex3, len(graph_ex3))
    print("\n ---------------")
    return


if __name__ == "__main__":
    main()
