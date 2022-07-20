import sys
sys.stdin = open('2667.txt')
input = sys.stdin.readline

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def numbering_complex_dfs(x, y):
    global count
    # 1인 지역을 지날 때 해당 지점을 0으로 변경
    map[y][x] = 0
    # 집의 수 +1
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and map[ny][nx] == 1:
            numbering_complex_dfs(nx, ny)
        

N = int(input().rstrip())
map = [list(map(int, input().rstrip())) for _ in range(N)]
count = 0
house_complex = []
# 방문한 적 없고 '1'인 시작점 찾기
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            numbering_complex_dfs(j, i)
            # print('DFS 한 사이클 끝')
            # 한 번 DFS 끝나면 해당 단지 탐색이 끝난 것이므로 count 정산
            house_complex.append(count)
            # 다음 단지 탐색 전 집의 수 초기화
            count = 0
print(len(house_complex))
for number in sorted(house_complex):
    print(number)

