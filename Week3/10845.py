import sys

N = int(sys.stdin.readline())
qu = []

for k in range(N):
    cmd_list = list(sys.stdin.readline().split())
    if cmd_list[0] == 'push':
        qu.append(cmd_list[1])
    elif cmd_list[0] == 'pop':
        if qu:
            print(qu[0])
            qu.pop(0)
        else:
            print(-1)
    elif cmd_list[0] == 'size':
        print(len(qu))
    elif cmd_list[0] == 'empty':
        if qu:
            print(0)
        else:
            print(1)
    elif cmd_list[0] == 'front':
        if qu:
            print(qu[0])
        else:
            print(-1)
    elif cmd_list[0] == 'back':
        if qu:
            print(qu[-1])
        else:
            print(-1)