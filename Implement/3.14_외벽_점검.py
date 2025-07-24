#3.14 외벽 점검

import time
from itertools import permutation

start_time = time.time()


def solution(n, weak, dist):
    answer = 0
    interval = [weak[0]]
    for i in range(len(1, len(weak))):
        temp = interval.pop()
        interval.append(weak[i]-temp)
        interval.append(weak[i])
    interval.pop()
    interval.append(n+weak[0]-weak[-1])
    dist.sort()
    
    temp_dist = []
    for i in range(len(dist)):
        temp_dist.append(dist[-1-i])
        
    
        
    
    return -1

end_time = time.time()
print('time : ', end_time - start_time)