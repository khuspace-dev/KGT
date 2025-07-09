#3.11 뱀

import time
start_time = time.time()

def move(x, y, heading):
    if heading == 0:
        y -= 1
    elif heading == 1:
        x += 1
    elif heading == 2:
        y += 1
    else:
        x -= 1
    ret = [x, y, heading]
    return ret

pos = [[0, 0]]
heading = 1 #0 : 위, 1 : 오, 2 : 아, 3 : 왼
N = int(input())
K = int(input())
Map = []
for i in range(N):
    line = []
    for i in range(N):
        line.append(0)
    Map.append(line)
for i in range(K):
    a, b = map(int,input().split())
    Map[a-1][b-1] = 1
L = int(input())

answer = 0
inner_check = True
for i in range(L):
    T, C = input().split()

    for i in range(answer, int(T)):
        answer += 1
        new_pos = move(pos[-1][0], pos[-1][1], heading)
        if(new_pos[0] < 0 or new_pos[1] < 0 or N <= new_pos[0] or N <= new_pos[1] or [new_pos[0], new_pos[1]] in pos):
            inner_check = False
            break
        elif(Map[new_pos[1]][new_pos[0]] == 1):
            Map[new_pos[1]][new_pos[0]] = 0
            pos.append([new_pos[0], new_pos[1]])
        else:
            pos.append([new_pos[0], new_pos[1]])
            pos.pop(0)

    if inner_check == False:
        break
    if C == 'L':
        heading += 3
        heading %= 4
    elif C == 'D':
        heading += 1
        heading %= 4

while inner_check:
    answer += 1
    new_pos = move(pos[-1][0], pos[-1][1], heading)
    if(new_pos[0] < 0 or new_pos[1] < 0 or N <= new_pos[0] or N <= new_pos[1] or [new_pos[0], new_pos[1]] in pos):
        inner_check = False
    elif(Map[new_pos[1]][new_pos[0]] == 1):
        Map[new_pos[1]][new_pos[0]] = 0
        pos.append([new_pos[0], new_pos[1]])
    else:
        pos.append([new_pos[0], new_pos[1]])
        pos.pop(0)

print(answer)

end_time = time.time()
print('time : ', end_time - start_time)