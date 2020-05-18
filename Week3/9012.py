import sys
T = int(sys.stdin.readline())

for _ in range(T):
    line = sys.stdin.readline()
    stack =[]
    cnt = 0
    for check in line:
        if cnt < 0:
            break
        if check =='(':
            stack.append(check)
            cnt += 1
        elif check ==')':
            if len(stack)>0:
                stack.pop()
                cnt -= 1
            else:
                cnt = -1
                break

    if cnt == 0:
        print("YES")
    else:
        print("NO")

