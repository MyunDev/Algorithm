n = int(input())

num_len = len(str(n))
final_len = num_len // 2

result_a = 0
result_b = 0

array = []

for i in str(n):
    array.append(i)

list_a = list(map(int, array))

for i in range(final_len):
    result_a += list_a[i]

for i in range(final_len, num_len):
    result_b += list_a[i]


if result_a == result_b:
    print("LUCKY")
else:
    print("READY")

