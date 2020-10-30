#https://www.acmicpc.net/problem/2583

def dfs(x, y):
    stack = [(x, y)]
    graph[x][y] = 1
    num = 1

    while stack:
        x, y = stack.pop()
        for dx, dy in zip(direction_x, direction_y):
            nx, ny = x + dx, x + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                stack.append((nx, ny))
                graph[nx][ny] == 1
                num += 1
    answer_list.append(num)

m, n, k = map(int, input().split())
graph = [[0]* n for _ in range(m)]

#안에 표시해야 할 직사각형 1로 미리 표시해두기
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split()) # 0 2 4 4 
    for j in range(y1, y2): # 2, 4 
        for k in range(x1, x2): # 0, 4
            graph[j][k] = 1

#상, 하, 좌, 우
direction_x = [0, 0, -1, 1]
direction_y = [1, -1, 0, 0]

answer_list = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            dfs(i, j)


print(len(answer_list))
print(' '.join(map(str, sorted(answer_list))))


