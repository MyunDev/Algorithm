n, m = map(int, input().split())

array = []
for _ in range(n):
  array.append(list(map(int, input().split())))


new_array = []
for num in array:
  new_array.append(min(num))

print(max(new_array))