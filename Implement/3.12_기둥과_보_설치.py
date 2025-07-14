#3.12 기둥과 보 설치

import time
start_time = time.time()

def install(x, y, a, f):
    ret = False
    if a:
        if f[y-1][x] == 1 or f[y-1][x] == 3:
            ret = True
        elif x <= len(f) and (f[y-1][x+1] == 1 or f[y-1][x+1] == 3):
            ret = True
        elif 0 < x and x <= len(f) and (f[y][x-1] == 2 and f[y][x+1] == 2) or (f[y][x-1] == 3 and f[y][x+1] == 3):
            ret = True
    else:
        if y == 0 or f[y-1][x] == 1 or f[y-1][x] == 3:
            ret = True
        elif f[y][x] == 2 or f[y][x] == 3:
            ret = True
        elif 0 < x and (f[y][x-1] == 2 or f[y][x-1] == 3):
            ret = True
    return ret

def remove(x, y, a, f):
    ret = True
    if a:
        if 0 < x and (f[y][x-1] == 2 or f[y][x-1] == 3):
            ret = False
        elif x <= len(f) and (f[y][x+1] == 2 or f[y][x+1] == 3):
            ret = False
    else:
        if f[y+1][x] == 1 or f[y+1][x] == 3:
            ret = False
        elif 0 < x and (f[y+1][x-1] == 2 or f[y+1][x-1] == 3):
            ret = False
            if f[y][x-1] == 1 or f[y][x-1] == 3:
                ret = True
            elif (f[y+1][x-2] == 2 and f[y+1][x] == 2) or (f[y+1][x-2] == 3 and f[y+1][x] == 3):
                ret = True
        elif f[y+1][x] == 2 or f[y+1][x] == 3:
            ret = False
            if f[y][x+1] == 1 or f[y][x+1] == 3:
                ret = True
            elif (f[y+1][x-1] == 2 and f[y+1][x+1] == 2) or (f[y+1][x-1] == 3 and f[y+1][x+1] == 3):
                ret = True
    return ret

def solution(n, build_frame):
    frame = []
    for i in range(n+2):
        line = []
        for j in range(n+2):
            line.append(0)
        frame.append(line)
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b:
            if install(x, y, a, frame):
                frame[y][x] += a + 1
        else:
            if remove(x, y, a, frame):
                frame[y][x] -= a + 1
    answer = []
    for i in range(n+1):
        line = []
        for j in range(n+1):
            if frame[j][i] == 1 or frame[j][i] == 3:
                line.append([i, j, 0])
        for j in range(n+1):
            if frame[j][i] == 2 or frame[j][i] == 3:
                if n <= i:
                    continue
                if (frame[j][i] or frame[j-1][i] == 1 or frame[j][i-1] == 2) and (frame[j][i+1] or frame[j-1][i+1] == 1 or frame[j][i+1] == 1):
                    line.append([i, j, 1])
        answer += line

    return answer

print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
print(solution(5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))
print(solution(5, [[1, 0, 0, 1], [2, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [1, 0, 0, 0]]))
print(solution(100, [[2, 0, 0, 1], [100, 0, 0, 1], [100, 1, 1, 1], [99, 1, 1, 1], [99, 1, 0, 1], [99, 0, 0, 1]]))

end_time = time.time()
print('time : ', end_time - start_time)