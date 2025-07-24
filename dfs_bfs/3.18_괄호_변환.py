#3.18 괄호 변환

import time
start_time = time.time()

def balance(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
            
def check(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    
    if p == '':
        return answer
    index = balance(p)
    u = p[:index + 1]
    v = p[index + 1:]
    
    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

end_time = time.time()
print('time : ', end_time - start_time)