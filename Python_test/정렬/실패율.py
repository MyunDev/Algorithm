# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    result = {}
    num = len(stages)

    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count
        else:
            #스테이지에 도달하지 못하여 실패율이 0인 경우 N:3 , [1,1,1] 인 경우 나머지 스테이지 실패율 전부 0
            result[stage] = 0

    return sorted(result, key = lambda x : result[x], reverse=True)