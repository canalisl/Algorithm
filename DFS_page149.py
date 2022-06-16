# page. 149 음료수 얼려 먹기

import sys
sys.stdin = open('DFS_page149.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
tray = []
for _ in range(N):
    tray.append(list(map(int, input().rstrip()))) 
# 아이스크림 갯수
cnt = 0

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if tray[y][x] == 0:
        # 현재 노드 방문 처리
        tray[y][x] = 1
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        # 상하좌우 모두 체크 끝난 노드에는 True 할당
        return True
    # 방문한 노드라면 False 할당하고 호출했던 위치로 되돌아감
    return False

# 좌측 위부터 dfs 시작
# 얼음 덩어리의 첫 요소에서 dfs를 하면 연결된 모든 부분이 1로 바뀌므로 중복해서 카운트되지 않음
# 즉 연결된 다른 노드에서 출발하는 dfs는 모두 False가 반환됨(이미 1로 바뀌었으므로)
for i in range(M):
    for j in range(N):
        if dfs(i, j) == True:
            cnt += 1

print(cnt)



