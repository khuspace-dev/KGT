#3.1 모험가 길드

import time
start_time = time.time()

N = int(input())
arr = list(map(int,input().split()))

arr.sort()

answer = 0
while(len(arr)):
    member = arr.pop()
    if(len(arr)+1 < member):
        break
    for i in range(member-1):
        arr.pop()

    answer += 1

print(answer)

end_time = time.time()
print('time : ', end_time - start_time)
    