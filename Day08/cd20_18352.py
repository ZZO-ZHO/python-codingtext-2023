# 백준 18352 - 특정거리도시찾기

import sys
from collections import deque
inpur = sys.stdin.readline

N,M,K,X = map(int,input().split())
A = [[]for _ in range(N+1)]
answer = []
visited = [-1] * (N+1)

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] += 1
    while q:
        now = q.popleft()
        for i in A[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)

# 두번쨰줄부터 엣지 입력
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)

BFS(X)

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)