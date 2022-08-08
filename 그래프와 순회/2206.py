from collections import deque
import sys
sys.stdin = open('2206.txt')
input = sys.stdin.readline


def breaking_wall(x, y):
    queue = deque()
    queue.append((x, y))
    map[y][x] = 1
    while queue:
        xi, yi = queue.popleft()
        for i in range(4):
            nx = xi + dx[i]
            ny = yi + dy[i]
            if 0 <= nx < M and 0 <= ny < N and map[ny][nx] == 0:
                queue.append((nx, ny))
                map[ny][nx] = map[y][x] + 1


N, M = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(N)]
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
breaking_wall(0, 0)
print(map)