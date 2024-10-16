num = int(input()) #컴퓨터수
net = int(input()) #네트워크 연결 컴퓨터수

# 그래프 초기화
graph = [[] for _ in range(num + 1)]

# 간선 정보 입력받기
for _ in range(net):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 기록 리스트
visited = [False] * (num + 1)

# DFS 함수
def dfs(n):
    visited[n] = True # 현재 노드 방문처리
    for i in graph[n]:
        if not visited[i]: # 방문하지 않은 노드이면
            dfs(i) # 방문처리
            
dfs(1) #1번부터 탐색

print(visited.count(True)-1)