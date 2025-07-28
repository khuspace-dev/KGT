#3.36 편집 거리

import time
start_time = time.time()

A = input()
B = input()

N = len(A)
M = len(B)

dp = [[0] * (M + 1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = i
for i in range(1, M+1):
    dp[0][i] = i

for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1]

        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[N][M])

end_time = time.time()
print('time : ', end_time - start_time)