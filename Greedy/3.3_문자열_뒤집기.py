#3.3 문자열 뒤집기

import time
start_time = time.time()

s = input()


ans0 = 0
ans1 = 0
check0 = True
check1 = True
for i in s:
    if (i == '0'):
        check1 = True
        if check0:
            ans0 += 1
            check0 = False
    else:
        check0 = True
        if check1:
            ans1 += 1
            check1 = False

print(min(ans0, ans1))

end_time = time.time()
print('time : ', end_time - start_time)