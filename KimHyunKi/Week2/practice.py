import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    d = gcd(a, b)
    return int(a * b // d)

T = int(sys.stdin.readline())

for i in range(T):
    num1, num2 = map(int, sys.stdin.readline().split())
    
    print(lcm(num1, num2))



