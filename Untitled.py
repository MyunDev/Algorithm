import sys
#lst = list(map(int, input().split()))
def solution():
    lst = list(map(int, sys.stdin.readline().split()))
    N = lst[0]
    answer = []

    for i in range(N):
        lst = list(map(int, sys.stdin.readline().split()))
        answer.append(min(lst))
    return max(answer)


print(solution()) 

