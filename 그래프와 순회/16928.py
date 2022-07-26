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
        else:
            for i in range(6):
                next = now + dice[i]
                if 1 <= next <= 100:
                    if next in ladderX:
                        next = ladderY[ladderX.index(next)]
                    elif next in snakeU:
                        next = snakeV[snakeU.index(next)]
                    # 사다리나 뱀을 만나 <이동한 후> 위치의 방문여부가 중요하므로 마지막에 체크
                    if not visited[next]:
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