#3.6 무지의 먹방 라이브

import time
start_time = time.time()


def min_food_ditect(arr):
    for j in range(len(arr)):
        if (arr[j] != 0):
            ret = arr[j]
            break
    if (j == len(arr) - 1):
        return 1
    for i in range(j, len(arr)):
        if(arr[i] == 0):
            continue
        if(arr[i] < ret):
            ret = arr[i]
    return ret

def len_food(arr):
    ret = len(arr)
    for i in range(len(arr)):
        if(arr[i] == 0):
            ret -= 1
    return ret

def solution(food_times, k):
    last_eat = 0
    while(0 < k):
        food_length = len_food(food_times)

        if(food_length == 0):
            break
        if (k <= food_length):
            for i in range(len(food_times)):
                if (food_times[i] == 0):
                    continue
                food_times[i] -= 1
                k -= 1
                if(k == 0):
                    break
            last_eat = (i + 1)%len(food_times)
            break
                    
        min_food = min_food_ditect(food_times)

        if (min_food * food_length <= k):
            for i in range(len(food_times)):
                if(food_times[i] == 0):
                    continue
                else:
                    food_times[i] -= min_food
            k -= min_food * food_length
            continue
        else:
            k %= food_length
    
    if(len_food(food_times) == 0):
        answer = -1
    
    for i in range(last_eat, len(food_times)):
        if(food_times[i] != 0):
            answer = i + 1
            break

    return answer

#print(solution([3, 1, 2], 5))
##print(solution([1, 1, 1, 1, 1, 1], 1))
#print(solution([4, 1, 1, 5], 4))
#print(solution([4, 3, 5, 6, 2], 7))
#print(solution([3, 1, 1, 1, 2, 4, 3], 12))
#print(solution([1, 1, 1, 1], 4))
#print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))
#print(solution([4, 2, 3, 6, 7, 1, 5, 8], 27))
#print(solution([3, 3, 3], 8))
#print(solution([1], 3))
#print(solution([1, 10, 10], 6))
#print(solution([1, 1, 1], 3))
#print(solution([3, 1, 2], 3))
#print(solution([3, 1, 1, 1, 2, 4, 3], 12))
#print(solution([4, 2, 3, 6, 7, 1, 5, 8], 27))
#print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))
#print(solution([1, 2, 3, 4, 5, 6, 7, 8], 35))

end_time = time.time()
print('time : ', end_time - start_time)