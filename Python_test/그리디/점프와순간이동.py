# https://programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0
    num = 0
    
    while n > 1:
        num = n // 2
        if n % 2 != 0:
            ans += 1
        n = num 
        
    return ans + 1