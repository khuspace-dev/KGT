#3.27 정렬된 배열에서 특정 수의 개수 구하기

import time
start_time = time.time()

def BS(arr, target):
    left = 0
    right = len(arr) - 1
    while left<=right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

N, x = map(int,input().split())
arr = list(map(int,input().split()))

ans = 0
while True:
    A = BS(arr,x)
    if A == -1:
        break
    else:
        arr.pop(A)
        ans += 1

if ans != 0:
    print(ans)
else:
    print(-1)


end_time = time.time()
print('time : ', end_time - start_time)