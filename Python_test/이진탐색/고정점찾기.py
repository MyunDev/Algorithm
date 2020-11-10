def binary_search(data, start, end):
    if start > end:
        None
    mid = (start + end) // 2

    if data[mid] == mid:
        return mid
    elif data[mid] > mid:
        return binary_search(data, start, mid - 1)
    else:
        return binary_search(data, mid+1, end) 


n = int(input())
data = list(map(int, input().split()))

index = binary_search(data, 0, n-1)

if index == None:
    print(-1)
else:
    print(index)