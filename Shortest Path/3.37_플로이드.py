#3.37 플로이드

import time
start_time = time.time()

INF = int(1e9)

N = int(input())
M = int(input())

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i in range(M):
    a, b, c = map(int,input().split())
    if c < graph[a][b]:
        graph[a][b] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

end_time = time.time()
print('time : ', end_time - start_time)