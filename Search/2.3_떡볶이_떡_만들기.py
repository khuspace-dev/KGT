#2.3 떡볶이 떡 만들기

import time
start_time = time.time()

N, M = map(int, input().split())
arr = list(map(int,input().split()))

left = 0
right = max(arr)

ans = 0
while(left <= right):
    total = 0
    mid = (left + right) // 2

    for i in arr:
        if mid < i:
            total += i - mid
    if total < M:
        right = mid - 1
    else:
        ans = mid
        left = mid + 1

print(ans)

end_time = time.time()
print('time : ', end_time - start_time)