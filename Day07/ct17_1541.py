# 백준 1541 - 잃어버린 괄호

answer = 0
A = list(map(str, input().split('-')))  # - 기준으로 잘라서 문자열 리스트

def mySum(i):   # 마이너스로 나눈 각 문자열
    result = 0
    temp = str(i).split('+')    # + 기준으로 수식 자름
    
    for k in temp:
        result += int(k)

    return result

for s in range(len(A)):
    temp = mySum(A[s])

    if s == 0:
        answer += temp
    else:
        answer -= temp
        
print(answer)
        

