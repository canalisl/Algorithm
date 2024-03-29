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
                if next <= 100:
                    if next in ladder:
                        next = ladder[next]
                    elif next in snake:
                        next = snake[next]
                    # 사다리나 뱀을 만나 <이동한 후> 위치의 방문여부가 중요하므로 마지막에 체크
                    if not visited[next]:
                        visited[next] = visited[now] + 1
                        queue.append(next)
            

N, M = map(int, input().split())
ladder = dict()
snake = dict()
dice = [1, 2, 3, 4, 5, 6]
for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y
for _ in range(M):
    u, v = map(int, input().split())
    snake[u] = v
visited = [0] * 101
print(snake_ladder_game(1))
