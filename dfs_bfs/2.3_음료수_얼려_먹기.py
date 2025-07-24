#2.3 음료수 얼려먹기

import time
start_time = time.time()

N, M = map(int, input().split())

Map = []
for i in range(N):
    line = list(map(int,input().split()))
    Map.append(line)

BFS = []
ans = 0
for q in range(N):
    for p in range(M):
        if Map[q][p] == 1:
            continue
        else:
            BFS.append([p, q])
            while BFS:
                L = BFS.pop(0)
                i = L[1]
                j = L[0]
                Map[i][j] = 1
                if 0 < i and Map[i-1][j] == 0:
                    BFS.append([j,i-1])
                if 0 < j and Map[i][j-1] == 0:
                    BFS.append([j-1,i])
                if i < N-1 and Map[i+1][j] == 0:
                    BFS.append([j,i+1])
                if j < M-1 and Map[i][j+1] == 0:
                    BFS.append([j+1,i])
            ans += 1
print(ans)

end_time = time.time()
print('time : ', end_time - start_time)