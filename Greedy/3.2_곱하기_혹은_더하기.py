#3.2 곱하기 혹은 더하기

import time
start_time = time.time()

s = input()

ans = 1
check = False

for i in s:
    j = int(i)
    if(j == 0):
        continue
    else:
        ans *= j
        check = True

if (check):
    print(ans)
else:
    print(0)

end_time = time.time()
print('time : ', end_time - start_time)
