from collections import deque
import sys, pprint
sys.stdin = open('2178.txt')
input = sys.stdin.readline

def find_exit_bfs(x, y, maze):
    global cnt
    queue = deque()
    queue.append((x, y))
    while queue:
        xi, yi = queue.popleft()
        for i in range(4):
            nx = xi + dx[i]
            ny = yi + dy[i]
            # 시작점(0, 0)은 탐색에서 제외
            if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] == 1 and (nx != 0 or ny != 0):
                queue.append((nx, ny))
                maze[ny][nx] = maze[yi][xi] + 1


N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
find_exit_bfs(0, 0, maze)
# pprint.pprint(maze)
print(maze[N - 1][M - 1])
