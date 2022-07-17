import sys, pprint
sys.stdin = open('2667.txt')
input = sys.stdin.readline

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_new_unit():
    for i in range(N):
        for j in range(N):
            if map[i][j] == 1 and not visited[i][j]:
                start_y, start_x = i, j
                break
        break
    numbering_complex(start_x, start_y)


def numbering_complex(x, y):
    visited[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and map[ny][nx] == 1:
            numbering_complex(nx, ny)


N = int(input().rstrip())
map = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
find_new_unit()
pprint.pprint(visited)