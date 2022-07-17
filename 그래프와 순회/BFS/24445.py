from collections import deque
import sys
sys.stdin = open('24445.txt')
input = sys.stdin.readline


def bfs_reverse(E, R, visited):
    queue = deque()
    queue.append(R)
    global order
    visited[R] = True
    order_list[R] = order
    order += 1
    while queue:
        start = queue.popleft()
        for i in E[start]:
            if not visited[i]:
                visited[i] = True
                order_list[i] = order
                order += 1
                queue.append(i)


N, M, R = map(int, input().split())
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
bfs_reverse(graph, R, visited)
for j in range(1, N + 1):
    print(order_list[j])