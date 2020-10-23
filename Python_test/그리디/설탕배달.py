#백준 설탕배달
#https://www.acmicpc.net/problem/2839

n = int(input())
count = 0

while True:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    n = n - 3
    count += 1
    if n < 0:
        print('-1')
        break    



