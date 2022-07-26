from collections import deque
import sys
sys.stdin = open('16928.txt')
input = sys.stdin.readline


def snake_ladder_game(n):
    queue = deque()
    queue.append(n)
    while queue:
        now = queue.popleft()
        if now == 100:
            return visited[now]
        # 사다리 있는 칸이면
        elif now in ladderX and not visited[ladderY[ladderX.index(now)]]:
            # 타고 올라가고
            next = ladderY[ladderX.index(now)]
            visited[next] = visited[now] + 1
            queue.append(next)
        # 뱀 있는 칸이면
        elif now in snakeU and not visited[snakeV[snakeU.index(now)]]:
            # 내려오고
            next = snakeV[snakeU.index(now)]
            visited[next] = visited[now] + 1
            queue.append(next)
        else:
            for i in range(6):
                next = now + dice[i]
                if 1 <= next <= 100 and not visited[next]:
                    visited[next] = visited[now] + 1
                    queue.append(next)
            

N, M = map(int, input().split())
ladderX = []
ladderY = []
snakeU = []
snakeV = []
dice = [1, 2, 3, 4, 5, 6]
for _ in range(N):
    x, y = map(int, input().split())
    ladderX.append(x)
    ladderY.append(y)
for _ in range(M):
    u, v = map(int, input().split())
    snakeU.append(u)
    snakeV.append(v)
visited = [0] * 101
print(snake_ladder_game(1))