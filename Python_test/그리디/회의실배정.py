import sys

n = int(input())
time_list = [[0]*2 for _ in range(n)]

for i in range(n):
    start_time, end_time = map(int, sys.stdin.readline().split())
    time_list[i][0] = start_time
    time_list[i][1] = end_time

time_list.sort(key = lambda x: (x[1],x[0]) )

count = 1
end_time = time_list[0][1]
for i in range(1, n):
    if time_list[i][0] >= end_time:
        count += 1
        end_time = time_list[i][1]

print(count)
