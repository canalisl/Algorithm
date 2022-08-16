from collections import deque

def solution(maps):
    answer = BFS(0, 0, maps)
    return answer


def BFS(x, y, maps):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    m = len(maps)   # 행 번호
    n = len(maps[0])    # 열 번호
    queue = deque()
    queue.append((x, y))
    while queue:
        xi, yi = queue.popleft()
        if xi == n - 1 and yi == m - 1:
            return maps[m - 1][n - 1]
        for i in range(4):
            nx = xi + dx[i]
            ny = yi + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[ny][nx] == 1:
                maps[ny][nx] = maps[yi][xi] + 1
                queue.append((nx, ny))
    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))