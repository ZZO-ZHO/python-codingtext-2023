# 백준 11404 - 플로이드 워셜

import sys
input = sys.stdin.readline

N = int(input())    # 도시 5
M = int(input())    # 노선 개수 14

distance = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]  # 6*6 인접행렬

for i in range(1, N+1):
    distance[i][i] = 0  # 인접행렬 초기화

for i in range(M):
    s, e, v = map(int, input().split())
    if distance[s][e] > v:  # 중복된 노선중 더 저렴한 버스가 있으면
        distance[s][e] = v

# 플로이드 워셜 시작
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            # 경유지를 경우해서 오는 노선의 비용이 더 저렴할경우
            if distance[i][j] > distance[i][k] + distance[k][e]:
                distance[i][j] = distance[i][k] + distance[k][e]

for i in range(1, N+1):
    for i in range(1, N+1):
        if distance[i][j] == sys.maxsize:
            print(0, end=' ')
        else:
            print(distance[i][j],end=' ')
    print()