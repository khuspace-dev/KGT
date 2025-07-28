#3.32 정수 삼각형

import time
start_time = time.time()

N = int(input())

dp = list(map(int,input().split()))
for i in range(N-1):
    temp = []
    line = list(map(int,input().split()))
    temp.append(dp[0] + line[0])
    for j in range(1, len(line)-1):
        temp.append(max(line[j] + dp[j], line[j] + dp[j-1]))
    temp.append(line[-1] + dp[-1])
    dp = temp[:]

print(max(dp))

end_time = time.time()
print('time : ', end_time - start_time)