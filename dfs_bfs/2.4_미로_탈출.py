#2.4 미로탈출

import time
start_time = time.time()

N, M = map(int, input().split())
Maze = []
for i in range(N):
    line = list(map(int,input().split()))
    Maze.append(line)

ans = 0

BFS = []
BFS.append([0, 0])
while BFS:
    L = BFS.pop(0)
    i = L[1]
    j = L[0]
    if Maze[i][j] == 0:
        continue
    if (i == N-1 and j == M-1):
        ans = Maze[i][j]
        break
    if 0 < i and Maze[i-1][j] != 0:
        BFS.append([j,i-1])
        if Maze[i-1][j] == 1:
            Maze[i-1][j] = Maze[i][j] + 1
        else:
            Maze[i-1][j] = min(Maze[i][j] + 1, Maze[i-1][j])
    if 0 < j and Maze[i][j-1] != 0:
        BFS.append([j-1,i])
        if Maze[i][j-1] == 1:
            Maze[i][j-1] = Maze[i][j] + 1
        else:
            Maze[i][j-1] = min(Maze[i][j] + 1, Maze[i][j-1])
    if i < N-1 and Maze[i+1][j] != 0:
        BFS.append([j,i+1])
        if Maze[i+1][j] == 1:
            Maze[i+1][j] = Maze[i][j] + 1
        else:
            Maze[i+1][j] = min(Maze[i][j] + 1, Maze[i+1][j])
    if j < M-1 and Maze[i][j+1] != 0:
        BFS.append([j+1,i])
        if Maze[i][j+1] == 1:
            Maze[i][j+1] = Maze[i][j] + 1
        else:
            Maze[i][j+1] = min(Maze[i][j] + 1, Maze[i][j+1])

print(ans)


end_time = time.time()
print('time : ', end_time - start_time)