from sys import stdin
n = int(input())
# 데이터 저장용 공간 matrix 아파트 있는지 여부를 나타냄
matrix = [[0]*n for _ in range(n)]
# 방문 내역 저장용 visited 같은 0으로 채워진 인접행렬을 만들어서 방문 여부를 판단하는 행렬로 쓰인다.
visited = [[0]*n for _ in range(n)]

# matrix에 아파트 유무 0과 1을 입력해준다.
for i in range(n):
    line = stdin.readline().strip()  #strip은 문자열 제거 함수 파라미터 안에 있는 것을 제거해준다.
    for j, b in enumerate(line):
        matrix[i][j] = int(b)

# 방향 확인용 좌표 dx와 dy
# 중앙을 기준으로 좌/우/위/아래
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
nums = 0 

# DFS 함수 정의
def dfs(x, y, c):
    visited[x][y] = 1   # 방문 여부 표시 방문했음을 visited 매트릭스에 저장해준다.
    global nums           # 아파트 단지 수를 세기위한 변수
    # 아파트가 있으면 숫자를 세어줍니다.
    if matrix[x][y] == 1:
        nums += 1
    # 해당 위치에서 좌/우/위/아래 방향의 좌표를 확인해서 dfs 적용
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n: #nx와 ny가 matrix의 범위 내인지 확인 
            if visited[nx][ny] == 0 and matrix[nx][ny] == 1: #visited가 0 and matrix가 1: 아직 방문한 적은 없는데 아파트가 있다.
                dfs(nx,ny, c) #재귀호출로 dfs 다시 진행

cnt = 1 # 아파트 단지 세기 위한
numlist = [] # 아파트 단지별 숫자
nums = 0 # 아파트 수
for a in range(n):
    for b in range(n):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a,b,cnt) #처음 발견한 곳의 행렬 좌표와 단지 1이 들어간다.
            numlist.append(nums) #아파트 수가 numlist 안에 저장.
            nums = 0


print(len(numlist)) #아파트 단지수
for n in sorted(numlist):
    print(n) #단지별 아파트의 개수

