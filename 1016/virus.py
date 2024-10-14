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
print(visited)