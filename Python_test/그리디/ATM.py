#백준 알고리즘
#https://www.acmicpc.net/problem/11399

n = int(input())
time = list(map(int, input().split()))
time.sort()

result = 0 

#for i in range(n):
#    for j in range(i + 1):
#        result += time[j]


for i in range(n):
    result += sum(time[:i+1])


print(result)
