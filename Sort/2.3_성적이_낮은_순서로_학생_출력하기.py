#2.3 성적이 낮은 순서로 학생 출력하기

import time
start_time = time.time()
N = int(input())

arr = []
for i in range(N):
    A, B = input().split()
    arr.append([A, int(B)])
arr.sort(key = lambda x:x[1])

for i in range(len(arr)):
    print(arr[i][0], end=' ')

end_time = time.time()
print('time : ', end_time - start_time)