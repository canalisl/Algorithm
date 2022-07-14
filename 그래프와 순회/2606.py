from collections import deque
import sys
sys.stdin = open('2606.txt')
input = sys.stdin.readline


def count_infected_pc(network, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        infected = queue.popleft()
        for pc in network[infected]:
            if not visited[pc]:
                queue.append(pc)
                visited[pc] = True


N = int(input().rstrip())
M = int(input().rstrip())
network = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    network[u].append(v)
    network[v].append(u)
visited = [False] * (N + 1)

count_infected_pc(network, 1, visited)
print(visited.count(True) - 1)  # 1번 컴퓨터는 제외