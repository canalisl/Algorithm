from collections import deque
import sys
sys.stdin = open('7562.txt')
input = sys.stdin.readline


def knight_bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        if (x, y) == (v, w):
            return visited[y][x]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + 1
                queue.append((nx, ny))


T = int(input().rstrip())
# 1시부터 시계방향으로
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
for _ in range(T):
    l = int(input().rstrip())
    x, y = map(int, input().split())
    v, w = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    print(knight_bfs(x, y))