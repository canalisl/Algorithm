import sys, pprint
sys.stdin = open('1012.txt')
# RecursionError 방지
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def count_earthworm_dfs(x, y):
    global cnt
    farm[y][x] = False
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and farm[ny][nx]:
            count_earthworm_dfs(nx, ny)


T = int(input().rstrip())
# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[False] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = True
    # pprint.pprint(farm)
    # 지렁이 마릿수 초기화
    cnt = 0
    # 각 구역별 배추 포기수
    total_earthworm = []
    for i in range(N):
        for j in range(M):
            if farm[i][j]:
                count_earthworm_dfs(j, i)
                total_earthworm.append(cnt)
                cnt = 0
    # print(*total_earthworm)
    print(len(total_earthworm))
    