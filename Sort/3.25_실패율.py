#3.25 실패율

import time
start_time = time.time()

def solution(N, stages):
    answer = []
    stages.sort()
    arr = []
    for i in range(N+2):
        arr.append(0)
    for i in stages:
        for j in range(1, i+1):
            arr[j] += 1
    ratio = []
    for i in range(1, N+1):
        if arr[i] == 0:
            ratio.append([i,0])
        else:
            ratio.append([i, (arr[i]-arr[i+1])/arr[i]])
    ratio.sort(key=lambda x : (-x[1], x[0]))
    for i in range(len(ratio)):
        answer.append(ratio[i][0])
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))

end_time = time.time()
print('time : ', end_time - start_time)