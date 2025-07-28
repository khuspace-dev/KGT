#3.34 병사 배치하기

import time
start_time = time.time()

def BS(arr, target):
    left = 0
    right = len(arr)-1
    while (left < right):
        mid = (left + right) // 2
        if target < arr[mid]:
            left = mid + 1
        else:
            right = mid
    return right

N = int(input())
arr = list(map(int,input().split()))

lis = [arr[0]]
for i in range(1, len(arr)):
    if arr[i] < lis[-1]:
        lis.append(arr[i])
    else:
        pos = BS(lis, arr[i])
        lis[pos] = arr[i]

print(N - len(lis))

end_time = time.time()
print('time : ', end_time - start_time)