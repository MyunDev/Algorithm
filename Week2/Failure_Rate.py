def solution(N, stages):
    result = {}
    num = len(stages)

    for stage in range(1, N+1):
        if num != 0:
            user = stages.count(stage)
            result[stage] = user / num
            num -= user
        else:
            result[stage] = 0

    return sorted(result, key=lambda x : result[x], reverse=True)