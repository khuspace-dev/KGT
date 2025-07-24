#3.24 안테나

import time
start_time = time.time()

N = int(input())
arr = list(map(int,input().split()))
arr.sort()

pos = arr[0]

ans = []
while pos <= arr[-1]:
    temp = 0
    for i in range(N):
        if pos - arr[i] < 0:
            temp -= pos - arr[i]
        else:
            temp += pos - arr[i]
    ans.append([temp, pos])
    pos += 1
ans.sort(key = lambda x : x[0])

print(ans[0][1])

end_time = time.time()
print('time : ', end_time - start_time)