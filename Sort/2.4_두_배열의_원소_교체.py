#2.4 두 배열의 원소 교체

import time
start_time = time.time()

N, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse = True)

for i in range(K):
    temp = A[i]
    A[i] = B[i]
    B[i] = temp

print(sum(A))

end_time = time.time()
print('time : ', end_time - start_time)