#3.33 퇴사

import time
start_time = time.time()

N = int(input())
comunication = []

dp = [0] * (N+2)
for i in range(N):
    A, B = map(int,input().split())
    comunication.append([A, B])


for i in range(N):
    day = comunication[i][0]
    price = comunication[i][1]
    dp[i+1] = max(dp[i+1], dp[i])
    if day + i + 1 <= N+1:
        dp[day + i + 1] = max(dp[i+1] + price, dp[day + i + 1])

print(max(dp[1:N+2]))
end_time = time.time()
print('time : ', end_time - start_time)