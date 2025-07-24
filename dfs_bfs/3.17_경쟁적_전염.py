#3.17 경쟁적 전염

import time
start_time = time.time()

N, K = map(int, input().split())
virus = []
for i in range(N):
    line = list(map(int,input().split()))
    virus.append(line)

BFS = []
for i in range(N):
    for j in range(N):
        if virus[i][j] != 0:
            BFS.append([j, i])
    
T = 1
BFS.append(T)
t, x, y = map(int,input().split())

while BFS:
    L = BFS.pop(0)
    if type(L) == int:
        if t == L:
            break
        else:
            T += 1
            BFS.append(T)
            continue
    i = L[1]
    j = L[0]
    if 0 < i and virus[i-1][j] == 0:
        BFS.append([j,i-1])
        virus[i-1][j] = virus[i][j]
    if 0 < j and virus[i][j-1] == 0:
        BFS.append([j-1,i])
        virus[i][j-1] = virus[i][j]
    if i < N-1 and virus[i+1][j] == 0:
        BFS.append([j,i+1])
        virus[i+1][j] = virus[i][j]
    if j < N-1 and virus[i][j+1] == 0:
        BFS.append([j+1,i])
        virus[i][j+1] = virus[i][j]

print(virus[x-1][y-1])

end_time = time.time()
print('time : ', end_time - start_time)