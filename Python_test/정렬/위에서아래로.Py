n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(input()))

num_list.sort(reverse=True)

# print(num_list) 배열 형태로 출력됨

for i in num_list:
    print(i, end= ' ')