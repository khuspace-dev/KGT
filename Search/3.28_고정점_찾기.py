#3.28 고정점 찾기

import time
start_time = time.time()

N = int(input())
arr = list(map(int, input().split()))

left = 0
right = N - 1

while left <= right:
    mid = (left + right) // 2
    if mid == arr[mid]:
        break
    
    elif mid < arr[mid]:
        right = mid - 1
    else:
        left = mid + 1

if mid == arr[mid]:
    print(mid)

else:
    print(-1)

end_time = time.time()
print('time : ', end_time - start_time)