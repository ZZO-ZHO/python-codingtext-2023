# 백준 1920 - DFS와 BFS

N = int(input())    # 5
A = list(map(int, input().split()))
A.sort()    # 파이썬에서 제공하는 기본 정렬

M = int(input())
targetList = list(map(int, input().split()))

for i in range(M):
    find = False
    target = targetList[i]

    start = 0
    end = N - 1
    while start <= end:
        midle = (start + end) // 2  # 중앙 인덱스
        midVal = A[midle]   # 중앙에 있는 값
        if midVal > target: # 오른쪽 날림
            end = midle - 1
        elif midVal < target:   # 왼쪽 날림
            start = midle + 1
        else:   # 값 찾음
            find = True
            break

    if find:
        print(1)
    else:
        print(0)