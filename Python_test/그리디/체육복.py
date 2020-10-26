#프로그래머스
#https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
#https://wooaoe.tistory.com/78

def solution(n, lost, reserve):
    reserve_data = set(reserve)-set(lost)
    lost_data = set(lost)-set(reserve)
    
    for i in reserve_data:
        if i-1 in lost_data:
            lost_data.remove(i-1)
        elif i+1 in lost_data:
            lost_data.remove(i+1)
            
    return n - len(lost_data)