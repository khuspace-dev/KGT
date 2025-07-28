#2.5 효율적인 화폐 구성

import time
start_time = time.time()

N, M = map(int,input().split())

dp = [10001] * 10001
money = []
for i in range(N):
    a = int(input())
    money.append(a)
    dp[a] = 1

for i in range(1, 10001):
    for j in range(N):
        if 0 < i - money[j] and dp[i - money[j]] != 10001:
            dp[i] = min(dp[i], dp[i - money[j]] + 1)

if(dp[M] == 10001):
    dp[M] = -1
print(dp[M])

end_time = time.time()
print('time : ', end_time - start_time)