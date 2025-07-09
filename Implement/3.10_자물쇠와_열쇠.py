#3.10 자물쇠와 열쇠

import time
import copy
start_time = time.time()

def rotation(arr):
    ret = []
    for i in range(len(arr)):
        line = []
        for j in range(len(arr)-1 , -1, -1):
            line.append(arr[j][i])
        ret.append(line)
    return ret

def check(arr):
    ret = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i][j] != 1):
                ret = False
                break
    return ret

def solution(key, lock):
    answer = False
    key1 = key
    key2 = rotation(key)
    key3 = rotation(key2)
    key4 = rotation(key3)
    N = len(lock)
    M = len(key)

    x = -M + 1
    y = -M + 1
    for q in range(N + M - 1):
        for p in range(N + M - 1):
            temp_lock_1 = copy.deepcopy(lock)
            temp_lock_2 = copy.deepcopy(lock)
            temp_lock_3 = copy.deepcopy(lock)
            temp_lock_4 = copy.deepcopy(lock)

            for i in range(M):
                for j in range(M):
                    X = j + x
                    Y = i + y
                    if(X < 0 or Y < 0 or N <= X or N <= Y):
                        continue
                    else:
                        temp_lock_1[Y][X] += key1[i][j]
                        temp_lock_2[Y][X] += key2[i][j]
                        temp_lock_3[Y][X] += key3[i][j]
                        temp_lock_4[Y][X] += key4[i][j]

            if(check(temp_lock_1)):
                answer = True
                break
            if(check(temp_lock_2)):
                answer = True
                break
            if(check(temp_lock_3)):
                answer = True
                break
            if(check(temp_lock_4)):
                answer = True
                break

            x += 1
        y += 1
        x = -M + 1
    
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

end_time = time.time()
print('time : ', end_time - start_time)