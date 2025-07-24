#3.16 연구소

import time
import copy
from itertools import combinations
start_time = time.time()

N, M = map(int, input().split())
Lab_t = []
for i in range(N):
    line = list(map(int,input().split()))
    Lab_t.append(line)

BFS_t = []

comb = []
for i in range(N):
    for j in range(M):
        comb.append([i, j])
        if Lab_t[i][j] == 2:
            BFS_t.append([j, i])
com = list(combinations(comb, 3))


ans = 0
for k in range(len(com)):
    Lab = copy.deepcopy(Lab_t)
    check = 0
    for i in range(3):
        a = com[k][i][0]
        b = com[k][i][1]
        if Lab[a][b] != 0:
            check = 1
            continue
        else:
            Lab[a][b] = 1

    if check:
        continue

    BFS = BFS_t[:]
    while BFS:
        L = BFS.pop(0)
        i = L[1]
        j = L[0]
        Lab[i][j] = 2
        if 0 < i and Lab[i-1][j] == 0:
            BFS.append([j,i-1])
        if 0 < j and Lab[i][j-1] == 0:
            BFS.append([j-1,i])
        if i < N-1 and Lab[i+1][j] == 0:
            BFS.append([j,i+1])
        if j < M-1 and Lab[i][j+1] == 0:
            BFS.append([j+1,i])

    temp = 0
    for i in range(N):
        for j in range(M):
            if Lab[i][j] == 0:
                temp += 1
    ans = max(ans, temp)

print(ans)

end_time = time.time()
print('time : ', end_time - start_time)