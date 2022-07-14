from collections import deque
import sys
sys.stdin = open('1260.txt')
input = sys.stdin.readline


def DFS(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for next in graph[start]:
        if not visited[next]:
            visited[next] = True
            DFS(graph, next, visited)


def BFS(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    print(start, end=' ')
    while queue:
        start = queue.popleft()
        for next in graph[start]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                print(next, end=' ')


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for edge in graph:
    edge.sort()
visited = [False] * (N + 1)
DFS(graph, V, visited)
print()
# visited 초기화
visited = [False] * (N + 1)
BFS(graph, V, visited)