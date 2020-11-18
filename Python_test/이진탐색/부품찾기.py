n = int(input())

store = list(map(int, input().split()))

m = int(input())
guest = list(map(int, input().split()))


store.sort()
guest.sort()

def binary_search(store, target, start, end):
    while start <= end:
        
        mid = (start + end) // 2

        if store[mid] == target:
            return mid
        elif store[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return None
        



for i in guest:
    result = binary_search(store, i, 0, n - 1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

