#2.1 큰 수의 법칙

import time
start_time = time.time()


N, M, K = map(int,input().split())

arr = list(map(int,input().split()))

arr.sort()

ans = 0

count = 0
for i in range(M):
    if (count < K):
        ans += arr[-1]
        count += 1
    else:
        ans += arr[-2]
        count = 0

print(ans)

end_time = time.time()
print('time :', end_time - start_time)