#https://hodunamu.com/python-%EC%98%88%EC%83%81-%EB%8C%80%EC%A7%84%ED%91%9C/
#https://programmers.co.kr/learn/courses/30/lessons/12985#

def solution(n,a,b):
    answer = 1
    
    if a > b :
        a, b = b, a
        
    while b - a != 1 or a % 2 == 0:
        answer += 1
        if a % 2 == 1 :
            a = (a + 1) / 2
        else :
            a = a / 2
        
        if b % 2 == 1 :
            b = (b + 1) / 2
        else :
            b = b / 2
    #answer += 1
    return answer

