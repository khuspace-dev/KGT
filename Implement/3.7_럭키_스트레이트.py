#3.7 럭키 스트레이트

import time
start_time = time.time()

s = input()

length = len(s)

left = s[0:length//2]
right = s[length//2:length+1]

sum_left = 0
sum_right = 0

for i in range(length//2):
    sum_left += int(left[i])
    sum_right += int(right[i])

if(sum_left == sum_right):
    print("LUCKY")
else:
    print("READY")

end_time = time.time()
print('time : ', end_time - start_time)