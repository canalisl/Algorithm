from collections import deque
import sys
sys.stdin = open('24444.txt')
input = sys.stdin.readline

N, M, R = map(int, input().split())
E = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)
for edge in E:
    edge.sort()

visited = [False] * (N + 1)
order_list = [0] * (N + 1)
order = 1


def bfs(E, R, visited):
    global order
    visited[R] = True
    order_list[R] = order
    order += 1
    queue = deque()
    queue.append(R)
    while queue:
        next = queue.popleft()
        for i in E[next]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                order_list[i] = order
                order += 1


bfs(E, R, visited)
for j in range(1, N + 1):
    print(order_list[j])

