# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    day = []
    
    for i in range(len(progresses)):
        
        tmp_day = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] > 0:
            tmp_day += 1
            
        day.append(tmp_day)
    
    for i in range(len(day)):
        if i == 0:
            max = day[i]
            answer.append(1)
            continue
        
        if day[i] <= max:
            answer[-1] += 1
        
        if day[i] > max:
            max = day[i]
            answer.append(1)
    
    return answer


def solution2(progresses, speeds):
    answer = []
    day = []
    
    for p,s in zip(progresses, speeds):
        tmp = (100-p)//s
        if (100-p)%s > 0: tmp += 1
        day.append(tmp)
        
    for i,d in enumerate(day):
        if i==0:
            max = d
            answer.append(1)
            continue
        
        if d <= max:
            answer[-1] += 1
            
        if d > max:
            max = d
            answer.append(1) 
            
    return answer