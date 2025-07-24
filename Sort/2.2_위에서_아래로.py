#2.2 위에서 아래로

import time
start_time = time.time()

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
arr.sort()
rev_arr = arr[::-1]
print(" ".join(map(str, rev_arr)))

end_time = time.time()
print('time : ', end_time - start_time)