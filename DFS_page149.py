# page. 149 음료수 얼려 먹기

import sys
sys.stdin = open('DFS_page149.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
tray = []
for _ in range(M):
    tray.append(list(input().rstrip())) 
# 아이스크림 갯수
cnt = 0
visited = [[False] * N for _ in range(M)]
for x in range(N):
    for y in range(M):
        if tray[y][x] == '0' and visited[y][x] == False:
            start_x, start_y = x, y
            break
    break

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited[start_y][start_x] = True

while True:
    for i in range(4):
        if tray[y+dy[i]][x+dx[i]] == '0' and visited[y+dy[i]][x+dx[i]] == False:
            ny = y + dy[i]
            nx = x + dx[i]
            visited[ny][nx] = True
            x, y = nx, ny
        break
    break




print(visited)



