# 백준 1717 - 집합의 표현
# Union-Fri 문제

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
N, M = map(int, input().split())
parent = [0] * (N + 1)  # [0 for _ in range(N+1)]

def find(a):    # find 연산
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 재귀호출 -> 경로 압축
        return parent[a]
    
def union(a, b):    # 대표노드 합치기
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def cheakSame(a, b):
    a = find(a)
    b = find(b)
    if a == b: return True
    else: return False

for i in range(0, N+1):
    parent[i] = i 
    
for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a,b)
    else:
        if cheakSame(a,b):
            print('Yes')
        else:
            print('No')
