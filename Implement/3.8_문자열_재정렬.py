#3.8 문자열 재정렬

import time
start_time = time.time()

s = input()
word = ""
Sum = 0

for i in s:
    try:
        i = int(i)
        Sum += i
    except:
        word += i

word = "".join(sorted(word))
print(word + str(Sum))

end_time = time.time()
print('time : ', end_time - start_time)