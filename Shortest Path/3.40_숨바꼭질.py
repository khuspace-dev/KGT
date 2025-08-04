#3.40 숨바꼭질

import time
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
start_time = time.time()

N, M = map(int, input().split())
start = 1

graph = [[] for _ in range(N+1)]

distance = [INF] * (N+1)

for i in range(M):
    a, b = map(int,input().split())

    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q = []

    heapq.heapush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[i]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

max_node = 0
max_distance = 0
result = []

for i in range(1, N+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)
print(max_node, max_distance, len(result))

end_time = time.time()
print('time : ', end_time - start_time)