#3.19 연산자 끼워 넣기

import time
from itertools import permutations
start_time = time.time()

N = int(input())
Num = list(map(int,input().split()))
Op = list(map(int,input().split()))
Oper = []
for j in range(Op[0]):
    Oper.append('+')
for j in range(Op[1]):
    Oper.append('-')
for j in range(Op[2]):
    Oper.append('*')
for j in range(Op[3]):
    Oper.append('/')

Operator = list(permutations(Oper, len(Oper)))

ans = []

for i in range(len(Operator)):
    temp = Num[0]
    for j in range(len(Operator[i])):
        if Operator[i][j] == '+':
            temp += Num[j+1]
        elif Operator[i][j] == '-':
            temp -= Num[j+1]
        elif Operator[i][j] == '*':
            temp *= Num[j+1]
        elif Operator[i][j] == '/':
            temp //= Num[j+1]
    ans.append(temp)

print(max(ans))
print(min(ans))

end_time = time.time()
print('time : ', end_time - start_time)