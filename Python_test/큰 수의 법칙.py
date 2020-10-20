import sys

n, m, k = map(int, input().split())
data = list(map(int, sys.stdin.readline().split()))

data.sort()
first_num = data[-1]
second_num = data[-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first_num
        m -= 1
    if m == 0:
        break
    result += second_num
    m -= 1

print(result)

