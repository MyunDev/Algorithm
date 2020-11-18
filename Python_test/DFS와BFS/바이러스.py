# https://www.acmicpc.net/problem/2606

n = int(input())
k = int(input())
start = 1
#연결된 그래프 초기화
graph = [[] for _ in range(n + 1)] 

#그래프 정보 입력하기
for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# [ [], [2, 5], [3], [], [7], [2, 6], [], []]

# 노드의 방문 여부 나타내기
visited = [False] * (n + 1)

def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


cnt = 0 

dfs(graph, 1, visited)
    
for i in visited:
    if i == True:
        cnt += 1



print(cnt-1)






