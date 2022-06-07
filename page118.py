import sys
sys.stdin = open('page118.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(M)]
cnt = 0

#  북동남서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 처음 지점 방문체크
visited[x][y] = 1

while True:
    # 왼쪽으로 회전
    d = (d + 3) % 4
    # '서 있는 방향 기준 왼쪽' 칸이 가보지 않은 곳이고 & 바다가 아니라면
    if visited[x + dx[d]][y + dy[d]] == 0 and map[x + dx[d]][y + dy[d]] != 1:
        #  왼쪽으로 이동하고
        nx = x + dx[d]
        ny = y + dy[d]
        #  방문체크
        visited[nx][ny] = 1
    else:
        cnt += 1
        # 네 방향 모두 이미 가봤거나 OR 바다라면
        if cnt == 4:
            if map[x - dx[d]][y - dy[d]] != 1:
                # 그 상태에서 뒤로 한칸 이동
                nx = x - dx[d]
                ny = y - dy[d]
                # 방문체크
                visited[nx][ny] = 1
            # 그 뒷칸이 바다라면 이동 멈춤 = 끝!!
            break
        continue

    x, y = nx, ny

# 방문한 칸 수 출력
visited_cnt = 0
for i in range(N):
    for j in range(M):
        if visited[i][j] == 1:
            visited_cnt += 1

print(visited_cnt)