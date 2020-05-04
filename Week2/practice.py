import sys

num1, num2 = list(map(int, sys.stdin.readline().split()))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)



print(gcd(num1,num2))
print(num1 * num2 // gcd(num1,num2))



