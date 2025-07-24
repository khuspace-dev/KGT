#3.26 카드 정렬하기

import time
start_time = time.time()

N = int(input())
arr = []

for i in range(N):
    arr.append(int(input()))
arr.sort()
ans = 0
while 1 < len(arr):
    A = arr.pop(0)
    B = arr.pop(0)
    ans += A + B
    arr.append(A+B)
    arr.sort()

print(ans)

end_time = time.time()
print('time : ', end_time - start_time)