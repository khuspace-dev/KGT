#3.4 만들 수 없는 금액

import time
start_time = time.time()

N = int(input())
arr = list(map(int,input().split()))

arr.sort()

ans = 1

for i in arr:
    if ans < i:
        break
    else:
        ans += i

print(ans)

end_time = time.time()
print('time : ', end_time - start_time)