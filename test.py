def solution(cards1, cards2, goal):
    answer = ''
    i = 0
    j = 0
    
    for x in range(0, len(goal)):
        if x+1 == len(goal):
            answer = 'Yes'
            
        else:
            if goal[x] == cards1[i]:
                if i + 1 == len(cards1):
                    pass
                else: i += 1
                

            elif goal[x] == cards2[j]:
                if j + 1 == len(cards2):
                    pass
                else: j += 1 

            else:
                answer = 'No'
                break
            
    return answer
