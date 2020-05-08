import sys

key = sys.stdin.readline().split()

seven_guys = list(key)
seven_guys = list(map(int, seven_guys))

res = sum(seven_guys)
seven_guys.sort()

for i in range(len(seven_guys)):
    for j in range(i+1, len(seven_guys)):
        if res - seven_guys[i] - seven_guys[j] == 100:
            for k in range(len(seven_guys)):
                if k == i or k == j:
                    continue
                else:
                    print(seven_guys[k])
                    