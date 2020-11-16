# 프로그래머스 문제 
# https://programmers.co.kr/learn/courses/30/lessons/67256
# https://life-of-panda.tistory.com/75
# https://whwl.tistory.com/71

def solution(numbers, hand):
    answer = ''
    lastL = 10
    lastR = 12
    
    for n in numbers:
        if n in [1,4,7]:
            answer+='L'
            lastL = n
        elif n in [3,6,9]:
            answer+='R'
            lastR = n
        else:
            n = 11 if n == 0 else n
            
            absL = abs(n-lastL)
            absR = abs(n-lastR)
            
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer+='R'
                lastR = n
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer +='L'
                lastL = n
            else:
                if hand == 'left':
                    answer+='L'
                    lastL = n
                else:
                    answer+='R'
                    lastR = n
                
    return answer
