n, k = map(int, input().split())
count = 0

while n >= k :
    #n 이 나누어 떨어지지 않을 때 1씩 빼기 
    while n % k != 0:
        n -= 1
        count += 1
    #n이 나누어 떨어질 때 나누고 count 증가시키기
    n = n // k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)
