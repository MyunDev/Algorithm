n = int(input())
home_data = list(map(int, input().split()))
home_data.sort()

print(home_data[(n - 1)//2])
