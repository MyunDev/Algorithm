# https://programmers.co.kr/learn/courses/30/lessons/12926
# https://data-science-blog.tistory.com/1

def solution(s, n):
    answer = ''
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for string in s:
        if string in low:
            low_idx = low.find(string) + n
            answer += low[low_idx % 26]
        elif string in up:
            up_idx = up.find(string) + n
            answer += up[up_idx % 26]
        else:
            answer += " "
    return answer


