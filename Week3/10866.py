import sys

N = int(sys.stdin.readline())
Deque = []


for x in range(N):
    k = list(sys.stdin.readline().split())

    if k[0] == "push_front":
        Deque.insert(0,k[1])
    elif k[0] == "push_back":
        Deque.append(k[1])
    elif k[0] == "pop_front":
        if Deque:
            print(Deque.pop(0))
        else: 
            print(-1)
    elif k[0] == "pop_back":
        if Deque:
            print(Deque.pop(-1))
        else: 
            print(-1)
    elif k[0] == "size":
        print(len(Deque))
    elif k[0] == "empty":
        if Deque:
            print(0)
        else:
            print(1)
    elif k[0] == "front":
        if Deque:
            print(Deque[0])
        else:
            print(-1)
    elif k[0] == "back":
        if Deque:
            print(Deque[-1])
        else:
            print(-1)
