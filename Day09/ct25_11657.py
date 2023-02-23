# 백준 11657 - 타임머신

import sys
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize] * (N + 1)

for _ in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만포드 수행
distance[1] = 0

for _ in range(N-1):
    for start, end, time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
           distance[end] = distance[start] + time

# 음수사이클 확인
mCycle = False
for start, end, time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
       mCycle = True    # 음수사이클 존재

if mCycle != True:
    for i in range(2,N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)

    