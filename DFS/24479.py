import sys
sys.stdin = open('24479.txt')
# RecursionError를 방지하기 위한 설정
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
E = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
# 오름차순으로 방문하기 위한 인접 노드 리스트 오름차순 정렬
for edge in E:
    edge.sort()
# 방문 순서 나타내기 위한 리스트 생성
# ex. 3번 인덱스 값 2 -> 3번 노드는 두 번째로 방문했다 
order_list = [0] * (N + 1)
# 첫 순서이므로 1로 order 초기화
order = 1
visited = [False] * (N + 1)


def dfs(graph, v, visited):
    global order
    visited[v] = True
    order_list[v] = order
    # 순서 1 증가
    order += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(E, R, visited)
# 각 노드의 방문순서 출력
for i in range(1, N + 1):
    print(order_list[i])