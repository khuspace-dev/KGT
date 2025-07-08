#2.2 게임 개발

import time
start_time = time.time()

def progress_2(x, y, h, m):
    ret = True
    if h == 0:
        y -= 1
        if (y < 0 or m[y][x] != 0):
            ret = False
    elif h == 1:
        x += 1
        if (len(m[0]) <= x or m[y][x] != 0):
            ret = False
    elif h == 2:
        y += 1
        if (len(m) <= y or m[y][x] != 0):
            ret = False
    elif h == 3:
        x -= 1
        if (x < 0 or m[y][x] != 0):
            ret = False
        
    return ret

row, col = map(int,input().split())
x, y, heading = map(int,input().split())
Map = []
for i in range(row):
    line = list(map(int,input().split()))
    Map.append(line)

ans = 1
count = 0
while True:
    heading += 1
    heading %= 4
    if(progress_2(x, y, heading, Map)):
        if heading == 0:
            y -= 1
        elif heading == 1:
            x += 1
        elif heading == 2:
            y += 1
        elif heading == 3:
            x -= 1
        Map[y][x] = 2
        ans += 1
        count = 0
    else:
        count += 1
    if count == 4:
        Map[y][x] = 2
        if heading == 0:
            y += 1
        elif heading == 1:
            x -= 1
        elif heading == 2:
            y -= 1
        elif heading == 3:
            x += 1
        if(x < 0 or y < 0 or len(Map[0]) <= x or len(Map) <= y or Map[y][x] == 1):
            break
        count = 0

print(ans)
for i in range(row):
    print(Map[i])

end_time = time.time()
print('time : ', end_time - start_time)