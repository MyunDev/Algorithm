# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())

array = list(map(int, input().split()))

#array.sort()

start = 0
end = max(array)

#나무 높이 담을 공간
result = 0

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0 
        for x in array:
            if x > mid:
                total += x - mid
            
        if total < m:
            end = mid - 1
        else:
            start = mid + 1
            return mid




print(result) 
