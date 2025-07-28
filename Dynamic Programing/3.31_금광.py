#3.31 금광

import time
start_time = time.time()

T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))
    gold = []
    for j in range(N):
        line = []
        for k in range(M * j, M * (j+1)):
            line.append(arr[k])
        gold.append(line)

    for j in range(1, M):
        for k in range(N):
            if k == 0:
                gold[k][j] = max(gold[k][j], gold[k][j] + gold[k][j-1], gold[k][j] + gold[k+1][j-1])
            elif k == N-1:
                gold[k][j] = max(gold[k][j], gold[k][j] + gold[k][j-1], gold[k][j] + gold[k-1][j-1])
            else:
                gold[k][j] = max(gold[k][j], gold[k][j] + gold[k][j-1], gold[k][j] + gold[k+1][j-1], gold[k][j] + gold[k-1][j-1])
    ans = []
    for i in range(N):
        ans.append(gold[i][M-1])
    print(max(ans))
    



end_time = time.time()
print('time : ', end_time - start_time)