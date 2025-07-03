#2.3 1이 될 때까지

import time
start_time = time.time()

N, K = map(int, input().split())

count = 0

while(1 < N):
    count += 1
    if(N%K == 0):
        N //= K
    else:
        N -= 1

print(count)

end_time = time.time()
print('time : ', end_time - start_time)