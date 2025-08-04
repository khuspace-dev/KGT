#3.43 어두운 길

import time
start_time = time.time()

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N+1)

edges = []
result = 0

for i in range(1, N+1):
    parent[i] = i

for i in range(M):
    x, y, z = map(int,input().split())
    edges.append((x, y, z))

edges.sort()
total = 0

for edge in edges:
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)

end_time = time.time()
print('time : ', end_time - start_time)