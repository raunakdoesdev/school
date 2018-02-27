from collections import defaultdict
from heapq import *
import copy

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen = [(0,f,())], set()
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path)

def floyd_warshall(w, n):
    d = {0: w}
    for k in range(1,n+1):
        d[k] = {}
        for i in range(1,n+1):
            for j in range(1,n+1):
                d[k][i,j] = min(d[k-1][i,j],
                                d[k-1][i,k] + d[k-1][k,j])
    return d[n]


fin = open ('slingshot.in', 'r')
fout = open ('slingshot.out', 'w')

n, m = map(int, fin.readline().split())

w = {}

for i in range(1,n+1):
    w[i,i] = 0
    for j in range(1,n+1):
        w.setdefault((i,j), INF)

# Build base graph
for i in range(n):
    x, y, t = map(int, fin.readline().split())
    w[x, y] = t
# print edges
for i in range(m):
    a, b = map(int, fin.readline().split())
    for j in range(n):
        # First directional
        new_edges.append([a, edges[j][0], abs(a - edges[j][0])])
        new_edges.append([edges[j][1], b, abs(b - edges[j][1])])

        # Direct
        new_edges.append([a, b, abs(b - a)])
    fout.write(str(dijkstra(new_edges, a, b)[0]) + '\n')

fout.close()
