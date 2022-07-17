import sys, pprint
sys.stdin = open('2667.txt')
input = sys.stdin.readline
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def find_new_unit():
    global number
    for i in range(N):
        for j in range(N):
            if map[i][j] == 1 and not visited[i][j]:
                numbering_complex(j, i)
                number += 1

    
def numbering_complex(x, y):
    # 단지 번호
    # print(f'ny는 {y}이고, nx는 {x}입니다.' )
    visited[y][x] = number
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and map[ny][nx] == 1:
            numbering_complex(nx, ny)
    # print(f'더 이상 갈 곳이 없습니다. nx는 {nx}이고, ny는 {ny}입니다.' )


number = 1
N = int(input().rstrip())
map = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
find_new_unit()
pprint.pprint(visited)