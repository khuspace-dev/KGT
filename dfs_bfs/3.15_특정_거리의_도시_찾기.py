#3.15 특정 거리의 도시 찾기

import time
start_time = time.time()

N, M, K, X = map(int, input().split())
road = [[]]
length = [0]

for i in range(N):
    road.append([])
    length.append(0)
for i in range(M):
    A, B = map(int,input().split())
    road[A].append(B)

BFS = [X]
while BFS:
    city = BFS.pop(0)
    for i in range(len(road[city])):
        A = road[city][i]
        if length[A] == 0:
            length[A] = length[city] + 1
            BFS.append(A)
        elif length[city] + 1 < length[A]:
            length[A] = length[city] + 1
            BFS.append(A)

check = 1
for i in range(len(length)):
    if length[i] == K:
        print(i)
        check = 0
if check:
    print(-1)


end_time = time.time()
print('time : ', end_time - start_time)