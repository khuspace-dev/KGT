#2.1 왕실의 나이트

import time
start_time = time.time()

s = input()

dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

x = dict[s[0]]
y = int(s[1])

x_arr = []
y_arr = []
for i in range(8):
    x_arr.append(x)
    y_arr.append(y)

x_offset = [2, 2, -2, -2, 1, -1, 1, -1]
y_offset = [1, -1, 1, -1, 2, 2, -2, -2]

for i in range(8):
    x_arr[i] += x_offset[i]
    y_arr[i] += y_offset[i]

answer = 0

for i in range(8):
    if(x_arr[i] < 1 or 8 < x_arr[i] or y_arr[i] < 1 or 8 < y_arr[i]):
        continue
    else:
        answer += 1

print(answer)

end_time = time.time()
print('time : ', end_time - start_time)