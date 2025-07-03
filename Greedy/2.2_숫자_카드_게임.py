#2.2 숫자 카드 게임

import time
start_time = time.time()


N, M = map(int,input().split())
card  = []

for i in range(N):
    line = list(map(int,input().split()))
    card.append(line)

arr = []
for i in range(N):
    arr.append(min(card[i]))

print(max(arr))

end_time = time.time()
print('time :', end_time - start_time)