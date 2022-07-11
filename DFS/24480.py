import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('24480.txt')
input = sys.stdin.readline


def dfs_reverse(E, start, visited):
    global order
    visited[start] = True
    order_list[start] = order
    order += 1
    for i in E[start]:
        if not visited[i]:
            dfs_reverse(E, i, visited)


N, M, R = map(int, input().split())
# graph = [[1] for _ in range(N + 1)] ->  [[1], [1], [1], [1], [1], [1]] 배열 자체의 갯수 늘림
# graph = [[1] * (N + 1)] -> [[1, 1, 1, 1, 1, 1]] / 배열 안의 원소 갯수 늘림
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for edge in graph:
    edge.sort(reverse=True)

visited = [False] * (N + 1)
order_list = [0] * (N + 1)
order = 1
dfs_reverse(graph, R, visited)
for j in range(1, N + 1):
    print(order_list[j])
