from collections import deque
import sys, pprint
sys.stdin = open('7569.txt')
input = sys.stdin.readline


def ripening_day_3d():
    while queue:
        x, y, z = queue.popleft()
        # 3차원이므로 육방탐색
        for l in range(6):
            nx = x + dx[l]
            ny = y + dy[l]
            nz = z + dz[l]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and box[nz][ny][nx] == 0:
                queue.append((nx, ny, nz))
                box[nz][ny][nx] = box[z][y][x] + 1


M, N, H = map(int, input().split())
# 3차원 리스트 입력
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# 위아래 앞뒤 좌우
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
cnt = 0
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                cnt += 1
            elif box[i][j][k] == 1:
                queue.append((k, j, i))
if cnt == 0:
    print(0)
else:
    ripening_day_3d()
    # pprint.pprint(box)
    is_unripened = False
    for a in range(H):
        for b in range(N):
            for c in range(M):
                if box[a][b][c] == 0:
                    is_unripened = True
                    break
    if is_unripened:
        print(-1)
    else:
        # 각 층(2차원 리스트)의 최댓값을 담은 리스트 생성
        floor_max = [max(map(max, box[d])) for d in range(H)]
        print(max(floor_max) - 1)