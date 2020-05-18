import sys

N = int(sys.stdin.readline())
numbers = []

for i in range(N):
    numbers.append(list(map(int,sys.stdin.readline().split())))

numbers.sort(key = lambda x : (x[0],x[1]))


for x,y in numbers:
    print(x,y)