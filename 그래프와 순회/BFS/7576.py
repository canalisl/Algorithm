from collections import deque
import sys, pprint
sys.stdin = open('7576.txt')
input = sys.stdin.readline

def ripening_day(x, y):
    global day
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and box[ny][nx] == 0:
                queue.append((nx, ny))
                box[ny][nx] = box[y][x] + 1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
day = 0
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            cnt += 1
        if box[i][j] == 1:
            ripening_day(j, i)
pprint.pprint(box)
print(day)