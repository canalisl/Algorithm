from collections import deque
import sys, pprint
sys.stdin = open('2206.txt')
input = sys.stdin.readline


def breaking_wall(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    while queue:
        xi, yi, zi = queue.popleft()
        # 마지막 칸에 도달하면
        if xi == M - 1 and yi == N - 1:
            # 최단거리 출력
            return visited[yi][xi][zi]
        for i in range(4):
            nx = xi + dx[i]
            ny = yi + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                # 마주친 칸이 벽이고 & 아직 부순 적이 없다면
                if map[ny][nx] == 1 and zi == 0:
                    visited[ny][nx][1] = visited[yi][xi][0] + 1
                    queue.append((nx, ny, 1))
                # 벽이 아니고 & 방문한 적이 없다면
                elif map[ny][nx] == 0 and visited[ny][nx][zi] == 0:
                    visited[ny][nx][zi] = visited[yi][xi][zi] + 1
                    queue.append((nx, ny, zi))
    return -1


N, M = map(int, input().split())
map = [list(map(int, input().rstrip())) for _ in range(N)]
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 3차원 리스트로 벽 파괴 여부 파악  ex) visited[y][x][0]은 파괴 가능 visited[y][x][1]은 파괴 불가능
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
print(breaking_wall(0, 0, 0))
# pprint.pprint(visited)