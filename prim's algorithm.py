INF = 9999999
N = 6
G = [[0,3,0,1,0,0],
     [3,0,2,0,5,0],
     [0,2,0,0,0,4],
     [1,0,0,0,6,0],
     [0,5,0,6,0,7],
     [0,0,4,0,7,0]]
vertices=['A','B','C','D','E','F']
mst=[]
selected_node = [0]*N
no_edge = 0
selected_node[0] = True
while (no_edge <N - 1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    mst.append((vertices[a], vertices[b], G[a][b]))
    selected_node[b] = True
    no_edge += 1
print(mst)