n, k  = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True) #배열 B는 내림차순 정렬 수행

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: 
        break 

print(sum(a))