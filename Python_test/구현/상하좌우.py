n = int(input())
x, y = 1, 1

plans = input().split()

#방향 지정 L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

#이동 계획 확인
for plan in plans:
    #이동 후 좌표 확인
    for i in range(len(move_type)):
        if plan == move_type[i]:
            nx = x + dx[i]
            ny = y + dy[i]    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue 

    #좌표 이동  
    x,y = nx, ny

print(x, y)
