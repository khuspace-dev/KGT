#2.4 바닥 공사

import time
start_time = time.time()

N = int(input())
dp = [0] * 1001

dp[0] = 1
for i in range(998):
    dp[i+2] += dp[i] * 2
    dp[i+1] += dp[i]

dp[1000] += dp[999]

print(dp[N]%796796)

end_time = time.time()
print('time : ', end_time - start_time)