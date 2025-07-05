#3.5 볼링공 고르기

import time
start_time = time.time()

N, M = map(int, input().split())
arr = list(map(int,input().split()))


ans = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if(arr[i] == arr[j]):
            continue
        ans += 1

print(ans)

end_time = time.time()
print('time : ', end_time - start_time)