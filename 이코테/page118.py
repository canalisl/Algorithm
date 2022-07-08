import sys
sys.stdin = open('page118.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
cnt = 0

#  북동남서
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 처음 지점 방문체크
visited[y][x] = 1

while True:
    # 왼쪽으로 회전
    d = (d + 3) % 4
    # '서 있는 방향 기준 왼쪽' 칸이 가보지 않은 곳이고 & 바다가 아니라면
    if visited[y + dy[d]][x + dx[d]] == 0 and map[y + dy[d]][x + dx[d]] != 1:
        #  왼쪽으로 이동하고
        nx = x + dx[d]
        ny = y + dy[d]
        #  방문체크
        visited[ny][nx] = 1
        # 새로운 칸으로 이동했으므로 방문실패 cnt 초기화
        cnt = 0
        # 이동한 칸으로 좌표 변경
        x, y = nx, ny
    else:
        cnt += 1
        # 네 방향 모두 이미 가봤거나 OR 바다라면
        if cnt == 4:
            # 뒷칸이 바다가 아닐 때
            if map[y - dy[d]][x - dx[d]] != 1:
                # 그 상태에서 뒤로 한칸 이동
                nx = x - dx[d]
                ny = y - dy[d]
                # 방문체크
                visited[ny][nx] = 1
                # 새로운 칸으로 이동했으므로 방문실패 cnt 초기화
                cnt = 0
                # 이동한 칸으로 좌표 변경
                x, y = nx, ny
            # 그 뒷칸이 바다라면 이동 멈춤 = 끝!!
            else:
                break
        continue


# 방문한 칸 수 출력
visited_cnt = 0
for i in range(N):
    for j in range(M):
        if visited[j][i] == 1:
            visited_cnt += 1

print(visited_cnt)