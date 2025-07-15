#3.13 치킨 배달

import time
start_time = time.time()

N, M = map(int,input().split())
Map = []
for i in range(N):
    line = list(map(int,input().split()))
    Map.append(line)

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == 1:
            house.append([j, i])
        elif Map[i][j] == 2:
            chicken.append([j, i])

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield[arr[i]]
        else:
            for next in combination(arr[i+1:], r-1):
                yield [arr[i]] + next

chicken_choose = list(combination(chicken, M))

def distance(arr1, arr2):
    a = arr1[0] - arr2[0]
    b = arr1[1] - arr2[1]
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    ret = a + b
    return ret

ans = 100000000
for i in range(len(chicken_choose)):
    Sum = 0
    for j in range(len(house)):
        dist = 100000000
        for k in range(len(chicken_choose[i])):
            dist = min(dist, distance(chicken_choose[i][k], house[j]))
        Sum += dist
    ans = min(ans, Sum)

print(ans)

end_time = time.time()
print('time : ', end_time - start_time)