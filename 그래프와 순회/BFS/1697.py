from collections import deque
import sys
sys.stdin = open('1697.txt')
input = sys.stdin.readline


def find_kids_bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        now = queue.popleft()
        if now == K:
            return visited[now]
        for next in (now - 1, now + 1, 2*now):
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = visited[now] + 1
                queue.append(next)
            

N, K = map(int, input().split())
visited = [0] * 100001
print(find_kids_bfs(N))
