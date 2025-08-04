#3.39 화성 탐사

import time
import heapq
import sys
start_time = time.time()

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(int(input())):
    N = int(input())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    
    distance = [[INF] * (N) for _ in range(N)]

    x, y = 0, 0

    q = [(graph[x][y], x, y)]

    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heapop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or N <= nx or ny < 0 or N <= ny:
                continue
            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heapush(q, (cost,nx,ny))

    print(distance[N-1][N-1])

end_time = time.time()
print('time : ', end_time - start_time)