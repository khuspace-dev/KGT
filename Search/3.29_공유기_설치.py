#3.29 공유기 설치

import time
start_time = time.time()

N, C = map(int, input().split())

arr = []

for i in range(N):
    A = int(input())
    arr.append(A)

arr.sort()

left = 1
right = arr[-1] - arr[0]

ans = 0

while left <= right:
    mid = (left + right) // 2
    pos = arr[0]
    count = 1
    
    for i in range(1, N):
        if pos + mid <= arr[i]:
            pos = arr[i]
            count += 1

    if C <= count:
        left = mid + 1
        ans = mid
    else:
        right = mid - 1
print(ans)

end_time = time.time()
print('time : ', end_time - start_time)