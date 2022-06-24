# page. 152 미로 탈출
from collections import deque
import sys
sys.stdin = open('BFS_page152.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]



# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어났거나 괴물이면 건너뛰기
            if nx < 0 or nx >= N or ny < 0 or ny >= M or maze[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            elif maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    return maze[N - 1][M - 1]

print(bfs(0, 0))