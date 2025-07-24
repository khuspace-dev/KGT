#2.2 부품 탐색

import time
start_time = time.time()

def BS(arr, target):
    left = 0
    right = len(arr) - 1
    while left<=right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
M = int(input())
x = list(map(int,input().split()))

for i in range(len(x)):
    if(BS(arr, x[i])):
        print('yes', end=' ')
    else:
        print('no', end=' ')


end_time = time.time()
print('time : ', end_time - start_time)