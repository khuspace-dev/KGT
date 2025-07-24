#3.23 국영수

import time
start_time = time.time()

N = int(input())
arr = []
for i in range(N):
    arr.append(input().split())

arr.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in range(len(arr)):
    print(arr[i][0])

end_time = time.time()
print('time : ', end_time - start_time)