from collections import deque
import sys, pprint
sys.stdin = open('7576.txt')
input = sys.stdin.readline


def ripening_day():
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
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0
queue = deque()
for i in range(N):
    for j in range(M):
        # 첫 날 안 익은 토마토 갯수 세기
        if box[i][j] == 0:
            cnt += 1
        elif box[i][j] == 1:
            # 여기서 바로 BFS 시작하지 않고 익은 토마토 노드를 큐에 추가
            queue.append((j, i))
# 처음부터 모든 토마토가 익어있다면
if cnt == 0:
    # 0 출력하고 종료
    print(0)
else:
    # 익은 토마토 각각에서 동시에 BFS 시작
    ripening_day()
    # 안 익은 토마토가 남아있는지 체크
    is_unripened = False
    for k in range(N):
        for l in range(M):
            if box[k][l] == 0:
                is_unripened = True
                break
    if is_unripened:
        print(-1)
    else:
        # 익는데 걸리는 날짜 = 박스 최댓값 -1
        print(max(map(max, box)) - 1)