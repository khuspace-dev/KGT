#3.9 문자열 압축

import time
start_time = time.time()

def solution(s):
    answer = 1001
    s = list(s)
    check = []
    count = 0
    ans = ""
    for i in range(1, len(s)//2+1):
        j = 0
        while j < len(s):
            if (len(check) == 0):
                for k in range(i):
                    try:
                        check.append(s[j+k])
                    except:
                        ans += "".join(s[j:])
                        break
            if(len(s) < j+i+i):
                if(count!=0):
                    ans += str(count+1)
                ans += "".join(check)
                ans += "".join(s[j+i:])
                break
            if (check == s[j+i:j+i+i]):
                count += 1
                j += i
                continue
            else:
                if (count == 0):
                    ans += s[j]
                    check = []
                    j += 1
                    continue
                else:
                    ans += str(count+1)
                    ans += "".join(check)
                    count = 0
                    check = []
                    j += i
                    continue
            j += 1
        answer = min(answer, len(ans))
        ans = ""
        check = []
        count = 0
    if(len(s) == 1):
        answer = 1
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("a"))

end_time = time.time()
print('time : ', end_time - start_time)