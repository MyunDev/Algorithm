import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
ans = 0

def prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in num_list:
    if prime(i):
        ans += 1

print(ans)

