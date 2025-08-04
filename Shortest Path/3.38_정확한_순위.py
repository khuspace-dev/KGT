#3.38 정확한 순위

import time
start_time = time.time()

INF = int(1e9)

N, M = map(int,input().split())

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i in range(1, N+1):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
result = 0

for i in range(1, N+1):
    count = 0
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
        if count == N:
            result += 1
print(result)

end_time = time.time()
print('time : ', end_time - start_time)